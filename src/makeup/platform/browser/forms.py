from plone.app.users.browser.register import RegistrationForm, BaseRegistrationForm
from makeup.platform.browser.interfaces import ICustomRegistrationForm, IUserType
from zope.interface import implements

from z3c.form import field, button
from makeup.platform import _

from plone import api

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

    @button.buttonAndHandler(
        _(u'label_register', default=u'Next Step'), name='register'
    )
    def custom_register(self, action):

        data, errors = self.extractData()
        url = self.context.absolute_url()

        if data['user_type'] == 'Client':
            role='Client'
            redirect=url  + "/++add++Client"
        else:
            role='Makeup Artist'
            redirect = url + "/++add++MakeupArtist"

        properties = dict(
            fullname=data['fullname'],
        )

        user = api.user.create(email=data['email'], username=data['username'], properties=properties,)

        api.user.grant_roles(username=data['username'],
                             roles=[role,]
                             )

        self.request.response.redirect(redirect)

UserTypeView = UserType



