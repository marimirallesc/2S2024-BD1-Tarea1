
import pyodbc


class MssqlConnection(object):
    def __init__(self):
        self.SERVER = 'mssql-181428-0.cloudclusters.net'
        self.PORT = 19997  
        self.UID = 'Usuario'
        self.PASSWORD = 'Usuario1'
        self.DATABASE = 'BD_PrimeraTarea'

    def connect_mssql(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=%s,%s;'
            'DATABASE=%s;'
            'UID=%s;'
            'PWD=%s' % (self.SERVER, self.PORT, self.DATABASE, self.UID, self.PASSWORD),
            autocommit=True)
        return conn

    def operate_database(self):
   
        connect = self.connect_mssql()
        cursor = connect.cursor()

        # example select login user
        #cursor.execute("exec sp_helplogins;")
        #user_list = [i[0] for i in cursor.fetchall()]
        #print(user_list)
        # row = cursor.fetchone()
        # while row: 
        #     print(row)
        #     row = cursor.fetchone()


        # Listar Empleados
        cursor.execute("EXECUTE [dbo].[ListarEmpleados] 0")

        print(cursor.fetchall() )
        cursor.nextset()
        print(cursor.fetchall() )


        # Insertar Empleado
        # cursor.execute("EXECUTE [dbo].[InsertarEmpleado] Randy, 300000, 0")

        # print(cursor.fetchall() )
            
        connect.close()


if __name__ == '__main__':
    MssqlConnection().operate_database()

