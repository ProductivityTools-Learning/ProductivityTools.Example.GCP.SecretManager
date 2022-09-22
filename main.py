from flask import Flask
import os

app = Flask(__name__)

@app.route("/Hello")
def hello():
    return "<p>Hello</p>"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
