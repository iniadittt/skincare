import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask

app = Flask(__name__, template_folder='templates')

from routes     import *

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))