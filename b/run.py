from flask import Flask

print("It worked!")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run('0.0.0.0', port=3892)