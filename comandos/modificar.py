import mysql.connector
import hashlib

def conectar():
    # Modifica estos valores según tu configuración de MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='ahorcado'
    )
    return conexion

def mostrar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

def insertar_usuario(conexion, nombre, contraseña):
    cursor = conexion.cursor()
    contraseña_hash = hashlib.sha256(contraseña.encode()).hexdigest()
    cursor.execute('''
        INSERT INTO usuarios (nombre, contraseña_hash)
        VALUES (%s, %s)
    ''', (nombre, contraseña_hash))
    conexion.commit()

def borrar_usuario_por_id(conexion, id_usuario):
    cursor = conexion.cursor()
    cursor.execute('''
        DELETE FROM usuarios
        WHERE id = %s
    ''', (id_usuario,))
    conexion.commit()

if __name__ == "__main__":
    conexion_mysql = conectar()

    while True:
        print("\nOpciones:")
        print("1. Mostrar usuarios")
        print("2. Añadir usuario")
        print("3. Borrar usuario por ID")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nUsuarios:")
            mostrar_usuarios(conexion_mysql)
        elif opcion == "2":
            nombre_usuario = input("Ingresa el nombre de usuario: ")
            contraseña_usuario = input("Ingresa la contraseña: ")
            insertar_usuario(conexion_mysql, nombre_usuario, contraseña_usuario)
            print("Usuario añadido correctamente.")
        elif opcion == "3":
            id_usuario = input("Ingresa el ID del usuario a borrar: ")
            borrar_usuario_por_id(conexion_mysql, id_usuario)
            print("Usuario borrado correctamente.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

    # Cierra la conexión a MySQL
    conexion_mysql.close()