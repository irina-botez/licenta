from zope.interface import Interface
from makeup.platform import _
from plone.supermodel import model
from zope import schema

class ICustomRegistrationForm(Interface):
    """Marker interface for registration form with radio buttons : MUA or Client
    """

class IUserType(model.Schema):

    user_type = schema.Choice(
        title = _(u"Are you a Makeup Artist or a Client?"),
        required = True,
        values = [_(u'Makeup Artist'), _(u'Client')]
    )
