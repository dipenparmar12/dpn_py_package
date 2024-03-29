# save this as app.py
from flask import Flask
from dpn_py_package import multiple, add_one

app = Flask(__name__)

@app.route("/")
def hello():
    num = add_one(10)
    num1 = multiple(10)
    return [num, num1]

## Start the development server
# flask run
# flask --app manage run --debug --port 8000

# import os
# running_in_virtualenv = "VIRTUAL_ENV" in os.environ

# # alternative ways to write this, also supporting the case where
# # the variable is set but contains an empty string to indicate
# # 'not in a virtual environment':
# running_in_virtualenv = bool(os.environ.get("VIRTUAL_ENV"))
# running_in_virtualenv = bool(os.getenv("VIRTUAL_ENV")) 