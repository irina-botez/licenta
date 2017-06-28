from zope.formlib import form
from plone.app.users.browser.register import RegistrationForm
from makeup.platform.browser.interfaces import ICustomRegistrationForm, IUserType
from zope.interface import implements

class CustomRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(ICustomRegistrationForm)

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(CustomRegistrationForm, self).form_fields

        # Add a captcha field to the schema
        myfields += form.Fields(IUserType)
        # myfields['captcha'].custom_widget = CaptchaWidget

        # Perform any field shuffling here...

        # Return the fiddled fields
        return myfields
