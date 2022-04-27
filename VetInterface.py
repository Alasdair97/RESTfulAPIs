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
    {'Owner_id': 0,
     'Owner_name': 'Alasdair'},
    {'Owner_id': 1,
     'Owner_name': 'Ahmed'},
    {'Owner_id': 2,
     'Owner_name': 'Gareth'}
]

CustomerData = AnimalList
JSONData = []

for Things in AnimalList:
    print(Things)
    print(Things.PetName)
    JSONAnimal = vars(Things)
    JSONData.append(JSONAnimal)

JSONDataDict = str(JSONData)
print(JSONDataDict)



@app.route('/', methods=['GET'])  # tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to TSI Vets</h1><p>Internal System</p>"  # what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return JSONDataDict

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

