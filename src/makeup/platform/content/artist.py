from zope.interface import implementer
from makeup.platform.interfaces import IArtist
from plone.dexterity.content import Container

@implementer(IArtist)
class Artist(Container):
    """MakeupArtist Content Type"""
