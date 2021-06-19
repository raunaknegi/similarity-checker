import numpy as np 
import nltk
from random import randint
import torch
from models import InferSent
from sklearn.metrics.pairwise import cosine_similarity

def Infersent(document1,document2):

    MODEL_PATH = "infersent1.pkl"
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0, 'version': 1}
    model = InferSent(params_model)
    model.load_state_dict(torch.load(MODEL_PATH))
    
    use_cuda = False
    model = model.cuda() if use_cuda else model
    W2V_PATH = 'glove/glove.6B.300d.txt'
    model.set_w2v_path(W2V_PATH)
    
    model.build_vocab_k_words(K=100000)
    
    sentences=[document1,document2]
    embeddings = model.encode(sentences, bsize=128, tokenize=False, verbose=True)
    score=cosine_similarity(embeddings[0].reshape(-1,1),embeddings[1].reshape(-1,1))
    return str(np.mean(score))

  