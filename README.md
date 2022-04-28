# RESTfulAPIs
Creating a RESTful API for Python Using flask

In command line (or terminal you crazy mac users) type  

pip –version 

if pip has a version number then it is installed and added to the path.  (This should have been done when we installed python) 

If it is not a valid command then… 

Task 1 

 – install pip and add it to the path. 

 

What is PIP? 

Task 2 

Research PIP 

https://www.w3schools.com/python/python_pip.asp 

 

Connor is working on a project.  Lynn is working on the same project.  Even using imports how do we know that our set ups are running the same versions of the system and we have the same dependencies? 

 

Package managers!  From Maven (java) to NPM (JavaScript) package managers let us programmatically decide every library we want included in our project.  We can then share this across the team to include the same dependencies for everyone. 

 

Task 3 

Research APIs 

Particularly RESTful APIs and the HTTP commands available. 

Also look at JSON. 

Make a JSON object for a VETs system storing information about customers.   

RULES –  

A customer can have many pets but a pet must belong to a customer. 

This should be written as a document not using a program (So use word or notepad etc) 

 

Task 4 

Get the demo flaskAPI code from my github 

Run it from the command line (and leave the command line open) (OK OK and your bloody terminal) using; 

Python yourfilename.py 

This will set the API running on your local machine. 

Text

Description automatically generated 

The first time you run it you will probably see a message like so. 

Run 

Pip install flask 

Text

Description automatically generated 

PIP will handle the rest. 

Run the program again. 

Text

Description automatically generated 

Note the web address 127.0.0.1:5000 

You can now access this server via that address or as it is more commonly known  

Localhost:5000 

 

Check this is working on your machine. 

Task 5 

Next look at FlaskAPI2. 

In this file I added a return for all of a collection. 

Run it and navigate to the address bar and you should get the json file back. 

Graphical user interface, text

Description automatically generated 

Ok so now that hopefully this is making sense. 

Task 6 

FlaskAPI3 on github adds a method for finding a single record based on feeding a query parameter into the URL.  Once running it should look like the below. 

Graphical user interface, text, application, email

Description automatically generated 

 

Task 6 

Combine your new knowledge of flask to turn your vet program into an API for now only worry about getting information out using GET requests we will look at the others later.  Make the functionality as rich as possible and so your Json should be the JSON you designed earlier and have more opportunities for fun 😊 

 

Add methods to retrieve searches based on more than ID and look at error handling it when there are no results. 

Once you have completed these steps then here is the big one… 

 

Task 7 

Deploy your Vet program code to Azure and post the web address it is stored at.  Put this address in chat @ting me.  Fastest person to host a working and comprehensive program wins a £25 pound amazon gift card and eternal bragging rights. 

Extra tasks 

https://learning.postman.com/ 

Learn postman a great api testing tool we will need it to test any non GET requests 

Try to update a record in your dictionary  

Keep making this awesome! 