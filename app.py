# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

# Instantiate Flask
app = Flask(__name__)

# Establish mongo connections
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Define routes
@app.route("/")
def index():
    mars_data = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars = mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    # Connect to MongoDB
    mars_collection = mongo.db.mars_collection

    # Run the scrape function
    mars_data = scrape.scrape_info()

    # Update the Mongo database using update and upsert=True
    mars_collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
