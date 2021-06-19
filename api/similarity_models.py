
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import nltk
import tensorflow_hub as hub
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import pickle


#model 1(tf_idf)
def tf_idf(document1, document2):
    vectorizer=TfidfVectorizer()
    document_appended=np.array((document1,document2))
    embeddings=vectorizer.fit_transform(document_appended)
    score=cosine_similarity(embeddings[0:1],embeddings[1:])
    return str(score[0][0])

#using BERT,here every sentence is compared against others
def BERT(document1,document2):
    model=SentenceTransformer('bert-base-nli-mean-tokens') 
      
    doc1_tokenized=re.compile('[.!?]').split(document1)[:-1]
    doc2_tokenized=re.compile('[.!?]').split(document2)[:-1]

    embedding1=np.array(model.encode(doc1_tokenized))
    embedding2=np.array(model.encode(doc2_tokenized))

    score=cosine_similarity(embedding1,embedding2)
    return str(np.mean(score))

#using Universal Sentence Encoder
def USE(document1,document2):
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model=hub.load(module_url)

    vec1=model([document1])
    vec2=model([document2])

    score=cosine_similarity(vec1,vec2)
    return str(score[0][0])

#jaccard similarity
def jaccard_similarity(document1,document2):
    lemmatizer=WordNetLemmatizer()
    def preprocess(text):
        text=re.sub('[^a-zA-Z]',' ',text)
        text=text.lower().split()
        text=[lemmatizer.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
        text=' '.join(text)
        return text

    doc1_tokenized=preprocess(document1)
    doc2_tokenized=preprocess(document2)

    union=set(doc1_tokenized+doc2_tokenized)

    intersection=set()

    for word in doc1_tokenized:
        if word in doc2_tokenized:
            intersection.add(word)

    score=len(intersection)/len(union)
    return score
