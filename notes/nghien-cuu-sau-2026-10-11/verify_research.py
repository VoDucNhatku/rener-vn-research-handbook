"""Verify document structure and recorded files; never runs the ReNER application."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import unquote
import hashlib, json, re, sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
AUDIT = ROOT/'notes/audit-2026-10-11'
def read(p): return p.read_text(encoding='utf-8-sig')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

previous = json.loads(read(AUDIT/'verification.json'))
paths = {ROOT/r['file'] for r in previous['docs']}
paths.update(HERE.glob('*.md'))
docs, broken, local_links = [], [], 0
for p in sorted(paths):
    t = read(p)
    outside = re.sub(r'^\s*```[^\n]*\n.*?^\s*```\s*$', '', t, flags=re.M|re.S)
    for match in re.finditer(r'\[[^\]\n]+\]\((<[^>\n]+>|[^)\n]+)\)', outside):
        target = match.group(1).strip('<>')
        if re.match(r'^(https?://|mailto:|app:|codex:|#)', target): continue
        target = unquote(target.split('#')[0])
        if not target: continue
        dest = Path(target) if Path(target).is_absolute() else p.parent/target
        local_links += 1
        if not dest.exists(): broken.append({'file':p.relative_to(ROOT).as_posix(),'target':target})
    docs.append({'file':p.relative_to(ROOT).as_posix(),'sha256':sha(p),
                 'fences_balanced':len(re.findall(r'^\s*```',t,re.M))%2==0,
                 'replacement_characters':t.count('\ufffd'),'lines':len(t.splitlines())})

manifest = json.loads(read(HERE/'sources/manifest.json'))
source_files = []
for row in manifest:
    for path_key, hash_key in [('file','sha256'),('text_file','text_sha256')]:
        p = HERE/'sources'/row[path_key]
        source_files.append({'id':row['id'],'file':row[path_key],
                             'ok':p.is_file() and sha(p)==row[hash_key]})
    assert row['read_scope'] and row['read_scope'] != 'pending', row['id']
    assert row['status']==200, row['id']

originals = []
for row in json.loads(read(AUDIT/'originals.json')) + json.loads(read(AUDIT/'additional-artifacts.json')):
    p=ROOT/row['file']
    originals.append({'file':row['file'],'unchanged':p.is_file() and sha(p)==row['sha256']})
design = next(x for x in previous['docs'] if x['file']=='notes/design-rener-vn-waterfall.md')
design_unchanged = sha(ROOT/design['file']) == design['sha256_after']

case_text=read(HERE/'BO-CA-PHAN-CHUNG-RENER.md')
case_ids=sorted(set(re.findall(r'\*\*C(\d{2})\s+—', case_text)))
assert case_ids == [f'{i:02d}' for i in range(1,27)], case_ids
toy=json.loads(read(HERE/'toy-metrics.json'))
assert abs(toy['A']['f1']-4/7)<1e-12 and abs(toy['B']['f1']-2/3)<1e-12
assert toy['C07_prefix']['unicode_code_points']==2 and toy['C07_prefix']['utf16_code_units']==3

source_urls={r['url'] for r in manifest}
report=read(HERE/'NGHIEN-CUU-SAU-VA-THAY-DOI-TU-DUY.md')
sources_linked=[r['id'] for r in manifest if r['url'] in report]
assert len(sources_linked)==21, sources_linked
bad_format=[r['file'] for r in docs if not r['fences_balanced'] or r['replacement_characters']]
bad_sources=[r for r in source_files if not r['ok']]
bad_originals=[r for r in originals if not r['unchanged']]
out={
    'verified_at_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Authored-document local file links, fences, UTF8 replacement characters; current 21 raw/text snapshots; protected originals and design compared with prior audit; synthetic arithmetic.',
    'documents':docs,'local_links_checked':local_links,'broken_local_links':broken,
    'sources_count':len(manifest),'source_hash_checks':source_files,
    'source_read_scopes_recorded':len(manifest),'source_urls_in_report':sources_linked,
    'protected_originals':originals,'design_v02_unchanged_since_prior_audit':design_unchanged,
    'case_ids':case_ids,'application_case_status':'ALL_26_NOT_RUN',
    'synthetic_arithmetic_checked':True,
    'limitations':['No app tests, NLP evaluation, user research or legal review.',
                   'No external URL recheck for the whole historical corpus.',
                   'No full reread of all old documents or every source section.',
                   'No render verification of historical Mermaid/PDF figures.',
                   'Hashes verify snapshot integrity, not source truth or interpretation.'],
}
failed=bool(broken or bad_format or bad_sources or bad_originals or not design_unchanged)
out['status']='FAIL' if failed else 'PASS_FOR_STATED_DOCUMENT_CHECKS'
(HERE/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'documents':len(docs),'local_links':local_links,
                 'broken':broken,'source_files_hashed':len(source_files),
                 'bad_sources':bad_sources,'protected_originals_unchanged':len(originals)-len(bad_originals),
                 'design_unchanged':design_unchanged,'format_failures':bad_format,
                 'cases':len(case_ids),'application_cases_run':0},ensure_ascii=True,indent=2))
sys.exit(1 if failed else 0)
