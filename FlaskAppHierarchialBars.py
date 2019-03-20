from flask import Flask, flash, redirect, render_template, request, session, abort,send_from_directory,send_file,jsonify
import pandas as pd
import numpy as np
import json
import xlrd
#from json import jsonify
import DataUpdate
from sklearn.feature_extraction.text import TfidfVectorizer
import dask.dataframe as dd
import pip




app= Flask(__name__)

@app.route("/main",methods=["GET","POST"])

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-data",methods=["GET","POST"])
def homepage():
   df=pd.read_excel(r'C:\Users\Public\Pythonfiles\Crops.xlsx')
# choose columns to keep, in the desired nested json hierarchical order
   df = df[["Category", "Cat", "value"]]


# order in the groupby here matters, it determines the json nesting
# the groupby call makes a pandas series by grouping 'the_parent' and 'the_child', while summing the numerical column 'child_size'
   df1 = df.groupby(['Category', 'Cat'])['value'].sum()
   df1 = df1.reset_index()


# start a new flare.json document
   flare = dict()
   d = {"name":"flare", "children": []}


   for line in df1.values:
      Category = line[0]
      Cat = line[1]
      value = line[2]

    # make a list of keys
      keys_list = []
      for item in d['children']:
        keys_list.append(item['name'])

    # if 'the_parent' is NOT a key in the flare.json yet, append it
      if not Category in keys_list:
        d['children'].append({"name":Category, "children":[{"name":Cat, "size":value}]})

    # if 'the_parent' IS a key in the flare.json, add a new child to it
      else:
        d['children'][keys_list.index(Category)]['children'].append({"name":Cat, "size":value})

   flare = d
   e= json.dumps(flare)
   f= json.loads(e)
   print(f)
   return jsonify(f)
# export the final result to a json file

if __name__ == "__main__":
    app.run(debug=True)



