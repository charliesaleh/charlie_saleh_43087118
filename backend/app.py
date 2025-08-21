from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Charlie Saleh here in Flask, Hello!"

app.run(debug=True)
