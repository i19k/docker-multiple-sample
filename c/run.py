from flask import Flask
import requests

print("It worked!")

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = x = requests.get('http://localhost:3892').text
    return a + " (from second server)"

if __name__ == "__main__":
    app.run('0.0.0.0', port=3893)