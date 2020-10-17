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
            if query.startswith("Insert"):
                connection.commit()
            print(cursor.fetchone())

        except(Exception,psycopg2.Error) as error:
            print(error)
        finally:
            if(connection):
                cursor.close()
                connection.close()
