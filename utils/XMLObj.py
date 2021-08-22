# encoding=utf-8
from xml.dom.minidom import parse
import xml.dom.minidom
from xcore.log import Log


class XMLObj(object):

    """docstring for XMLObj"""
    logger = Log.getLogger("xml")
    collection = None

    def __init__(self, fileName):
        super(XMLObj, self).__init__()

        domTree = xml.dom.minidom.parse(fileName)
        # root
        self.collection = domTree.documentElement
        self.logger.info("root el: %s" % self.collection.nodeName)
        if self.collection.hasAttribute("shelf"):
            self.logger.info("Root element : %s" % self.collection.getAttribute("shelf"))

    """需要节点唯一"""

    def getElementsAttrByTagName(self, name, attr):
        attrValue = None
        connectorList = self.collection.getElementsByTagName(name)

        if len(connectorList) > 1:
            self.logger.warn("has mult node: %s" % name)
            # return attrValue
        for connector in connectorList:
            if (connector is not None and connector.hasAttribute(attr)):
                attrValue = connector.getAttribute(attr)
            self.logger.info(attrValue)
        return attrValue
