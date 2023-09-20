from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import torch
from texttoSpeech import texttoSpeech
from speechtoText import speechtoText
 # LOAD MODEL
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-squad")
model = AutoModelForQuestionAnswering.from_pretrained("savasy/bert-base-turkish-squad")
qa=pipeline("question-answering", model=model, tokenizer=tokenizer)

ostim="1967 yılında küçük sanayi sitesi yapı kooperatifi olarak 1.748 üye ile faaliyete başlayan \
OSTİM; bugün 17 ana sektör ve 139 iş kolunda faaliyet gösteren 6.200 işletme ve 60.000 \
çalışanı ile Ankara ve Türkiye sanayisinde önemli ve öncü bir rol oynayan organize sanayi bölgesidir.\
OSTİM ekosistemi özgün ve örnek bir sanayi bölgesi yönetim modelidir. Demiral akbar ostimde çalışıyor, profesördür, kral hocadır. \
Murat ŞİMŞEK Ostim teknik üniversitesinde yapay zeka mühendisliği bölüm başkanıdır ayrıca dekan yardımcısıdır. Bu proejedeki NLP üzerine çalışmaktadır\
Bu ekosistem içinde faaliyet gösteren işletme ve çalışanların yaşam boyu eğitimine ve mesleki eğitimine özel önem verilmektedir. \
İşletmelerin teknoloji geliştirme, tanıtım, pazarlama, teknoloji transferi,\
 insan kaynakları ve istihdam gibi ihtiyaçlarına yönelik bütüncül ve sürdürülebilir hizmetler sağlanmaktadır."


os_question=speechtoText()

cevap = qa(question=os_question, context=ostim)["answer"]
print(cevap)
texttoSpeech(cevap)


