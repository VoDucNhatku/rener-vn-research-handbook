"""Read-only checks of authored docs/originals/snapshot manifests; writes audit results."""
from pathlib import Path
from urllib.parse import unquote
from collections import Counter
import hashlib, json, re, datetime, sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
inventory = json.loads(read(HERE/'inventory.json'))
files = [ROOT/x['file'] for x in inventory]
files += [ROOT/'notes/HIEN-TRANG-VA-QUYET-DINH.md']
files += list(HERE.glob('*.md'))
docs, broken, count = [], [], 0
for p in files:
    txt = read(p)
    fences = re.findall(r'^\s*```', txt, re.M)
    outside = re.sub(r'^\s*```[^\n]*\n.*?^\s*```\s*$', '', txt, flags=re.M|re.S)
    for m in re.finditer(r'\[[^\]\n]+\]\((<[^>\n]+>|[^)\n]+)\)',outside):
        target = m.group(1).strip('<>')
        if re.match(r'^(https?://|mailto:|app:|codex:|#)',target): continue
        target=unquote(target.split('#')[0])
        if not target: continue
        dest=Path(target) if Path(target).is_absolute() else p.parent/target
        count += 1
        if not dest.exists():broken.append({'file':p.relative_to(ROOT).as_posix(),'target':target})
    docs.append({'file':p.relative_to(ROOT).as_posix(),'sha256_after':digest(p),
                 'fences_balanced':len(fences)%2==0,'replacement_characters':txt.count('\ufffd')})

source_checks=[]; skipped=[]
source_root=ROOT/'notes/kusshoes-to-rener-vn/sources'
for folder in source_root.iterdir():
    if not folder.is_dir():continue
    for name in ['manifest.json','source-manifest.json','code-manifest.json']:
        mf=folder/name
        if not mf.exists():continue
        data=json.loads(read(mf))
        if isinstance(data,dict):
            data=next((data[k] for k in ['files','sources','entries'] if isinstance(data.get(k),list)),[])
        for i,row in enumerate(data):
            if not isinstance(row,dict) or not row.get('sha256'):
                skipped.append({'manifest':mf.relative_to(ROOT).as_posix(),'index':i,'reason':'no SHA256 recorded'})
                continue
            loc=row.get('local_path') or row.get('file')
            if not loc:
                skipped.append({'manifest':mf.relative_to(ROOT).as_posix(),'index':i,'reason':'no local path'})
                continue
            q=Path(loc)
            candidates=[q] if q.is_absolute() else [folder/q,ROOT/q]
            actual=next((x for x in candidates if x.is_file()),None)
            source_checks.append({'manifest':mf.relative_to(ROOT).as_posix(),'path':loc,
                                  'ok':bool(actual and digest(actual).lower()==row['sha256'].lower())})
originals=[]
for row in json.loads(read(HERE/'originals.json')):
    p=ROOT/row['file']; originals.append({**row,'unchanged':p.exists() and digest(p)==row['sha256']})

additional=[]
for row in json.loads(read(HERE/'additional-artifacts.json')):
    p=ROOT/row['file']; additional.append({**row,'unchanged':p.exists() and digest(p)==row['sha256']})
checks=[]
for name, prohibited in {
 'notes/kusshoes-to-rener-vn/TU-VIBE-CODING-DEN-GIAO-WEB.md': ['Running --> NeedsReview','snapshot được phép công khai'],
 'notes/kusshoes-to-rener-vn/SO-TAY-CHIA-VIEC-CHO-AI.md': ['S4 — đóng góp và duyệt để công khai'],
 'notes/design-rener-vn-waterfall.md': ['DOMAIN --> DB','NLP --> DB'],
 'notes/quy-chuan-ai-dev/PROMPT-KIEN-TRUC-GIAO-VIEC-AI.md': ['14 passed','2 passed','Verified: V1 ✅','Max ~400 changed lines','domain rules -> repository -> DB','không phụ thuộc vào độ dài prompt'],
 'TMG301_TongHopKienThuc.md': ['không bị hạn chế bởi độ dài chuỗi dài','cây bao trùm nhỏ nhất (Minimum Spanning Tree)'],
 'notes/08-fine-tuning-mlm-summary.md': ['token `[MASK]` **không bao giờ xuất hiện**','giữ nguyên kiến trúc và tham số gốc'],
}.items():
    txt=read(ROOT/name)
    for phrase in prohibited:checks.append({'file':name,'removed_phrase':phrase,'ok':phrase not in txt})

old={x['file']:x['sha256_before'] for x in inventory}
changed=[x['file'] for x in docs if x['file'] in old and old[x['file']]!=x['sha256_after']]
out={'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'scope':'filesystem links excluding fenced examples, fence pairs, UTF8 replacement character, recorded hashes; no application tests or Mermaid render',
     'docs':docs,'changed_existing_documents':changed,'local_links_checked':count,'broken_local_links':broken,
     'source_hash_checks':source_checks,'source_entries_skipped':skipped,'originals':originals,
     'additional_artifacts':additional,'targeted_rescan':checks}
(HERE/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'documents':len(docs),'changed_existing':len(changed),'local_links':count,'broken':broken,
 'source_hashes':len(source_checks),'source_hash_failures':[x for x in source_checks if not x['ok']],
 'source_entries_skipped':len(skipped),'originals_unchanged':sum(x['unchanged'] for x in originals),
 'format_failures':[x['file'] for x in docs if not x['fences_balanced'] or x['replacement_characters']],
 'targeted_rescan_failures':[x for x in checks if not x['ok']],
 'additional_artifacts_unchanged':sum(x['unchanged'] for x in additional)},ensure_ascii=True,indent=2))
failed=bool(broken or any(not x['ok'] for x in source_checks+checks)
            or any(not x['unchanged'] for x in originals+additional)
            or any(not x['fences_balanced'] or x['replacement_characters'] for x in docs))
sys.exit(1 if failed else 0)
