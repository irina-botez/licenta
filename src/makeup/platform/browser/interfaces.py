from zope.interface import Interface
from makeup.platform import _
from plone.supermodel import model
from zope import schema

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from z3c.form import form, field, button
from plone.z3cform.layout import wrap_form
from z3c.form.browser.radio import RadioFieldWidget

users = SimpleVocabulary(
    [SimpleTerm(value=u'M', title=_(u'Makeup Artist')),
     SimpleTerm(value=u'C', title=_(u'Client'))]
    )

class ICustomRegistrationForm(Interface):
    """Marker interface for registration form with radio buttons : MUA or Client
    """

class IUserType(Interface):

    user_type = schema.Choice(
        title = _(u"Are you a Makeup Artist or a Client?"),
        required = True,
        vocabulary = users
        # values = [_(u'Makeup Artist'), _(u'Client')]
    )

class UserType(form.Form):

    fields = field.Fields(IUserType)
    fields['user_type'].widgetFactory = RadioFieldWidget
    ignoreContext = True  # don't use context to get widget data
    label = _(u"Send a deal alert")
    description = _(
        u"At Pistebook we want to make sure you find the ski holiday deal that you are looking for. So we've tried not to over complicate the information we need from you, this means you don't miss out on a great deal by being too specific on your requirements.")

    # template = ViewPageTemplateFile('templates/register_form.pt')

    def updateWidgets(self):
        super(UserType, self).updateWidgets()
        # self.widgets['adults_no'].size = 2

UserTypeView = UserType
