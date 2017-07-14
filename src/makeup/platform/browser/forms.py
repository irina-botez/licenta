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
        _(u'label_register', default=u'Register'), name='register'
    )
    def custom_register(self, action):

        data, errors = self.extractData()

        if data['user_type'] == 'Client':
            role='Client'
        else:
            role='Makeup Artist'

        properties = dict(
            fullname=data['fullname'],
        )

        user = api.user.create(email=data['email'], username=data['username'], properties=properties,)

        # api.user.grant_roles(username='jane',
        #                      roles=['Reviewer', 'SiteAdministrator']
        #                      )

        # import pdb;pdb.set_trace()

UserTypeView = UserType



