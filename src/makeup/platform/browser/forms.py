from plone.app.users.browser.register import RegistrationForm, BaseRegistrationForm
from makeup.platform.browser.interfaces import ICustomRegistrationForm, IUserType
from zope.interface import implements

from z3c.form import field, button
from makeup.platform import _

class UserType(RegistrationForm):

    implements(ICustomRegistrationForm)


    fields = field.Fields(IUserType)
    ignoreContext = True  # don't use context to get widget data
    def updateWidgets(self):
        super(UserType, self).updateWidgets()

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(UserType, self).form_fields

        return myfields

UserTypeView = UserType



