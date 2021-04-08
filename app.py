import os
from flask import jsonify, request,render_template, Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)

@app.route('/',methods=['POST','GET'])
def hello():
        if request.method == 'POST':
           firstname=request.form['firstname']
           firstname=request.form['lastname']
           email=request.form['email']
           birthday=request.form['birthday']
           sql = "INSERT INTO users(user_name, user_email, user_password) " \
              "VALUES(%s, %s, %s)"
           data = (name, email, pwd)
           try:
              conn = mysql.connect()
              cursor = conn.cursor()
              cursor.execute(sql, data)
              conn.commit()
              cursor.close()
              conn.close()
              resp = jsonify("User created successfully!")
              resp.status_code = 200
              try:
                 conn = mysql.connect()
                 cursor = conn.cursor()
                 cursor.execute("SELECT * FROM users")
                 rows = cursor.fetchall()
                 cursor.close()
                 conn.close()
                 resp = jsonify(rows)
                 resp.status_code = 200
                 return resp
              except Exception as exception:
                 return jsonify(str(exception))
           except Exception as exception:
              return jsonify(str(exception))

        else:
           return render_template('index.html')

if __name__ == "__main__":
        app.run("0.0.0.0",5000, debug=True)

