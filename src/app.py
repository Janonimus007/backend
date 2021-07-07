from bson.objectid import ObjectId
from flask import Flask,request,jsonify
from flask.json import jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)

CORS(app)

db = mongo.db.users

#contactar a la empresa (queda registrado el contacto y el motivo)
@app.route('/contacto',methods=['POST'])
def contacto():
    id = db.insert({
        'name':request.json['name'],
        'email':request.json['email'],
        'num_telefono':request.json['num_telefono'],
        'msj_contacto':request.json['msj_contacto']
    })
    return jsonify(str(ObjectId(id)))

#registrar usuario
@app.route('/trabajadores',methods=['POST'])
def createTrabajadores():
    id = db.insert({
        'name':request.json['name'],
        'email':request.json['email'],
        'num_telefono':request.json['num_telefono'],
        'direccion':request.json['direccion'],
        'paassword':request.json['paassword'],
        'codigo':request.json['codigo']
    })
    return jsonify(str(ObjectId(id)))

#reservar hora
@app.route('/reservas',methods=['POST'])
def createReservas():
    id = db.insert({
        'email':request.json['email'],
        'name':request.json['name'],
        'comuna':request.json['comuna'],
        'direccion':request.json['direccion'],
        'comentarios':request.json['comentarios'],
        'marca_vehiculo':request.json['marca_vehiculo'],
        'ano':request.json['ano'],
        'modelo':request.json['modelo'],
        'problema':request.json['problema']
    })
    return jsonify(str(ObjectId(id)))
   
#ingreso trabajadores
@app.route('/users',methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
            '_id':str(ObjectId(doc['_id'])),
            'email':doc['email'],
            'password':doc['password'],
        })
    return jsonify(users)


    
#cancelacion de hora
@app.route('/users/<id>',methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'hora cancelada'})

#cambio contraseña trabajadores 
@app.route('/users/<id>',methods=['PUT'])
def updateUser(id):
    db.update_one({'_id':ObjectId(id)},{'$set':{
        
        'password':request.json['password'],
    }})
    return jsonify({'msg': 'contrasena Update'})

if __name__ == "__main__":
    app.run(debug=True)
