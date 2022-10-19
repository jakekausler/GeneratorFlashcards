from flask import Flask
from card import Card

app = Flask(__name__)

@app.route("/")
def home():
    card = Card(0)
    card.fields = ["This", "is a", "test of underline"]
    print(card)
    return "Hello Flask!"

if __name__ == "__main__":
    app.run()