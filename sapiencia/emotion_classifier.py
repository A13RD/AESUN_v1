# from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, DataCollatorWithPadding
# from datasets import load_dataset
# import torch
#
# dataset = load_dataset("emotion")
#
#
# def map_emotion_to_sentiment(example):
#     emotion = example["label"]
#     if emotion in [0, 4, 5]:  # joy, love, surprise
#         return {"label": 1}   # Positivo
#     else:
#         return {"label": 0}   # Negativo
#
#
# dataset = dataset.map(map_emotion_to_sentiment)
#
#
# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
#
#
# def tokenize(batch):
#     return tokenizer(batch['text'], padding=True, truncation=True, max_length=128)
#
#
# tokenized_datasets = dataset.map(tokenize, batched=True)
#
#
# tokenized_datasets.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])
#
#
# train_dataset = tokenized_datasets['train']
# test_dataset = tokenized_datasets['test']
#
#
# model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
#
#
# data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
#
# training_args = TrainingArguments(
#     output_dir="./results",
#     num_train_epochs=3,
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=16,
#     evaluation_strategy="epoch",
#     logging_dir="./logs",
#     logging_steps=100,
# )
#
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     data_collator=data_collator,
#     train_dataset=train_dataset,
#     eval_dataset=test_dataset,
# )
#
# trainer.train()
#
# results = trainer.evaluate()
#
# print(f"Resultados de la evaluación: {results}")
#
# model.save_pretrained("./Training_model")
# tokenizer.save_pretrained("./Training_model")
#
#
# def predict_emotion(text):
#     inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
#     with torch.no_grad():
#         logits = model(**inputs).logits
#     prediction = torch.argmax(logits, dim=-1).item()
#     return "Positivo" if prediction == 1 else "Negativo"
#
#
# test_text = "I feel really happy today!"
# print(f"El sentimiento del texto es: {predict_emotion(test_text)}")
