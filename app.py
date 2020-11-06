from flask import Flask, render_template, g, redirect, url_for, request
import sqlite3 as sql
import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier

X = pd.read_csv('datasets/training_data.csv')
symptoms = X.columns
symptoms = symptoms[:len(symptoms)-2]

app = Flask(__name__)
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
      cur = con.cursor()
      cur.execute("INSERT INTO projects (name,email,password) VALUES (?,?,?)" ,(usr,email,key) )            
      con.commit()

    return render_template('index.html',name = usr,email = email)

  else:
    return render_template('index.html')

@app.route('/list',methods=['POST','GET'])
def list():
  path = "templates\db2.db"
  con = sql.connect(path)
  con.row_factory = sql.Row
  
  cur = con.cursor()
  cur.execute("select * from projects")
   
  rows = cur.fetchall()
  return render_template("list.html",rows = rows)

@app.route("/diagnose")
def diagnose():
    return render_template('try.html',sympList=symptoms)

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
  return 'results in terminal output for now'


if __name__ == "__main__":
  app.run()