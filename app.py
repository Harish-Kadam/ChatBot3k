from flask import Flask,render_template
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import nltk
import numpy as np
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
warnings.filterwarnings("ignore")


bot = ChatBot("Candice")
trainer=ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


app=Flask(__name__,template_folder='./template')
@app.route("/")
def index():
    return render_template("index.html")


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


@app.route("/get")
def response():
    userText = request.args.get('msg')
    greeting(userText)
  
    if(userText==""):
        return "Hi! I'm Harry your personal ChatBot"


    else:
        return str(bot.get_response(userText))



if __name__ == "__main__":
    app.run()
