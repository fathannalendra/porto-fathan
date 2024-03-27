from http import client
from flask import Flask,redirect,url_for, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://fathannalendra:nalendra1@cluster0.zewp6nd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)