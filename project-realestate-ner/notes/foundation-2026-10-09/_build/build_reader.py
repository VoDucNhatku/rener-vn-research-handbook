from pathlib import Path
import sys, re
from html import escape
sys.stdout.reconfigure(encoding='utf-8')

base = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(base / '_build' / 'deps'))
import markdown

source = (base / 'KIEN-THUC-NEN-TANG-RENER-VN.md').read_text(encoding='utf-8-sig')
rendered = markdown.markdown(source, extensions=['tables', 'fenced_code', 'toc'])
rendered = re.sub(r'<table>(.*?)</table>', r'<div class="table-scroll"><table>\1</table></div>', rendered, flags=re.S)
mini = '<div class="arch-mini" aria-label="Sơ đồ pipeline"><span>Seed / extension</span> → <span>Ingest</span> → <span>Extraction</span> → <span>Validator / Review</span> → <span>Observations / Comparables</span> → <span>Web</span><br><span>Review</span> → <span>Gold snapshot</span> → <span>Offline train / evaluate</span> → <span>Release</span></div>'
rendered = re.sub(r'<pre><code class="language-mermaid">.*?</code></pre>', mini, rendered, flags=re.S)
parts = re.split(r'(?=<h2 id=")', rendered)
intro, sections = parts[0], parts[1:]
toc, book = [], [intro]
for index, section in enumerate(sections, 1):
    match = re.search(r'<h2 id="([^"]+)">(.*?)</h2>', section)
    if not match:
        raise ValueError('Chapter heading not found')
    anchor, title = match.groups()
    section_id = f'chapter-{index}'
    section = section.replace(f'<h2 id="{anchor}">', f'<h2>', 1)
    toc.append(f'<li><a href="#{section_id}">{title}</a></li>')
    book.append(f'<section class="chapter" id="{section_id}">{section}</section>')
template = (base / '_build' / 'reader-template.html').read_text(encoding='utf-8')
output = template.replace('@@TOC@@', '<ul>'+''.join(toc)+'</ul>').replace('@@BOOK@@', ''.join(book))
(base / 'LO-TRINH-TRUC-QUAN.html').write_text(output, encoding='utf-8')
print({'chapters':len(sections),'markdown_chars':len(source),'html_chars':len(output),'output':str(base / 'LO-TRINH-TRUC-QUAN.html')})
