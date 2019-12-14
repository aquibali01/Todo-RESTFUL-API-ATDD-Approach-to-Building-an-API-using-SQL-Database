import unittest 
from ToDoApp import app
import requests, json

class test_toDoApp(unittest.TestCase):

    def setUp(self):
        app.config["MYSQL_USER"] = "sql12315418"
        app.config["MYSQL_PASSWORD"] = "XEDkPGFIBw"
        app.config["MYSQL_HOST"] = "sql12.freemysqlhosting.net"
        app.config["MYSQL_DB"] = "sql12315418"
        app.config["MYSQL_CURSORCLASS"] = "DictCursor"      
        self.client = app.test_client()   


    # testing retrieving all task functionality
    def test_get_tasks(self):
        result = self.client.get("http://127.0.0.1:5000//todo/api/v1.0/tasks")
        self.assertEqual(result.status_code, 200)

    # testing retrieving a task functionality
    def test_get_a_task(self):
        result = self.client.get("http://127.0.0.1:5000//todo/api/v1.0/tasks/1")
        self.assertEqual(result.status_code, 200)

        data = json.loads(result.data)
        self.assertEqual(data["task"][0]["tile"], "Book an Airline tick")
        self.assertEqual(data["task"][0]["description"], "Call the travel agent to reserve ticket ")

    # tesing a delete task functionality
    def test_delete_a_task(self):
        result = self.client.delete("http://127.0.0.1:5000//todo/api/v1.0/tasks/0")
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()