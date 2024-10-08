from flask import Flask, request, jsonify, render_template
from ConectarBD import MssqlConnection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/insertar/')
def insertar():
    return render_template('insertar.html')

# Rutas existentes
@app.route('/listar_empleados', methods=['GET'])
def listar_empleados():
    try:
        db = MssqlConnection()
        empleados = db.listarEmpleados()
        if empleados == 50005:  #Error en la BD
            raise Exception("Lista de empleados no disponible")
        else:
            return jsonify(empleados)
    except Exception as e:
        print(f"Error al listar empleados: {e}")  # Agrega un mensaje de error para depuración
        return jsonify({'error': str(e)})

@app.route('/insertar_empleado', methods=['POST'])
def insertar_empleado():
    try:
        data = request.json
        nombre = data.get('nombre')
        salario = data.get('salario')
        
        db = MssqlConnection()
        resultado = db.insertarEmpleado(nombre, salario)
        
        if resultado == 0:
            return jsonify({'success': True})
        elif resultado == 50006:
            return jsonify({'success': False, 'message': 'El empleado ya existe'})
        else:
            return jsonify({'success': False, 'message': 'Error al insertar el empleado'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
