import os
import xml.etree.ElementTree as ET

class ReadConfig:

    @staticmethod
    def GetInnerText(ConfigLocation, XPath):
        """ Get Inner Text of a Node (Static Method)

        Args:
            ConfigLocation (str): Config Location
            XPath (str): XPath of the Required Node
        """

        tree = ET.parse(ConfigLocation)
        root = tree.getroot()
        node_list = root.findall("./" + XPath)
        if not node_list:
            return None
        else:
            return node_list[0].text

def run(query):

    ObjConfigLocation = os.getcwd() + '\Test\config.xml'
    dbtype =ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbtype')
    dbname =ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbname')
    dbhost =ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbhost')
    dbport =ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbport')
    dbuser =ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbuser')
    dbpass =ReadConfig.GetInnerText(ObjConfigLocation,'/database/dbpass')


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
            print(cursor.fetchone())

        except(Exception,psycopg2.Error) as error:
            print(error)
        finally:
            if(connection):
                cursor.close()
                connection.close()
