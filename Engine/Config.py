import xml.etree.ElementTree as ET


'''
Change Note(s)

# v0.0.1 - Added ReadConfigByObject.GetInnerText, ReadConfig.GetInnerText, ReadConfig.GetNodeAttribList, ReadConfig.GetNodeAttrib - drathi

'''


class Config:

    class ReadConfigByObject:

        def __init__(self, ConfigLocation, XPath):
            self.ConfigLocation = ConfigLocation
            self.XPath = XPath

        def GetInnerText(self):
            """ Get Inner Text of a Node by Object Call

            Args:
                ConfigLocation (str): Config Location
                XPath (str): XPath of the Required Node
            """

            self.tree = ET.parse(self.ConfigLocation)
            self.root = self.tree.getroot()
            self.node_list = self.root.findall("./" + self.XPath)
            if not self.node_list:
                return None
            else:
                return self.node_list[0].text

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

        @staticmethod
        def GetNodeAttribList(ConfigLocation, XPath):
            """ Get Attributes of a Node (Static Method) returns value in array

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
                return node_list[0].attrib

        @staticmethod
        def GetNodeAttrib(ConfigLocation, XPath, Attribute):
            """ Get Attribute Specific Value of a Node (Static Method) returns value in string

            Args:
                ConfigLocation (str): Config Location
                XPath (str): XPath of the Required Node
                Attribute (str): Attibute of the Required Node

            """

            tree = ET.parse(ConfigLocation)
            root = tree.getroot()
            node_list = root.findall("./" + XPath)
            if not node_list:
                return None
            else:
                return node_list[0].attrib[Attribute]
