# A Mission to Mars!

University of Minnesota Data Visualization and Analysis BootCamp<br>
Stephanie Richards

![Mars Panorama](Images/1-mars.jpg)<br>

# Goals: <br>
<p> For this assignment, we were tasked to write a script that would scrape a number of websites using Splinter and Python Pandas, write all the information to MongoDB, and then use Flask and Jinja2 to render a website to display that data.

# Methods: <br>

I used Pandas, Splinter, and Beautiful Soup to scrape data from several websites related to Mars and Mars exploration. I wrote my code in a Jupyter Notebook in order to have a dynamic tool to use for debugging, and then transferred that code into a Python file called "scrape.py". The .ipynb file is located in the Mission_to_Mars folder in this repository.

Using the scrape.py file as a basis, I built an app.py file to run a Flask server to display the results. The website is built using Bootstrap 4, and has a button that activates the scrape function to get the most up-to-date Mars data provided by each source. I added a small amount of CSS to a "style" file to make the site slightly more attractive.

# Contained in This Repo:
* A folder called "Images", which contains the header image for this ReadMe and the screenshots of the finished website
* A folder called "Mission_to_Mars", which contains the Jupyter Notebook used to do the initial scripting
* A folder called "Static" that contains the CSS code for the finished website
* A folder called "templates" that contains the html index file
* A file called "app.py" that builds the routes used to render the Flask server and the website
* A file called "scrape.py" that contains the code used to scrape the various websites
* This README file

## If You Wish to Recreate This Site: <br>

You will need Mongo DB. The files will create a database called mars_db, containing a document called mars_collection.