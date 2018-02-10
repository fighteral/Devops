from flask import *
import time;


app = Flask(__name__)
@app.route('/')
def index():
	return render_template("test.html",term=time.asctime(time.localtime(time.time())))
