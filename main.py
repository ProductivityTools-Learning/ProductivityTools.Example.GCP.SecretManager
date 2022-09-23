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
    name = "projects/17710308926/secrets/pwsecret/versions/1"
    r=client.access_secret_version(request={"name":name})
    return r

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
