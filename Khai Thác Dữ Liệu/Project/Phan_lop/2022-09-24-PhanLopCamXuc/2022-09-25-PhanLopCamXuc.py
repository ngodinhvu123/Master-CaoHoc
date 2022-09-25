import pandas as pd
# https://realpython.com/python-keras-text-classification/
# Tap du lieu huan luyen.Co 3 du lieu huan luyen de phan tich cam xuc
filepath_dict = {'yelp':   'sentiment_analysis/yelp_labelled.txt',
                 'amazon': 'sentiment_analysis/amazon_cells_labelled.txt',
                 'imdb':   'sentiment_analysis/imdb_labelled.txt'}

df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t') ## doc file câu va nhãn
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
from sklearn.model_selection import train_test_split
# Xu ly tap du lieu yelp:User Reviews and Recommendations of Best Restaurants, Shopping, Nightlife, Food, Entertainment
df_yelp = df[df['source'] == 'yelp']
sentences = df_yelp['sentence'].values## doc sentence binh luan
y = df_yelp['label'].values## nhan nay co the la 0(negative) hoac 1 (positive)
sentences_train, sentences_test, y_train, y_test = train_test_split(
       sentences, y, test_size=0.25, random_state=1000) ## tach du lieu thu duoc thanh tap huan luyen va tap kiem tra
from sklearn.feature_extraction.text import CountVectorizer
## bien cau van thanh vector
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)
X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
## Huan luyen bang giai thuat phan lop LogisticRegression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
## Kiem tra mo hinh sau khi  huan luyen xong
print("Testing")
score = classifier.score(X_test, y_test)
print("Accuracy:", score)
print("===== Thay Phuc kiem tra mot vai cau go tu ngoai vao ====")
sentences = ['John likes ice cream', 'John hates chocolate.',"Tu loves his university."]
X_test  = vectorizer.transform(sentences) ## Chuyen cau kiem tra thanh vector
ab=classifier.predict(X_test)## ket qua kiem tra
print(sentences)## In ra cau can kiem tra
print(ab)### In ra ket qua kiem tra