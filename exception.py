from flask import Flask 
from src.logger import logging 
from src.exception import CustomException
import os,sys
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def index():
    try:
        raise Exception("we are testing our Exception file")
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)
        
        logging.info("We are testing out logging file")
    
    return "Welocme to Engineering Wala Bhaiya"


if __name__ == "__main__":
    app.run(debug =True) 