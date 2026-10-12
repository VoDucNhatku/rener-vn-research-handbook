"""Portable, read-only checks. Outputs optional report to an ignored local file."""
from pathlib import Path
from urllib.parse import unquote
import argparse, hashlib, json, re, sys

ROOT=Path(__file__).resolve().parent.parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def text_hash(p): return hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest()

def validate(root=ROOT):
    errors=[]; warnings=[]; links=0; docs=0; forensic=0
    patterns={
        'github_token':r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})',
        'private_key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        'provider_key':r'\bsk-(?:proj-)?[A-Za-z0-9_-]{25,}',
        'aws_access_key':r'\bAKIA[A-Z0-9]{16}\b',
        'bearer_literal':r'(?i)bearer\s+[A-Za-z0-9_=-]{25,}',
        'credential_url':r'\w+://[^\s/:]+:[^\s/@]+@',
    }
    text_types={'.md','.py','.json','.txt','.html','.yml','.yaml','.ts','.ps1','.cjs','.diff'}
    files=[p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
    for p in files:
        rel=p.relative_to(root).as_posix()
        if p.name.startswith('.env') or p.suffix in {'.pem','.key','.p12','.pfx','.db','.sqlite','.sqlite3'}:
            errors.append({'file':rel,'type':'forbidden_sensitive_filename'})
        if p.stat().st_size>50*1024*1024: errors.append({'file':rel,'type':'oversized_file'})
        if p.suffix not in text_types: continue
        try: t=p.read_text(encoding='utf-8-sig')
        except UnicodeError:
            errors.append({'file':rel,'type':'not_utf8'}); continue
        if '\ufffd' in t: errors.append({'file':rel,'type':'replacement_character'})
        for kind,pattern in patterns.items():
            for m in re.finditer(pattern,t):
                errors.append({'file':rel,'type':kind,'line':t.count('\n',0,m.start())+1})
        if p.suffix!='.md': continue
        docs+=1
        if len(re.findall(r'^\s*```',t,re.M))%2: errors.append({'file':rel,'type':'unbalanced_fences'})
        if 'before' in p.parts:
            forensic+=1; continue
        outside=re.sub(r'^\s*```[^\n]*\n.*?^\s*```\s*$','',t,flags=re.M|re.S)
        for m in re.finditer(r'\[[^\]\n]+\]\((<[^>\n]+>|[^)\n]+)\)',outside):
            target=m.group(1).strip('<>')
            if re.match(r'^(https?://|mailto:|app:|codex:|#)',target): continue
            name=unquote(target.split('#')[0])
            if not name: continue
            links+=1
            dest=(p.parent/name).resolve()
            if not dest.is_relative_to(root.resolve()): errors.append({'file':rel,'type':'outside_repo_link','target':target})
            elif not dest.exists(): errors.append({'file':rel,'type':'broken_local_link','target':target})
    manifest=json.loads((root/'evidence/import-manifest.json').read_text(encoding='utf-8-sig'))
    checked=0
    for row in manifest['files']:
        p=root/row['path']; checked+=1
        if not p.is_file(): errors.append({'file':row['path'],'type':'missing_import'}); continue
        expected=row.get('export_lf_sha256')
        ok=text_hash(p)==expected if expected else digest(p)==row['export_sha256']
        if not ok: warnings.append({'file':row['path'],'type':'changed_since_initial_import'})
    # Original proposal binaries are a preserved input, unlike evolving authored documents.
    originals=json.loads((root/'notes/audit-2026-10-11/originals.json').read_text(encoding='utf-8-sig'))
    for row in originals:
        p=root/row['file']
        if not p.is_file() or digest(p)!=row['sha256']: errors.append({'file':row['file'],'type':'original_proposal_changed'})
    cases=(root/'notes/nghien-cuu-sau-2026-10-11/BO-CA-PHAN-CHUNG-RENER.md').read_text(encoding='utf-8-sig')
    ids=set(re.findall(r'\*\*C(\d{2})\s+—',cases))
    if ids!={f'{i:02d}' for i in range(1,27)}: errors.append({'type':'case_catalog_incomplete'})
    if 'NOT RUN' not in cases: errors.append({'type':'case_status_missing'})
    return {'status':'FAIL' if errors else 'PASS_DOCUMENT_CHECKS','markdown_documents':docs,
            'local_links_checked':links,'historical_before_docs_skipped_for_links':forensic,
            'imported_files_checked':checked,'protected_proposal_files':len(originals),
            'errors':errors,'warnings':warnings,
            'limits':['No external URL, anchor, Markdown render or diagram check.',
                      'Secret regex checks are not a complete security audit; binary content is not scanned.',
                      'No ReNER app/NLP/extension/load/user test.',
                      'Historical source snapshot hashes are not reverified because raw sources are not redistributed.']}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--report',action='store_true'); args=ap.parse_args()
    result=validate()
    if args.report: (ROOT/'validation-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=True,indent=2))
    return 1 if result['errors'] else 0

if __name__=='__main__': sys.exit(main())
