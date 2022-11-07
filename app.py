from flask import Flask
app = Flask(__name__)

@app.route('/')
def counter():
  return "Hello, How are you?"
