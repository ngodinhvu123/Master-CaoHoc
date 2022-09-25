import pandas as pd
# https://realpython.com/python-keras-text-classification/
# Tập dữ liệu huấn luyện
filepath_dict = {'yelp':   './sentiment_analysis/yelp_labelled.txt',
                 'amazon': './sentiment_analysis/amazon_cells_labelled.txt',
                 'imdb':   './sentiment_analysis/imdb_labelled.txt'}

df_list = [] # 7-> 11 đọc dữ liệu
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
print(df.iloc[0]) #in ra dòng đầu tiên trong tập đầu tiên
sentences = ['John likes ice cream', 'John hates chocolate.']
from sklearn.feature_extraction.text import CountVectorizer

#Chuyển câu văn thành vector:
vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences)
print(vectorizer.vocabulary_)
# {'John': 0, 'chocolate': 1, 'cream': 2, 'hates': 3, 'ice': 4, 'likes': 5}

Mang = vectorizer.transform(sentences).toarray()
print('==Vector==')
# print(Mang)
print('==END Vector')

from sklearn.model_selection import train_test_split
#xử lý tập dữ liệu yelp
df_yelp = df[df['source'] == 'yelp']

sentences = df_yelp['sentence'].values # Đọc câu bình luận
y = df_yelp['label'].values # nhãn có thể là 0 hoặc 1 (positive or negvite)
sentences_train, sentences_test, y_train, y_test = train_test_split(
       sentences, y, test_size=0.25, random_state=1000) # tách dữ liệu thành tập huấn luyện và tập kiểm tra
from sklearn.feature_extraction.text import CountVectorizer

#biến cấu sentences thành vector
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
print("sentences_test",sentences_test)
print("--X_train---")
# print(X_train)

## Huấn luyện bằng giải thuật LogisticRegression
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
# Kiểm tra mô hình sau khi huấn luyện xong
print("Testing")
score = classifier.score(X_test, y_test)
print("Accuracy:", score)
print("===== Thầy phúc kiểm tra 3 câu từ ngoài vào =====")
sentences = ['John likes ice cream', 'John hates chocolate.',"Tu loves his university."]
X_test  = vectorizer.transform(sentences) # Chuyển câu kiểm tra thành vector
ab=classifier.predict(X_test) # Kết quả kiểm tra
print(sentences) # In ra câu cần kiểm tra
print(ab) # In ra kết quả cần kiểm tra
