from flask import Flask, request, jsonify, render_template,json,Response
import os
import openai
import requests

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
API_TOKEN = os.environ.get('HF_API_TOKEN')
Api_url ="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
Headers = {"Authorization": {{API_TOKEN}}}

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABSE_URI'] ="sqlite://user.db"
#db = SQLAlchemy(app)

#class user(db.Model):
 #   student_Id = db.Column(db.Integer,primary_key=True)
  #  username = db.Column(db.String(200),nullable=False)
   # password = db.Column(db.String(200), nullable=False)
    #level_of_blindness = db.Column(db.String(200), nullable=False)

#class chapters(db.Model):
 #   sno = db.Column(db.Integer,primary_key=True)
  #  chapter_name = db.Column(db.String,nullable=False)

#class status(db.Model):
 #   student_Id = db.Column(db.Integer)
  #  chapters = db.Column(db.String, db.ForeignKey('users.user_Id'),nullable = False)
   # status = db.Column(db.String, nullable = False)

#home
@app.route("/")
def home():
    return render_template("home.html")

HF_API_TOKEN = API_TOKEN
HF_MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
#
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question', '')
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    prompt = f"You're a friendly maths tutor helping a blind student learn statistics. Explain in clear, simple language. Question: {user_question}"

    try:
         response = requests.post(
             HF_MODEL_URL,
             headers=headers,
             json={"inputs": prompt}
         )

         if response.status_code != 200:
             return jsonify({"error": f"Hugging Face API Error: {response.text}"}), response.status_code

         generated_text = response.json()[0]['generated_text']
         # Optional: strip out the prompt part if included in the response
         answer = generated_text.split("Question:")[-1].strip()
         return jsonify({"answer": answer})

    except Exception as e:
         return jsonify({"error": str(e)}), 500
    
    

#print(Response.text)
#login
@app.route("/login")
def login():
        return render_template("login.html")
#signup
@app.route("/signup")
def signup():
    return render_template("signup.html")

#about
@app.route("/about")
def about():
    return render_template("about.html")

#how-it-works
@app.route("/how-it-work")
def how_it_work():
    return render_template("how-it-work.html")

#index
@app.route("/index")
def index():
    return render_template("index.html")

#classroom
@app.route("/classroom")
def classroom():
    return render_template("classroom.html")

#progress
@app.route("/progress")
def progress():
    return render_template("progress.html")

#community
@app.route("/community")
def  community():
    return render_template("community.html")

#test
@app.route("/test")
def test():
    return render_template("test.html")

#profile
@app.route("/profile")
def profile():
    return render_template("profile.html")




if __name__ == "__main__":
    app.run(debug=True)