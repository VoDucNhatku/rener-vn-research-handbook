from pathlib import Path
import json, urllib.request, hashlib, concurrent.futures, datetime, io, sys, re
from html.parser import HTMLParser
from pypdf import PdfReader

HERE=Path(__file__).resolve().parent
DEST=HERE/'sources';DEST.mkdir(exist_ok=True)

class Extract(HTMLParser):
    def __init__(self):
        super().__init__();self.skip=0;self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag in ['script','style','svg']:self.skip+=1
        if not self.skip and tag in ['p','div','h1','h2','h3','h4','li','tr','br','pre','section']:self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ['script','style','svg'] and self.skip:self.skip-=1
        if not self.skip and tag in ['p','div','h1','h2','h3','h4','li','tr','section']:self.parts.append('\n')
    def handle_data(self,s):
        if not self.skip:self.parts.append(s)

def fetch(row):
    out={**row,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'review_date_local':'2026-10-12','read_scope':'pending'}
    try:
        req=urllib.request.Request(row['url'],headers={'User-Agent':'Mozilla/5.0 (research source verification)'})
        with urllib.request.urlopen(req,timeout=30) as r:
            body=r.read();out['status']=r.status;out['final_url']=r.url
        pdf=body.startswith(b'%PDF');ext='.pdf' if pdf else '.html'
        raw=DEST/(row['id']+ext);raw.write_bytes(body)
        out.update(file=raw.name,bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
        if pdf:
            reader=PdfReader(io.BytesIO(body));out['pages']=len(reader.pages)
            text='\n\n'.join(f'=== PDF PAGE {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages))
        else:
            parser=Extract();parser.feed(body.decode('utf-8',errors='replace'))
            text=''.join(parser.parts);text=re.sub(r'\n[ \t]*\n+', '\n\n',text)
        f=DEST/(row['id']+'.txt');f.write_text(text,encoding='utf-8')
        out.update(text_file=f.name,text_chars=len(text),text_sha256=hashlib.sha256(f.read_bytes()).hexdigest())
    except Exception as e:out['error']=str(e)
    return out

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    rows=json.loads((HERE/'source-list.json').read_text(encoding='utf-8'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(fetch,rows))
    (DEST/'manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    for row in results:print(row['id'],row.get('status', 'ERROR'),row.get('text_chars',0),row.get('error',''))
