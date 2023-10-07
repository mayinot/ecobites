from flask import Flask
from flask_pymongo import PyMongo
from pymongo import cursor
from pymongo.message import query
from Credentials import constants
import pymongo


app = Flask(__name__)

# connecting to mongo
app.config["MONGO_URI"] = constants.MONGO_CONNECT
mongo = PyMongo(app)
# getting the db and disable the SSL certificate for UNIX developers
mongo.init_app(app, tlsAllowInvalidCertificates=True)


if __name__ == "__main__":
    # test data access function here 
    pass