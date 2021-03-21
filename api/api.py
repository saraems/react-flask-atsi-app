from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': {'hour': datetime.now().hour, 'minute': datetime.now().minute}}