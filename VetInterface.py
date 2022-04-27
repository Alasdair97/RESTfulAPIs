# Vet interface
import flask
from flask import request, jsonify
from PetObjects import AnimalList

# DataFile = open('CustomerData.txt', 'r')
# CustomerData = dict(DataFile.read())
# DataFile.close()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

PetOwners = [
    {'id': 0,
     'name': 'Alasdair'},
    {'id': 1,
     'name': 'Ahmed'},
    {'id': 2,
     'name': 'Gareth'}
]

CustomerData = AnimalList
JSONData = []

for Things in AnimalList:
    JSONAnimal = vars(Things)
    JSONData.append(JSONAnimal)

print(JSONData)



@app.route('/', methods=['GET'])  # tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to TSI Vets</h1><p>Internal System</p>"  # what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return JSONData

# app.route('/api/somearea/vetcustomers', methods=['GET'])
# def get_owner_by_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: You are an idiot."


app.run()

