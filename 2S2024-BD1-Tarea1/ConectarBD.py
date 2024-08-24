import pyodbc

class MssqlConnection:
    def __init__(self):
        self.connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=mssql-181428-0.cloudclusters.net,19997;'
            'DATABASE=BD_PrimeraTarea;'
            'UID=Usuario;'
            'PWD=Usuario1'
        )

    def connect_mssql(self):
        try:
            return pyodbc.connect(self.connection_string)
        except pyodbc.Error as ex:
            print(f"Connection error: {ex}")
            raise
      
    def listarEmpleados(self): 
        connect = self.connect_mssql()
        cursor = connect.cursor()   
        
        cursor.execute("EXECUTE [dbo].[ListarEmpleados] 0")
        empleados = cursor.fetchall()
        
        cursor.nextset()
        empleados = cursor.fetchall()
        
        #print('Empleados: /n', empleados)

        connect.close()
        return [{'Id': row[0], 'Nombre': row[1], 'Salario': float(row[2])} for row in empleados]

    def insertarEmpleado(self, nombre, salario):
        try:
            connect = self.connect_mssql()
            cursor = connect.cursor()

            # Ejecución del procedimiento almacenado con los nombres correctos de parámetros
            cursor.execute("""
                DECLARE @OutResult INT;
                EXECUTE [dbo].[InsertarEmpleado] @inNombre=?, @inSalario=?, @OutResult=@OutResult OUTPUT;
                """, (nombre, salario))

            connect.commit()
            cursor.close()
            connect.close()
            return 0  # Retorna 0 si todo fue exitoso
        except pyodbc.Error as ex:
            print(f"Error inserting employee: {ex}")
            return -1  # Retorna -1 si hubo un error

if __name__ == '__main__':
    # Ejemplo de uso
    nombre = 'Penelope Cruz'
    salario = 500000

    conexion = MssqlConnection()
    #conexion.insertarEmpleado(nombre, salario)

    empleados = conexion.listarEmpleados()  # Asegúrate de llamar a listarEmpleados
    
    
    #listar = MssqlConnection().listarEmpleados()
