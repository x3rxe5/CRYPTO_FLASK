from flask import Flask,jsonify
from blockchain import Blockchain

# Initialize app
app = Flask(__name__)

# get BlockChain
blockchain = Blockchain()
