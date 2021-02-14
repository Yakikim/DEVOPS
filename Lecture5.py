import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='LXf29u1CXu', passwd='0BRRO69NXP', db='LXf29u1CXu', autocommit=True)

# Getting a cursor from Databas

cursor = conn.cursor()
cursor.execute("insert into LXf29u1CXu.users(user_id, user_name,creation_date) values (5, 'John','dd');")

cursor.execute("insert into LXf29u1CXu.users(user_id, user_name, creation_date)  values (6, 'yAKI','dd');")
# Getting all data from table “users”
cursor.execute("SELECT * FROM LXf29u1CXu.users;")
#cursor.execute("commit;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

########################################################
import requests

res =  requests.get("https://api.exchangeratesapi.io/latest?base=USD")
data = res.json()
results = data['rates']
currency_value = results['ILS']
print("Result is: ", data)
#######################################################
from flask import Flask, request

app = Flask(__name__)

# local users storage
users = {}
# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        return {'user_id': user_id, 'user_name': users[user_id]}, 200 # status code

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        return {'user id': user_id , 'user name': user_name, 'status': 'saved'}, 200 # status code
  # todo elif for put and delete


app.run(host='127.0.0.1', debug=True, port=5000)