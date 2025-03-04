from flask import Flask 
from src.logger import logging 

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def index():
    logging.info("We are testing out logging file")
    
    return "Welocme to Engineering Wala Bhaiya"


if __name__ == "__main__":
    app.run(debug =True) 