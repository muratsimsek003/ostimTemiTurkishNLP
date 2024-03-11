from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import torch
from texttoSpeech import texttoSpeech
from speechtoText import speechtoText
import time


# LOAD MODEL
tokenizer = AutoTokenizer.from_pretrained("muratsimsek003/turkish_bert_qa")
model = AutoModelForQuestionAnswering.from_pretrained("muratsimsek003/turkish_bert_qa")
qa=pipeline("question-answering", model=model, tokenizer=tokenizer)

with open('ostim.txt', encoding='utf-8') as dosya:
    ostim = dosya.read()


os_question=speechtoText()

cevap = qa(question=os_question, context=ostim)["answer"]
print(cevap)
texttoSpeech(cevap)
