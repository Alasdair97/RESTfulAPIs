# Vet interface
import flask
from flask import request, jsonify
from PetObjects import AnimalList, PetOwners
import json
import ast

# DataFile = open('CustomerData.txt', 'r')
# CustomerData = dict(DataFile.read())
# DataFile.close()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

JSONAnimalData = []
JSONOwnerData = []

for Owner in PetOwners:
    JSONOwner = vars(Owner)
    JSONOwnerData.append(JSONOwner)

for Pets in AnimalList:
    JSONAnimal = vars(Pets)
    JSONAnimalData.append(JSONAnimal)

JSONAnimals = ast.literal_eval(json.dumps(JSONAnimalData))
JSONOwner = ast.literal_eval(json.dumps(JSONOwnerData))
# print(JSONDataDict)


@app.route('/', methods=['GET'])  # tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to TSI Vets</h1><p>Internal System</p>"  # what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return jsonify(JSONAnimals)


@app.route('/api/somearea/vetcustomers', methods=['GET'])
def get_owner_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: You are an idiot."

# Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for Person in JSONOwner:
        if Person['id'] == id:
            results.append(Person)
    for Pet in JSONAnimals:
        if Pet['owner_id'] == id:
            results.append(Pet)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
