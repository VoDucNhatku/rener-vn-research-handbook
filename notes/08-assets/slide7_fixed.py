import torch
from torch.optim import AdamW  # fix: transformers.AdamW was removed
from transformers import BertForSequenceClassification, BertTokenizer
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(0)
model_name = "bert-base-uncased"
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = BertTokenizer.from_pretrained(model_name)
print("params:", sum(p.numel() for p in model.parameters()))
print("layers:", model.config.num_hidden_layers, "hidden:", model.config.hidden_size,
      "heads:", model.config.num_attention_heads, "vocab:", model.config.vocab_size)

texts = ["This movie was great!", "I didn't like the book."]
labels = [1, 0]
enc = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=128)
print("tokens[0]:", tokenizer.convert_ids_to_tokens(enc["input_ids"][0]))
dataset = TensorDataset(enc["input_ids"], enc["attention_mask"], torch.tensor(labels))
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
optimizer = AdamW(model.parameters(), lr=2e-5)

model.train()
for epoch in range(3):
    for ids, mask, y in dataloader:
        optimizer.zero_grad()
        out = model(ids, attention_mask=mask, labels=y)
        out.loss.backward()
        optimizer.step()
    print(f"epoch {epoch} loss {out.loss.item():.4f}")
print("Fine-tuning completed!")
