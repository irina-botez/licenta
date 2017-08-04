from zope.interface import implementer
from makeup.platform.interfaces import IClient
from plone.dexterity.content import Item

@implementer(IClient)
class Client(Item):
    """Client Content Type"""
