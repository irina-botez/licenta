from zope.interface import Interface
from makeup.platform import _
from zope import schema

class ICustomRegistrationForm(Interface):
    """Marker interface for registration form with radio buttons : MUA or Client
    """

class IUserType(Interface):

    user_type = schema.Choice(
        title = _(u"Are you a Makeup Artist or a Client?"),
        required = True,
        default = u'Client',
        values = [_(u'Makeup Artist'), _(u'Client')]
    )


