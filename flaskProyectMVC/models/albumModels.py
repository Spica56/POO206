from app import mysql

#metodo para obtener albums activos
def getAll():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_album WHERE state= 1')
    consultaTodo = cursor.fetchall()
    cursor.close()
    return consultaTodo

#metodo para obtener album ID
def getById(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_album WHERE id = %s', (id,))
    consultaId = cursor.fetchone()
    cursor.close()
    return consultaId

#metodo para insertar un album
def insertAlbum(Vtitulo,Vartista,Vanio):
    cursor= mysql.connection.cursor()
    cursor.execute('insert into tb_album(album,artista,anio) values(%s,%s,%s)', (Vtitulo, Vartista, Vanio))
    mysql.connection.commit()
    cursor.close()

#metodo para actualizar un album
def updateAlbum(id,Vtitulo,Vartista,Vanio):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE tb_album
        SET album = %s, artista = %s, anio = %s
        WHERE id = %s
        """, (album, artista, anio_int, id))
    mysql.connection.commit()
    cursor.close()

#metodo para eliminar un album
def softDeleteAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE tb_album SET state = 0 WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()

#metodo para confirmar eliminación
def ConfirmDelete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_album WHERE id = %s', (id,))
    album = cursor.fetchone()
    cursor.close()