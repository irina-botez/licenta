from zope.formlib import form
from plone.app.users.browser.register import RegistrationForm, BaseRegistrationForm
from makeup.platform.browser.interfaces import ICustomRegistrationForm, IUserType
from zope.interface import implements

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from z3c.form import field, button
from plone.z3cform.layout import wrap_form
from z3c.form.browser.radio import RadioFieldWidget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from makeup.platform import _

class UserType(form.Form, RegistrationForm):

    implements(ICustomRegistrationForm)


    fields = field.Fields(IUserType)
    fields['user_type'].widgetFactory = RadioFieldWidget
    ignoreContext = True  # don't use context to get widget data
    label = _(u"Send a deal alert")
    description = _(
        u"At Pistebook we want to make sure you find the ski holiday deal that you are looking for. So we've tried not to over complicate the information we need from you, this means you don't miss out on a great deal by being too specific on your requirements.")

    # template = ViewPageTemplateFile('templates/register_form.pt')

    def updateWidgets(self):
        super(UserType, self).updateWidgets()

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(UserType, self).form_fields

        myfields += form.Fields(IUserType)

        return myfields

UserTypeView = UserType



