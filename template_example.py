from flask import Flask, render_template
app = Flask("My Template Application")

@app.route("/user/<username>")
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == "__main__":
    app.run()