from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Badillo83"
app.config['MYSQL_DB']= "dbflask"
#app.config['MYSQL_PORT']= 3306 //solo si se cambia el puerto

mysql= MySQL(app)

#ruta para probar la conección a mysql
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ), 200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ), 200

@app.route('/')
def home():
    return 'Hola mundo Flask'

if __name__ == '__main__':
    app.run(port= 3000, debug= True)
