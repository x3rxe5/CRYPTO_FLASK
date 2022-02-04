from flask import Flask,jsonify
from blockchain import Blockchain

# Initialize app
app = Flask(__name__)

# get BlockChain
blockchain = Blockchain()

@app.route("/",methods=['GET'])
def index():
  response = {
    "message":"Please visit /mine_block , /valid , /get_chain"
  }
  return jsonify(response),200

# For mining the block
@app.route("/mine_block",methods=['GET'])
def mine_block():
  previous_block = blockchain.print_previous_block()
  previous_proof = previous_block['proof']
  proof = blockchain.proof_of_work(previous_proof)
  previous_hash = blockchain.hash(previous_block)
  block = blockchain.create_block(proof,previous_hash)

  response = {
    "message":"A block has mined",
    "index":block["index"],
    "timestamp":block["timestamp"],
    "proof":block["proof"],
    "previous_hash":block["previous_hash"]
  }

  return jsonify(response),200

# for getting current chain
@app.route("/get_chain",methods=['GET'])
def display_chain():
  response = {
    "chain":blockchain.chain,
    "length":len(blockchain.chain)
  }

  return jsonify(response),200


# For Valid Transaction
@app.route("/valid",methods=['GET'])
def valid():
  valid = blockchain.chain_valid(blockchain.chain)
  message = ""
  if valid:
    message = "No Error in the chain"
  else:
    message = "Error In chain"

  response = {
    "message":message
  }

  return jsonify(response),200

app.run(debug=True)


