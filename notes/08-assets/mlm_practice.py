import random, torch
from transformers import BertForMaskedLM, BertTokenizer, pipeline

random.seed(42); torch.manual_seed(42)
name = "bert-base-uncased"
tok = BertTokenizer.from_pretrained(name)
model = BertForMaskedLM.from_pretrained(name).eval()

# Demo 1: fill-mask uses context on BOTH sides
fill = pipeline("fill-mask", model=model, tokenizer=tok)
for s in ["The capital of France is [MASK].",
          "I went to the [MASK] to deposit my money.",
          "I sat on the [MASK] of the river and watched the water."]:
    top = fill(s, top_k=3)
    print(s, "->", [(t["token_str"], round(t["score"], 3)) for t in top])

# Task 2 of the practice slide: random masking + accuracy
sentence = ("Natural language processing lets computers understand human language, "
            "and masked language models learn by predicting hidden words from their context.")
enc = tok(sentence, return_tensors="pt")
ids = enc["input_ids"][0].clone()
special = set(tok.all_special_ids)
cand = [i for i, t in enumerate(ids.tolist()) if t not in special]

def mask_tokens(ids, rate=0.15):
    k = max(1, round(rate * len(cand)))
    pos = sorted(random.sample(cand, k))
    masked = ids.clone(); masked[pos] = tok.mask_token_id
    return masked, pos

total, correct = 0, 0
for trial in range(20):
    masked, pos = mask_tokens(ids)
    with torch.no_grad():
        logits = model(input_ids=masked.unsqueeze(0)).logits[0]
    pred = logits[pos].argmax(-1)
    total += len(pos); correct += (pred == ids[pos]).sum().item()
    if trial < 2:
        print("masked :", tok.decode(masked, skip_special_tokens=False))
        print("orig vs pred:", list(zip(tok.convert_ids_to_tokens(ids[pos]), tok.convert_ids_to_tokens(pred))))
print(f"non-special tokens: {len(cand)}, masked per trial: {max(1, round(0.15*len(cand)))}")
print(f"accuracy over 20 trials: {correct}/{total} = {correct/total:.3f}")
