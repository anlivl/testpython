
from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python! New"+ random.choice(["1","2","3"])

@app.route("/read_file")
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return "Text=" + contents

if __name__ == "__main__":
    app.run(host='0.0.0.0')
