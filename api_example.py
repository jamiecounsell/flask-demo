from flask import Flask, render_template
import urllib2, json

app = Flask("My API Application")

API_ROOT = "http://api.icndb.com/"

@app.route("/norris/<category>")
def norris(category):
	# Build the URL we need to reach
	url = API_ROOT + "jokes/random?limitTo=[" + category + "]"

	# Request data from the API
	req = urllib2.urlopen(url)

	# Read that data into a Python Dictionary
	answer = json.loads(req.read())

	# Render the data to a template
	return render_template("api_info.html", **answer)

if __name__ == "__main__":
	app.run()