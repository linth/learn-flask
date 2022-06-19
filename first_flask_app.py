'''
first flask application.

Reference:
    - https://www.youtube.com/watch?v=UdRxvHVXTxA
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello flask. it\'s my first flask application.'


app.run()