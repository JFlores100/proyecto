from modelo.Conexion import conexion2023
from flask import jsonify,request

def buscar_cli(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM cliente WHERE ci = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            cli = {'ci': datos[0], 'nombre': datos[1],
                       'apellido': datos[2], 'correo': datos[3],
                       'fecha_nac': datos[4], 'genero': datos[5], 
                       'direccion': datos[6], 'pais': datos[7],
                       'telefono': datos[8]}
            return cli
        else:
            return None
    except Exception as ex:
            raise ex

class ModeloCliente():
    def listar_Cliente():
        try:
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM cliente")
            datos = cursor.fetchall()
            Clientes = []

            for fila in datos:
                cli = {'ci':fila[0],
                        'nombre':fila[1],
                        'apellido':fila[2],
                        'correo':fila[3],
                        'fecha_nac':fila[4],
                        'genero':fila[5],
                        'direccion':fila[6],
                        'pais':fila[7],
                        'telefono':fila[8]}
                
                Clientes.append(cli)

            conn.close()
            return jsonify({'clientes': Clientes, 'mensaje': "clientes listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error",'exito':False})
        
    @classmethod
    def lista_Cliente(self,codigo):
        try:
            cliente = buscar_cli(codigo)
            if cliente != None:
                return jsonify({'clientes': cliente, 'mensaje': "cliente encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Cliente no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def registrar_cliente(self):
        try:
            cliente = buscar_cli(request.json['ci_e'])
            if cliente != None:
                return jsonify({'mensaje': "El ci  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO cliente values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (request.json['ci_e'], request.json['nombre_e'], 
                                                                                       request.json['apellido_e'], request.json['correo_e'], 
                                                                                       request.json['fecha_nac_e'], request.json['genero_e'],
                                                                                       request.json['direccion_e'], request.json['pais_e'],
                                                                                       request.json['telefono_e']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Cliente registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def actualizar_cliente(self,codigo):
        try:
            cliente = buscar_cli(codigo)
            if cliente != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE cliente SET nombre=%s, apellido=%s, correo=%s,
                            fecha_nac=%s, genero=%s, direccion=%s, pais=%s, 
                            telefono=%s  WHERE ci=%s""",
                        (request.json['nombre_e'], request.json['apellido_e'], request.json['correo_e'], 
                             request.json['fecha_nac_e'], request.json['genero_e'], request.json['direccion_e'],
                            request.json['pais_e'], request.json['telefono_e'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "cliente actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "cliente no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_cliente(self,codigo):
        try:
            usuario = buscar_cli(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM cliente WHERE ci = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "cliente eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "cliente no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})