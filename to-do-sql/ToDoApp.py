# importing all the libraries

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

#connecting to the MySQL database
app.config["MYSQL_USER"] = "sql12315418"
app.config["MYSQL_PASSWORD"] = "XEDkPGFIBw"
app.config["MYSQL_HOST"] = "sql12.freemysqlhosting.net"
app.config["MYSQL_DB"] = "sql12315418"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

#creating a TABLE in the database
mysql = MySQL(app)
@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE todo (id INTEGER, tile VARCHAR(20), description VARCHAR(40), done BOOLEAN)''')
    return "Table Created!"

# # Adding the Tasks to the database

@app.route("/todo/api/v1.0/tasks", methods=["POST"])
def add_task():
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO todo VALUES (0, 'Meeting with the Boss', 'The Meeting is with Mr. Ali @ 11 A.M', False)''')
    cur.execute('''INSERT INTO todo VALUES (1, 'Book an Airline ticket', 'Call the travel agent to reserve ticket for venice', true)''')
    cur.execute('''INSERT INTO todo VALUES (2, 'Brother Birthday', 'Have to wish Haris a birthday', true)''')
    mysql.connection.commit()
    return "Added the task(s)"

#Retreiving all the tasks
@app.route("/todo/api/v1.0/tasks", methods=["GET"])
def get_all_tasks():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM todo''')
    result = cur.fetchall()
    return jsonify({"task": result})

#retrieving a single task
@app.route("/todo/api/v1.0/tasks/<int:id>", methods=["GET"])
def get_a_task(id):
    cur = mysql.connection.cursor()
    cur.execute(f'''SELECT * FROM todo WHERE id={id}''')
    result = cur.fetchall()
    return jsonify({"task": result})

#deleting a task 
@app.route("/todo/api/v1.0/tasks/<int:id>", methods=["DELETE"])
def delete_a_tasks(id):
    cur = mysql.connection.cursor()
    cur.execute(f'''DELETE FROM todo WHERE id={id};''')
    mysql.connection.commit()
    return "done deleted a task!"
    
#updating a task 
@app.route("/todo/api/v1.0/tasks/<int:id>", methods=["PUT"])
def update_a_task(id):
    cur = mysql.connection.cursor()
    cur.execute(f'''UPDATE todo SET tile="Book a Railway Ticket" WHERE id={id};''')
    mysql.connection.commit()
    return "Done updating a task"


if __name__ == "__main__":
    app.run(debug=True)
