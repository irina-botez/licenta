from zope.interface import implementer
from makeup.platform.interfaces import IClient
from plone.dexterity.content import Item
from zope.component.hooks import getSite

@implementer(IClient)
class Client(Item):
    """Client Content Type"""

def on_add(obj, evt):
    site = getSite()

    obj.REQUEST.RESPONSE.redirect(site.absolute_url())
