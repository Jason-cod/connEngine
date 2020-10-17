import os
from Config import Config

def run(query):

    ObjConfigLocation = os.getcwd() + '\Test\config.xml'
    dbtype = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbtype')
    dbname = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbname')
    dbhost = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbhost')
    dbport = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbport')
    dbuser = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbuser')
    dbpass = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbpass')


    if dbtype=="postgresql":
        import psycopg2
        try:
            connection = psycopg2.connect(user = dbuser ,
                                  password = dbpass,
                                  host = dbhost,
                                  port = dbport,
                                  database = dbname)

            cursor = connection.cursor()
            cursor.execute(query)
            if query.lower().startswith("insert"): # ignoring case sensitive for insert keyword
                connection.commit()
            if query.lower().startswith("select"):
                print(cursor.fetchone())

        except(Exception,psycopg2.Error) as error:
            print(error)
        finally:
            if(connection):
                cursor.close()
                connection.close()

    elif dbtype == "mysql":
        import mysql.connector
        try:
            connection = mysql.connector.connect(
                                    host= dbhost,
                                    user= dbuser,
                                    passwd= dbpass,
                                    database = dbname)
            cursor = connection.cursor()
            cursor.execute(query, multi=True)
            if "insert" in query.lower(): # ignoring case sensitive for insert keyword
                connection.commit()
            if query.lower().startswith("select"):
                print(cursor.fetchone())

        except(Exception,mysql.connector.Error) as error:
            print(error)
        finally:
            if(connection):
                cursor.close()
                connection.close()


def run_DataTable(query):
    
    ObjConfigLocation = os.getcwd() + '\Test\config.xml'
    dbtype = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbtype')
    dbname = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbname')
    dbhost = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbhost')
    dbport = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbport')
    dbuser = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbuser')
    dbpass = Config.ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbpass')

    if dbtype=="postgresql":
        import psycopg2
        try:
            connection = psycopg2.connect(user = dbuser ,
                                  password = dbpass,
                                  host = dbhost,
                                  port = dbport,
                                  database = dbname)

            cursor = connection.cursor()
            cursor.execute(query)
            if "insert" in query.lower() or "create" in query.lower(): # ignoring case sensitive for insert keyword
                connection.commit()
            if query.lower().startswith("select"):
                return cursor.fetchall()

        except(Exception,psycopg2.Error) as error:
            print(error)
        finally:
            if(connection):
                connection.commit()
                cursor.close()
                connection.close()

    elif dbtype == "mysql":
        import mysql.connector
        try:
            connection = mysql.connector.connect(
                                    host= dbhost,
                                    user= dbuser,
                                    passwd= dbpass,
                                    database = dbname)
            cursor = connection.cursor()
            cursor.execute(query)
            if query.lower().startswith("insert"): # ignoring case sensitive for insert keyword
                connection.commit()
            if query.lower().startswith("select"):
                return cursor.fetchall()
        except(Exception,mysql.connector.Error) as error:
            print(error)
        finally:
            if(connection):
                cursor.close()
                connection.close()