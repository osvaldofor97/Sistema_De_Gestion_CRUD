from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sistema'
mysql = MySQL(app)

@app.route('/api/customers/<int:id>') # GET
@cross_origin()
def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, firstname, lastname, email, phone FROM `sistema`.`customers` WHERE id = "+str(id)+";")
    data  = cur.fetchall()
    content = {}
    for i in data:
        content = { 
                'id': i[0],
                'firstname': i[1],
                'lastname': i[2],
                'email': i[3],
                'phone': i[4]
            }
        
    return jsonify(content)

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, firstname, lastname, email, phone FROM `sistema`.`customers`;")
    data  = cur.fetchall()
    result = []
    for i in data:
        content = { 
                'id': i[0],
                'firstname': i[1],
                'lastname': i[2],
                'email': i[3],
                'phone': i[4]
            }
        
        result.append(content)
        
    return jsonify(result)

@app.route('/api/customers', methods = ['POST'])
@cross_origin()
def saveCustomer():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `sistema`.`customers` (`firstname`, `lastname`, `email`, `phone`) VALUES (%s, %s, %s, %s);",(request.json['firstname'],request.json['lastname'],request.json['email'],request.json['phone']))
    mysql.connection.commit()
    return "Cliente guardado"

@app.route('/api/customers', methods = ['PUT'])
@cross_origin()
def updateCustomer():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE `sistema`.`customers` SET `firstname` = %s, `lastname` = %s, `email` = %s, `phone` = %s WHERE `id` = %s;", (request.json['firstname'],request.json['lastname'],request.json['email'],request.json['phone'],request.json['id']))
    mysql.connection.commit()
    return "Cliente actualizado"

@app.route('/api/customers/<int:id>', methods = ['DELETE'])
@cross_origin()
def removeCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `sistema`.`customers` WHERE id = "+str(id)+";")
    mysql.connection.commit()
    return "Cliente eliminado por id"

@app.route('/')
@cross_origin()
def Index():
    return render_template('index.html')

@app.route('/<path:path>')
@cross_origin()
def publicFiles(path):
    return render_template(path)

if __name__ == '__main__':
    app.run(None, 3000, True)