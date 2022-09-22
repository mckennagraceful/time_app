from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/time')
def print_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
