# Vet interface
import flask
import json
from flask import request, jsonify
from VetAnimal import Dog

Pet1 = Dog('Tom', 'Steve')

JsonObjectString = json.dumps(Pet1.__dict__)

print(JsonObjectString) # Test for JSON

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])  # tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to TSI Vets</h1><p>Internal System</p>" #what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return jsonify(JsonObjectString)

