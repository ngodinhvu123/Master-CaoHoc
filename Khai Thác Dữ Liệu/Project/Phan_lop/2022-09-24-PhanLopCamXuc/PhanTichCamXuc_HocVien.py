OpnionList=["I love you so much.","I like Long Khanh","I dislike alcohol."]
SentLabel=[1,1,0]
### Hay doi 3 cau nay thanh vector
sentences =OpnionList
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences)
print("-- Danh sach tu vung--")
print(vectorizer.vocabulary_)
## Chuyen cac cau sang vector
Mang= vectorizer.transform(sentences).toarray()
print("In  Mang ket qua chuyen sang vector cua 3 cau ")
# print(Mang)
### Tao file chua du lieu huan luyen

filename= "dulieuhuanluyen.csv"
fwrite=open(filename,"w")
fwrite.write("love,you,so,much,like,long,khanh,dislike,alcohol,class")
fwrite.write("\n")
for i in range(0,3):
    row=Mang[i]
    chuoi=str(Mang[i][0])
    for j in range(1,len(row)):
        chuoi+=","+str(Mang[i][j])
    chuoi+=","+str(SentLabel[i])
    print(chuoi)
    fwrite.write(chuoi)
    fwrite.write("\n")
fwrite.close()