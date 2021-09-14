import time

from flask import Flask,render_template,request
import random
from flask_restful import Api,Resource




app=Flask(__name__)
api=Api(app)





##### MAIN PAGE
@app.route("/")
def index():
   return "Hi guys" 


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)
