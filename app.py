from flask import Flask

app = Flask(__name___)

@app.route('/')
def index():
  return 'flask is running'
