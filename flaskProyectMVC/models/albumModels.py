from app import mysql

# metodo para obtener albumes activos
def get_all():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_album WHERE state = 1')
    consulta_todo = cursor.fetchall()
    cursor.close()
    return consulta_todo

# Obtener álbum por ID
def get_by_id(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_album WHERE id = %s', (id,))
    result = cursor.fetchone()
    cursor.close()
    return result

# Insertar nuevo álbum
def insert_album(titulo, artista, anio):
    cursor = mysql.connection.cursor()
    cursor.execute(
        'INSERT INTO tb_album (album, artista, anio) VALUES (%s, %s, %s)',
        (titulo, artista, anio)
    )
    mysql.connection.commit()
    cursor.close()

# Metodo para actualizar un álbum
def update_album(id, album, artista, anio_int):
    cursor = mysql.connection.cursor()
    cursor.execute(
        '''
        UPDATE tb_album
        SET album = %s, artista = %s, anio = %s
        WHERE id = %s
        ''',
        (album, artista, anio_int, id)
    )
    mysql.connection.commit()
    cursor.close()

# Eliminar (soft delete)
def soft_delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE tb_album SET state = 0 WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()