# Vet interface
import flask
from flask import request, jsonify
from VetAnimal import Dog

DataFile = open('CustomerData.txt', 'r')
CustomerData = DataFile.read()
DataFile.close()

print(CustomerData)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])  # tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to TSI Vets</h1><p>Internal System</p>" #what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return CustomerData


app.run()

