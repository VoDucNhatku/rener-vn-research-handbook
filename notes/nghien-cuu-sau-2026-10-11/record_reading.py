"""Record selected reading scope and check educational arithmetic, not application tests."""
from pathlib import Path
from datetime import datetime, timezone
import json

HERE = Path(__file__).resolve().parent
scopes = {
    'S01': 'Main guidance: user needs, research evidence, needs vs user stories.',
    'S02': 'Short main page: story, rules, examples, questions and timebox.',
    'S03': 'Selected passages: 1.1, 3.1-3.2, beginning of 3.3, 3.4-3.5, 3.7; not full paper/appendices.',
    'S04': 'Introduction and selected 3.2 construct validity passages, especially content and consequential validity.',
    'S05': 'Method introduction, Figure 1 textual discussion and MFT/INV/DIR definitions; not full experiments.',
    'S06': 'Section 2 metric discussion; section 3 McNemar, sampling/bootstrap/randomization and selection guidance.',
    'S07': 'Reread 2.1 noise, section 3 collection/annotation, 4.6 errors, 4.7 NER contribution and Table 4 context.',
    'S08': 'Privacy tradeoff before section 5; 5.1 curation, language variety, speaker/annotator and start of speech situation.',
    'S09': 'Atomic recording/request identity; late requests/identifier lifespan; same ID different intent.',
    'S10': 'Timeouts, layered retries, backoff and jitter sections.',
    'S11': 'Read Committed and Repeatable Read; selected Serializable and transaction retry paragraphs, version 18.',
    'S12': 'Locking clause SKIP LOCKED and LIMIT/ORDER BY, not full SELECT reference, version 18.',
    'S13': 'Idle/shutdown, persisted state and browser-version lifetime notes.',
    'S14': 'Security considerations/safe handling; async responses compatibility passage.',
    'S15': 'Storage areas including session/local and access-level notes.',
    'S16': 'Indirect injection, agent controls/least privilege, model guardrails, intended-outcome grading and reporting limits.',
    'S17': 'Deny by default, every-request permission validation, framework configuration limitations.',
    'S18': 'SLI specification vs implementation, indicator categories, critical user journeys; not whole workbook.',
    'S19': 'SC 4.1.3, intent and status/search result examples.',
    'S20': 'Eval definitions, grader types, capability/regression, pass@k/pass^k, roadmap 1-3 and 6-7, complementary evaluation methods.',
    'S21': 'Failure modes, frontend rubric, agent roles/sprint contract, model-dependent simplification, results limits and lessons; not full appendix.',
}
manifest_path = HERE/'sources/manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
assert {r['id'] for r in manifest} == set(scopes)
for row in manifest:
    row['read_scope'] = scopes[row['id']]
    row['review_date_local'] = '2026-10-12'
    row['reading_status'] = 'selected_content_read_not_full_source_certification'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def metrics(correct, wrong, abstain):
    gold = correct + wrong + abstain
    predicted = correct + wrong
    precision = correct / predicted if predicted else None
    recall = correct / gold if gold else None
    return dict(gold=gold, correct=correct, wrong=wrong, abstain=abstain,
                tp=correct, fp=wrong, fn=wrong+abstain,
                precision=precision, recall=recall,
                f1=2*correct/(2*correct+wrong+wrong+abstain),
                coverage=predicted/gold,
                observed_error_among_answers=wrong/predicted if predicted else None)

a, b = metrics(4,0,6), metrics(6,2,2)
assert abs(a['f1']-4/7)<1e-12 and abs(b['f1']-2/3)<1e-12
prefix='🏠 '
out = {
    'computed_at_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'EDUCATIONAL_ARITHMETIC_ONLY_NOT_A_MODEL_OR_APP_TEST',
    'assumption': '10 synthetic cases; one gold numeric value each. Wrong value is both FP and a missed gold FN.',
    'A': a, 'B': b,
    'C10_duplicate_record_example': {'tp':2, 'fp':1, 'fn':0, 'precision':2/3, 'recall':1, 'f1':4/5},
    'C07_prefix': {'text':prefix, 'unicode_code_points':len(prefix), 'utf16_code_units':len(prefix.encode('utf-16-le'))//2},
    'C17_nested_attempt_upper_bound':3*3,
    'limitations': ['All counts are invented teaching examples.', 'No extractor, API, extension or dataset was executed.', '26 proposed cases remain NOT RUN.'],
}
assert out['C07_prefix']['unicode_code_points']==2 and out['C07_prefix']['utf16_code_units']==3
(HERE/'toy-metrics.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_read_scopes_recorded':len(manifest),'synthetic_A_f1':a['f1'],'synthetic_B_f1':b['f1'],'application_tests_run':False}))
