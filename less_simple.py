from flask import Flask
app = Flask("My Application")

@app.route("/user/<username>")
def hello(username):
    return "This is " + username + "'s page."

if __name__ == "__main__":
    app.run()