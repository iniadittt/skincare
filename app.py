import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates')
from routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
