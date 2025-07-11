from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

#album
app = Flask(__name__)

app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] ="root"
app.config['MYSQL_PASSWORD'] ="Badillo83"
app.config['MYSQL_DB'] ="Examen2"
#app.config['MYSQL_PORT'] =3306 // usar solo en cambio de puerto
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Contactos WHERE state= 1')
        consultaTodo = cursor.fetchall()
        return render_template('contactos.html', errores={}, contactos = consultaTodo)
    
    except Exception as e:
        print('Error: ' + e)
        return render_template('contactos.html', errores={}, contactos = [])
    finally:
        cursor.close()

@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Contactos WHERE id = %s', (id,))
        consultaId = cursor.fetchone()
        return render_template('consulta.html', contacto = consultaId)
    
    except Exception as e:
        print('Error al consultar por id: ' + e)
        return redirect(url_for('home'))
    finally:
        cursor.close()

#inicia
@app.route('/editar/<int:id>')
def editar(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Contactos WHERE id = %s', (id,))
    contacto = cursor.fetchone()
    cursor.close()
    
    if contacto is None:
        flash('Contacto no encontrado')
        return redirect(url_for('home'))
    
    return render_template('formUpdates.html', contacto=contacto)


@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    # 1. Recoger datos del formulario
    VNombre = request.form.get('TxtNombre', '').strip()
    VCorreo = request.form.get('TxtCorreo', '').strip()
    VTelefono = request.form.get('TxtTelefono', '').strip()
    VEdad = request.form.get('TxtEdad', '').strip()

    # 2. Validar datos
    errores = {}

    if not VNombre:
        errores['TxtNombre'] = 'El nombre es obligatorio'
    if not VCorreo:
        errores['TxtCorreo'] = 'El correo es obligatorio'
    if not VTelefono:
        errores['TxtTelefono'] = 'El telefono es obligatorio'
    if not VEdad:
        errores['TxtEdad'] = 'La edad es obligatoria'
    else:
        try:
            edad_int = int(VEdad)
            if edad_int < 1 or edad_int > 105:
                errores['TxtEdad'] = 'Ingresa una edad valida (entre 1 y 105)'
        except ValueError:
            errores['TxtEdad'] = 'La edad debe ser un numero valido'

    # 3. Si hay errores, volver al formulario con errores
    if errores:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Contactos WHERE id = %s', (id,))
        contacto_data = cursor.fetchone()
        cursor.close()
        return render_template('formUpdate.html', contacto=contacto_data, errores=errores)

    # 4. Si no hay errores, actualizar en la base de datos
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE Contactos
            SET nombre = %s, correo = %s, telefono = %s, edad = %s
            WHERE id = %s
        """, (VNombre, VCorreo, VTelefono, edad_int, id))
        mysql.connection.commit()
        flash('Contacto actualizado en BD')
    except Exception as e:
        mysql.connection.rollback()
        flash(f'Error al actualizar: {str(e)}', 'danger')
    finally:
        cursor.close()

    return redirect(url_for('home'))
# termina
    
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/guardarContacto', methods = ['POST'])
def guardar():

    #lista de errores
    errores={}

    #obtener los datos a insertar
    VNombre= request.form.get('txtNombre', '').strip()
    VCorreo= request.form.get('txtCorreo', '').strip()
    VTelefono= request.form.get('txtTelefono', '').strip()
    VEdad= request.form.get('txtEdad', '').strip()

    if not VNombre:
        errores['txtNombre']= 'Nombre del contacto es obligatorio'
    if not VCorreo:
        errores['txtCorreo']= 'Correo del contacto obligatorio'
    if not VTelefono:
        errores['txtTelefono']= 'El telefono es obligatorio'
    if not VEdad:
        errores['txtEdad']= 'La edad es obligatoria'
    elif not VEdad.isdigit() or int(VEdad)< 1 or int(VEdad)> 105:
        errores['txtEdad']= 'No ingresaste una edad valida'

    if not errores:
        #Intentamos ejecutar el INSERT
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into Contactos(nombre,correo,telefono,edad) values(%s,%s,%s,%s)', (VNombre, VCorreo, VTelefono, VEdad))
            mysql.connection.commit()
            flash('Contacto se guardo en BD')
            return redirect(url_for('home'))
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: '+ str(e))
            return redirect(url_for('contactos'))
        finally:
            cursor.close()
    return render_template('contactos.html', errores= errores)
#eliminar
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE Contactos SET state = 0 WHERE id = %s', (id,))
        mysql.connection.commit()
        flash('Contacto eliminado correctamente.')
    except Exception as e:
        print('Error al eliminar contacto: ' + str(e))
        flash('Error al eliminar contacto')
    finally:
        cursor.close()
    
    return redirect(url_for('home'))

@app.route('/confirmarEliminar/<int:id>')
def confirmarEliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Contactos WHERE id = %s', (id,))
        contacto = cursor.fetchone()
        if contacto is None:
            flash("Contacto no encontrado")
            return redirect(url_for('home'))
        return render_template('confirmDel.html', contacto=contacto)
    except Exception as e:
        print('Error al cargar confirmación: ' + str(e))
        flash("Error al intentar eliminar")
        return redirect(url_for('home'))
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(port=3000, debug=True)

