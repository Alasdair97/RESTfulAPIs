# Vet interface
from flask import request, jsonify, Flask
from PetObjects import AnimalList, PetOwners
import json

app = Flask(__name__)
app.config["DEBUG"] = True

JSONAnimalData = []
JSONOwnerData = []
JSONAllData = []

for Owner in PetOwners:
    JSONOwner = vars(Owner)
    JSONOwnerData.append(JSONOwner)
    JSONAllData.append(JSONOwner)

for Pets in AnimalList:
    JSONAnimal = vars(Pets)
    JSONAnimalData.append(JSONAnimal)
    JSONAllData.append(JSONAnimal)

JSONAnimals = json.loads(json.dumps(JSONAnimalData))
JSONOwner = json.loads(json.dumps(JSONOwnerData))
JSONAll = json.loads(json.dumps(JSONAllData))


@app.route('/', methods=[
    'GET'])  # which HTTP method we are using (GET) what route (extra bit of the URL) this method will be activated on.
def home():
    return (
        "<h1>Welcome to TSI Vets</h1><p>Internal System</p>"  # what the api returns
        "<p> Example GET requests </p>"
        "<p>Look up <a href='/api/data/all')>all data.</a> will fetch from extension /api/data/all</p>"
        "<p>Look up <a href='/api/vetpets/all')>all animals.</a> will fetch from extension /api/vetpets/all </p>"
        "<p>Look up <a href='/api/vetcustomers/all')>all owners.</a> will fetch from extension /api/vetcustomers/all </p>"
        "<p>Look up owners and corresponding pet(s): will fetch from extension /api/vetcustomers?id=[input] </p>"
        """
    <select onChange="window.location.href=this.value">
        <option value="/">-</option>
         <option value="/api/vetcustomers?id=0">0</option>
         <option value = "/api/vetcustomers?id=1">1</option>
         <option value = "/api/vetcustomers?id=2">2</option>
    </select>"""
        "<p>Look up PetID and corresponding owner: will fetch from extension /api/vetpets?petID=[input] </p>"
        """
    <select onChange="window.location.href=this.value">
        <option value="/">-</option>
         <option value="/api/vetpets?petID=0">0</option>
         <option value = "/api/vetpets?petID=1">1</option>
         <option value = "/api/vetpets?petID=2">2</option>
         <option value = "/api/vetpets?petID=3">3</option>
    </select>"""
    )


# A route to return all data entries.
@app.route('/api/data/all', methods=['GET'])
def api_all_data():
    return jsonify(JSONAll)


# A route to return all of the available entries in our collection of pets.
@app.route('/api/vetpets/all', methods=['GET'])
def api_all_pets():
    return jsonify(JSONAnimals)


# A route to return all of the available entries in our collection of owners.
@app.route('/api/vetcustomers/all', methods=['GET'])
def api_all_owners():
    return jsonify(JSONOwner)


@app.route('/api/vetpets', methods=['GET'])
def get_owner_by_pet_id():
    # Check if a petID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'petID' in request.args:
        id = int(request.args['petID'])
    else:
        return "Error: Invaild Search"

    # Create an empty list for our results
    petid_results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # Also matches all pets with same owner ID tag
    for Pet in JSONAnimals:
        if Pet['pet_id'] == id:
            petid_results.append(JSONOwner[Pet['owner_id']])
            petid_results.append(Pet)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(petid_results)


@app.route('/api/vetcustomers', methods=['GET'])
def get_owner_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Invaild Search."

    # Create an empty list for our results
    id_results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # Also matches all pets with same owner ID tag
    for Person in JSONOwner:
        if Person['id'] == id:
            id_results.append(Person)
    for Pet in JSONAnimals:
        if Pet['owner_id'] == id:
            id_results.append(Pet)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(id_results)


if __name__ == '__main__':
    app.run()
