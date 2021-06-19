import flask
from infersent import *
from similarity_models import *
from flask import Flask, flash, request,jsonify, json

app=Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict_similarity():
    #get the document strings
    json_data=request.get_json()
    document1=json_data['doc1']
    document2=json_data['doc2']
    name=json_data['modelName']
    #get the model name that has to be used
    score=eval(name+'(document1,document2)')
    #jsonify score
    return jsonify(
        similarity=score
    )

#predicting infersent predictions on a different route
@app.route('/predict_infersent',methods=['POST'])
def predict_infersent():
    json_data=request.get_json()
    document1=json_data['doc1']
    document2=json_data['doc2']
    score=Infersent(document1,document2)
    return jsonify(
        similarity=score
    )
    
if __name__=='__main__':
    app.debug=True
    app.run()
