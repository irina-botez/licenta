from zope.interface import implementer
from makeup.platform.interfaces import IClient
from plone.dexterity.content import Container

@implementer(IClient)
class Client(Container):
    """Client Content Type"""
