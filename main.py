from flask import Flask
import os
from google.cloud import secretmanager


app = Flask(__name__)

@app.route("/Hello")
def hello():
    return "<p>Hello</p>"

@app.route("/Secret")
def secret():
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/banded-edge-363320/secrets/pwujczyk/versions/1"
    r=client.access_secret_Version(request={"name":"pwsecret"})
    return r

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
