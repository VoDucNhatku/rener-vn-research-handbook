"""Build reading indexes from authored files without downloading or executing sources."""
from pathlib import Path
import json, re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
def read(p): return p.read_text(encoding='utf-8-sig')
def link(p): return '../'+quote(p.relative_to(ROOT).as_posix(), safe='/._-')
def candidates():
    files=[]
    for base in ['notes','project-realestate-ner/notes','KusShoes/notes']:
        for p in (ROOT/base).rglob('*.md'):
            if 'before' in p.parts: continue
            if 'sources' in p.parts and p.name!='README.md': continue
            files.append(p)
    files += [ROOT/'BAO-CAO-TONG-HOP-CONG-VIEC.md',ROOT/'TMG301_TongHopKienThuc.md']
    return sorted(set(files))

def build():
    files=candidates()
    out=['# Danh mục toàn bộ tài liệu nghiên cứu','',
         '[README](../README.md) · [Lộ trình](START-HERE.md) · [Bản đồ chủ đề](KNOWLEDGE-MAP.md)','',
         'Sinh từ các file do dự án viết, không tính full source bên ngoài hay bản forensic `before/` là kiến thức hiện hành. Bấm tên tài liệu để đọc; mở chi tiết để xem các mục đã có. Trạng thái hiện hành nằm ở [STATUS](STATUS.md).','',
         f'**{len(files)} tài liệu nghiên cứu/điều hướng nguồn** được liệt kê. Proposal, công cụ và bằng chứng có mục riêng phía dưới.','']
    registry=[]; refs={}
    for p in files:
        text=read(p)
        outside=re.sub(r'^\s*```[^\n]*\n.*?^\s*```\s*$','',text,flags=re.M|re.S)
        title=next((x.lstrip('# ').strip() for x in outside.splitlines() if x.startswith('# ')),p.stem)
        sections=re.findall(r'^## (.+)$',outside,re.M)
        registry.append({'path':p.relative_to(ROOT).as_posix(),'title':title,'sections':sections})
        out += [f'## {title}', '', f'[Mở tài liệu]({link(p)}) · `{p.relative_to(ROOT).as_posix()}`','',
                '<details><summary>Các mục trong tài liệu</summary>','']
        out += [f'- {s}' for s in sections] or ['- Tài liệu ngắn; đọc trực tiếp.']
        out += ['', '</details>', '']
        for label,url in re.findall(r'\[([^\]\n]+)\]\((https?://[^\s)]+)\)',outside):
            refs.setdefault(url,{'label':label,'documents':[]})['documents'].append(p.relative_to(ROOT).as_posix())
    out+=['## Proposal và hiện vật','',
          '- [Proposal v1.3 PDF](../project-realestate-ner/proposal-ReNER-VN-v1.3.pdf) và các phiên bản DOCX/XLSX trong `project-realestate-ner/`.','- [Reader HTML offline](../project-realestate-ner/notes/foundation-2026-10-09/LO-TRINH-TRUC-QUAN.html): snapshot lịch sử, không tự đồng bộ mọi đính chính.','- [Manifest nhập đầy đủ](../evidence/import-manifest.json): gồm file ngoài Markdown, script, ảnh, log và bản trước sửa.','- [Các điều chỉnh khi xuất](../evidence/export-adjustments.json) và [phần không xuất](../evidence/excluded-files.json).','']
    (ROOT/'docs/CATALOG.md').write_text('\n'.join(out),encoding='utf-8')
    (ROOT/'evidence/document-catalog.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    source_rows=json.loads(read(ROOT/'evidence/source-register.json'))
    unique={r['url']:r for r in source_rows}
    lines=['# Sổ nguồn tập trung','', '[README](../README.md) · [Bản đồ kiến thức](KNOWLEDGE-MAP.md) · [Phạm vi đóng gói](PACKAGING.md)','',
           'Có hai lớp: metadata snapshot lịch sử và các liên kết được nhắc trong tài liệu. Có URL không chứng minh đã đọc toàn bộ nguồn. Mức đọc/giới hạn cần xem báo cáo hoặc manifest tương ứng; số star/commit chỉ đúng theo ngày ghi nhận. Không tái phân phối full raw snapshot trong repo này.','',
           '## Nguồn có manifest','', f'{len(source_rows)} bản ghi metadata, {len(unique)} URL khác nhau. [JSON đầy đủ](../evidence/source-register.json).','',
           '| Nguồn | Hồ sơ ghi nhận |','|---|---|']
    for url,row in sorted(unique.items()):
        title=str(row['title']).replace('|','/').replace('\n',' ')[:140]
        manifest=row['manifest']
        lines.append(f'| [{title}]({url}) | [manifest](../{quote(manifest,safe="/._-")}) |')
    lines+=['','## Liên kết được nhắc trong phân tích','',
            'Danh mục sau giúp tra ngược; có thể gồm nguồn đọc một phần, công cụ tham khảo hoặc nội dung truy cập không thành công. Không coi mọi dòng là nguồn đã được kiểm chứng.','',
            '| Liên kết | Được nhắc ở |','|---|---|']
    for url,row in sorted(refs.items()):
        if url in unique: continue
        label=row['label'].replace('|','/').replace('[','').replace(']','')[:130]
        locations=sorted(set(row['documents']))
        refs_link='; '.join(f'[{Path(p).stem}](../{quote(p,safe="/._-")})' for p in locations[:3])
        lines.append(f'| [{label}]({url}) | {refs_link} |')
    lines+=['','## Phạm vi đã đọc gần nhất','',
            '[21 nguồn đọc sâu](../notes/nghien-cuu-sau-2026-10-11/SO-NGUON-DA-DOC.md) ghi từng mục đã đọc; các sổ nguồn trước nằm trong các thư mục `sources/` của nghiên cứu. Các link trỏ file nguồn được ghim commit khi manifest có commit.','']
    (ROOT/'docs/SOURCES.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'catalog_documents':len(files),'manifest_source_entries':len(source_rows),'manifest_unique_urls':len(unique),'linked_urls_in_authored_docs':len(refs)}))

if __name__=='__main__': build()
