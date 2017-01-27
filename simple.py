from flask import Flask
app = Flask("My Application")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()