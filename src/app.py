from flask import Flask
from decouple import config
from modelo.Clientes import ModeloCliente
from config import config

app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return " hola mundo "

#mostrar todos los clientes
@app.route("/clientes", methods=['GET'])
def listar_Cliente():
    resul=ModeloCliente.listar_Cliente()
    return resul

#buscar un  cliente
@app.route("/clientes/:<codigo>", methods=['GET'])
def lista_Cliente(codigo):
    resul=ModeloCliente.lista_Cliente(codigo)
    return resul

#registrar un cliente
@app.route("/clientes", methods=['POST'])
def guardar_cliente():
    resul=ModeloCliente.registrar_cliente()
    return resul

#actualizar un cliente
@app.route("/clientes/:<codigo>", methods=['PUT'])
def actualizar_cliente(codigo):
    resul=ModeloCliente.actualizar_cliente(codigo)
    return resul

#eliminar un cliente
@app.route("/clientes/:<codigo>", methods=['DELETE'])
def elimineycion_cliente(codigo):
    resul=ModeloCliente.eliminar_cliente(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>Pagina no Encontrada</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0',debug=True)