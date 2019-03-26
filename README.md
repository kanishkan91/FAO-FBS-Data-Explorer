This visualization app explores agricultural production and losses across countries between 2010 and 2013. 
The visualization is presented as a collapsible bar chart that the user can click on to explore the sub-categories of loss and production.
The data used for this application is extracted from the FAO food balance sheets. 
The application has been deployed on heroku and can be accessed here-https://faoexplorer-flask-d3.herokuapp.com/. 

The back end and the data processing for this application is written in python flask and jinja. 
The front end in js has been created by adapting Mike Bostock's hierarchical bar chart example which can be found here- https://bl.ocks.org/mbostock/1283663
I have also made use of Andrew Heekins helpful code on converting a data frame into a nested json. 
The code for the same can be found here-https://github.com/andrewheekin/csv2flare.json/blob/master/csv2flare.json.py
 
