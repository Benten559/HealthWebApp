from flask import Flask, render_template, session, redirect, url_for, request
import sqlite3 as sql
import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
#from flask_ngrok import run_with_ngrok
X = pd.read_csv('datasets/training_data.csv')
symptoms = X.columns
symptoms = symptoms[:len(symptoms)-2]

app = Flask(__name__)
app.config['SECRET_KEY'] = '78sOME098random987key108475'
#run_with_ngrok(app)  # Start ngrok when app is run
# login or signup page
@app.route("/")
def index():
  return render_template('login_signup.html',methods=['POST'] )

# record a new user signup
@app.route("/index" , methods=['POST','GET'])
def signup():
  if request.method == "POST":
    usr = request.form["firstname"]
    email = request.form["mail"]
    key = request.form["pass"]
    path = "templates\db2.db"

    with sql.connect(path) as con:
      #check if email is already an entry within Database
      cur = con.cursor()
      cur.execute("select email from projects where email=?",(email,))
      check = cur.fetchall()
      print(check)
      if check:
        return render_template('logredirect.html')
      else:
        cur.execute("INSERT INTO projects (name,email,password) VALUES (?,?,?)" ,(usr,email,key) )            
        con.commit()

    return render_template('index.html',name = usr,email = email)

  else:
    return render_template('index.html')

@app.route("/log",methods=['POST'])
def login():
  if request.method == "POST":
    usr = request.form["name"]
    email = request.form["email"]
    key = request.form["pass"]
    path = "templates\db2.db"

    with sql.connect(path) as con:
      cur = con.cursor()
      cur.execute("select password from projects where email=?",(email,))           
      outs = cur.fetchall()
      if outs[0][0] == key:
        session["user"] = usr
        return render_template('homeaftersignin.html',name = usr)
      else:
        return 'Password Incorrect'
    #   return render_template('index.html',name = usr,email = email)

    # else:
    #   return render_template('index.html')

# Present the use with all the symptoms
@app.route("/diagnose")
def diagnose():
    return render_template('try.html',sympList=symptoms)

# The DTM computes based on user input
@app.route("/diagnosis", methods=['POST','GET'])
def diagnosis():
  userSymps = request.form.getlist('symps')
  # initialize empty DF
  inputDF = pd.DataFrame(0,index = np.arange(1),columns = symptoms)
  # mark user selections as 1
  for symp in userSymps:
    inputDF[symp] = inputDF[symp].replace(0,1)

  model = pickle.load(open('templates/model.pkl','rb'))
  result = model.predict(inputDF)
  print(result)
  return render_template('prognosis.html',results = result)


if __name__ == "__main__":
  app.run(debug=True)