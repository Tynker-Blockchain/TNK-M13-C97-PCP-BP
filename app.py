from flask import Flask, render_template, request, redirect
import os
from time import time
# Import Wallet class
from wallet import Account

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

account = Account()
# Create myWallet using Wallet class


@app.route("/", methods= ["GET", "POST"])
def index():
    # Access myWallet as global
    global account
      
    # Call checkConnection() method and store the result in isConnected variable
    

    balance = "No Balance"

    if(account):
        balance = 0
    
    # Pass isConnected as isConnected
    return render_template('index.html', account= account, balance = balance)
   
@app.route('/transactions')
def transactions():
    global account    
    return render_template('transactions.html', transactions=[], account={})

if __name__ == '__main__':
    app.run(debug = True, port=4000)
