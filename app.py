from flask import Flask
import mysql.connector

# connect to db
db = mysql.connector.connect(
    host="localhost",
    user="dev",
    password="!developer"
)
# get db cursor to write sql queries
dbcursor = db.cursor()
# the db name to create
dbname = 'smarthealth'
# create database if not already created
dbcursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(dbname))

# init Flask app
app = Flask(__name__)

@app.route('/')
def index():
    dbcreated = False
    # get list of tables
    dbcursor.execute("SHOW DATABASES")
    for database in dbcursor:
        # if table name is in the created tables set dbcreated to True
        if database[0] == dbname:
            dbcreated = True
    return 'Hello, world! ' + ('Database "{}" created successfully!'.format(dbname) if dbcreated else 'Check database connectivity!')

if __name__ == "__main__":
    app.run(debug=True) 