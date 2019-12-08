from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__) 

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", news=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    mars_data = mongo.db.mars_data
    headline = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_data.update({}, headline, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
