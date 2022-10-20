from flask import Flask
from card import Card
import generator

app = Flask(__name__)

@app.route("/")
def home():
    generator.read_all()
    return "Hello Flask!"

if __name__ == "__main__":
    app.run()