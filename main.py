import random


meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık verilen bir cevap",
    "SHEESH": "Onaylamamak veya şaşırmak",
    "CREEPY": "Korkunç veya ürkütücü bir şey",
    "AGGRO": "Sinirlenmek veya agresifleşmek"
}


print("Anlamını öğrenmek istediğiniz bir kısaltma girin.")


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict:
    print(word + ": " + meme_dict[word])
else:
    print("Üzgünüm, bu kelimenin anlamı sözlükte yok. Bir dahaki sefere başka bir kelime deneyin!")
