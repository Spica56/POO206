from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModels import *

albumsBP = Blueprint('albums', __name__)

@albumsBP.route('/')
def home():
    try:
        consulta_todo = get_all() #FUNCIÓN DE OBTENER ALBUMES
        return render_template('formulario.html', errores={}, albums=consulta_todo)
    except Exception as e:
        print('Error al consultar todo: ' + str(e))
        return render_template('formulario.html', errores={}, albums=[])

@albumsBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        consulta_id = get_by_id(id) #FUNCION PARA OBTENER ALBUM POR ID
        return render_template('consulta.html', album=consulta_id)
    except Exception as e:
        flash('Error al consultar el álbum: ' + str(e))
        return redirect(url_for('albums.home'))

@albumsBP.route('/guardarAlbum', methods=['POST'])
def guardar():
    errores = {}
    titulo = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()

    if not titulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not artista:
        errores['txtArtista'] = 'Artista obligatorio'
    if not anio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'

    if errores:
        return render_template('formulario.html', errores=errores, albums=get_all())

    try:
        insert_album(titulo, artista, anio) #FUNCION DE INSERTAR ALBUM
        flash('Álbum guardado en la BD')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al guardar: ' + str(e))
        return redirect(url_for('albums.home'))

@albumsBP.route('/editar/<int:id>')
def editar(id):
    album = get_by_id(id) #FUNCION PARA OBTENER ALBUM POR ID REUTILIZADA
    
    if album is None:
        flash('Álbum no encontrado')
        return redirect(url_for('albums.home')) 
    
    return render_template('formUpdates.html', album=album)

@albumsBP.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    # 1. Recoger datos del formulario
    album = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()

    # 2. Validar datos
    errores = {}

    if not album:
        errores['txtTitulo'] = 'El título del álbum es obligatorio'
    if not artista:
        errores['txtArtista'] = 'El artista es obligatorio'
    if not anio:
        errores['txtAnio'] = 'El Año es obligatorio'
    else:
        try:
            anio_int = int(anio)
            if anio_int < 1800 or anio_int > 2030:
                errores['TxtAnio'] = 'Ingresa un año válido (entre 1800 y 2030)'
        except ValueError:
            errores['TxtAnio'] = 'El año debe ser un número válido'

    if errores:
        album_data= get_by_id(id) #REUTILIZACIÓN DE GET BY ID
        return render_template('formUpdate.html', album=album_data, errores=errores)

    try:
        update_album(id, album, artista, anio_int)
        flash('Álbum actualizado en la BD')
    except Exception as e:
        mysql.connection.rollback()
        flash(f'Error al actualizar: {str(e)}', 'danger')

    return redirect(url_for('albums.home'))

@albumsBP.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    try:
        soft_delete(id)
        flash('Álbum eliminado correctamente')
    except Exception as e:
        print('Error al eliminar el álbum: ' + str(e))
        flash('Error al eliminar el álbum')
    return redirect(url_for('albums.home'))    

@albumsBP.route('/confirmar_eliminar/<int:id>')
def confirmar_eliminar(id):
    try:
        album = get_by_id(id) #SE VUELVE A REUTILIZAR EL FETCHONE
        if album is None:
            flash("Álbum no encontrado")
            return redirect(url_for('home'))
        return render_template('confirmDel.html', album=album)
    except Exception as e:
        print('Error al cargar confirmación: ' + str(e))
        flash("Error al intentar eliminar")
    return redirect(url_for('albums.home'))