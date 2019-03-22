from flask import Flask, flash, redirect, render_template, request, session, abort,send_from_directory,send_file,jsonify
import pandas as pd

import json





app= Flask(__name__)

class DataStore():
    CountryName=None
    Year=None
data=DataStore()


@app.route("/main",methods=["GET","POST"])

@app.route("/",methods=["GET","POST"])
def homepage():
    CountryName = request.form.get('Country_field','India')
    print(CountryName)
    Year = request.form.get('Year_field', 2013)
    data.CountryName=CountryName
    data.Year=Year

    return render_template("index.html",CountryName=CountryName,Year=Year)


@app.route("/get-data",methods=["GET","POST"])
def returnProdData():
   df=pd.read_excel(r'C:\Users\Public\Pythonfiles\CropsFull.xlsx')
   CountryName = data.CountryName
   print(CountryName)
   Year = data.Year
   print(Year)

# choose columns to keep, in the desired nested json hierarchical order
   df=df[df.Country==CountryName]
   df=df[df.Year== int(Year)]
   print(df.head())
   #df = df.drop(
       #['Country', 'Item Code', 'Flag', 'Unit', 'Year Code', 'Element', 'Element Code', 'Code', 'Item'], axis=1)
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

@app.route("/get-loss-data",methods=["GET","POST"])
def returnLossData():
   df=pd.read_excel(r'C:\Users\Public\Pythonfiles\Losses.xlsx')
   CountryName = data.CountryName
   print(CountryName)
   Year = data.Year
   print(Year)

# choose columns to keep, in the desired nested json hierarchical order
   df=df[df.Country==CountryName]
   df=df[df.Year== int(Year)]
   print(df.head())
   #df = df.drop(
       #['Country', 'Item Code', 'Flag', 'Unit', 'Year Code', 'Element', 'Element Code', 'Code', 'Item'], axis=1)
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
   g= json.loads(e)
   print(g)
   return jsonify(g)


if __name__ == "__main__":
    app.run(debug=True)



