from underthesea import word_tokenize
sentenceList=["Tôi yêu em nhiều lăm.","Tôi yêu Long Khánh,","Tôi không thích rượu bia."]
print("Cac tu tieng Viet")
TuVungList=[]
for sentence in sentenceList:
    print(sentence)
    print(word_tokenize(sentence))
    for word in word_tokenize(sentence):
        if not word in TuVungList:
            TuVungList.append(word)
#Tao vocabulary bo tu vung
print("Tu vung")
print(TuVungList)
## Tao vector
for sentence in  sentenceList:
    MangViet=word_tokenize(sentence)
    MangCau=[]
    for wordtv in TuVungList:
        if wordtv in MangViet:
            MangCau.append(1)
        else:
            MangCau.append(0)
    print(sentence)
    print(MangCau)