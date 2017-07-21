from zope.interface import Interface
from makeup.platform import _
from zope import schema
from makeup.platform import utils

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

    password_1 = schema.Password(
        title = _(u"Enter a password"),
        required = True,
        constraint = utils.check_password
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=True,
        constraint=utils.check_phone
    )

