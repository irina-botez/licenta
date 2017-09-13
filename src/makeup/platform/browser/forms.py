# -*- coding: utf-8 -*-
from plone.app.users.browser.register import RegistrationForm
from makeup.platform.browser.interfaces import ICustomRegistrationForm, IUserType
from zope.interface import implements
from z3c.form import field, button
from makeup.platform import _
from plone import api
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from Products.statusmessages.interfaces import IStatusMessage


class UserType(RegistrationForm):

    implements(ICustomRegistrationForm)

    formErrorsMessage = _('There were errors.')

    fields = field.Fields(IUserType)
    ignoreContext = True  # don't use context to get widget data
    def updateWidgets(self):
        super(UserType, self).updateWidgets()

    def validate_registration(self, action, data):

        username = data.get('username')
        password = data.get('password')
        password_ctl = data.get('password_ctl')

        membership = getToolByName(self.context, 'portal_membership')
        for member in membership.listMembers():
            if member.getUserName() == username:
                err_str = _(u'Username already in use. Please choose another username')
                IStatusMessage(self.request).addStatusMessage(err_str, type="error")
                return False

        if password != password_ctl:
            err_str = _(u'Passwords do not match.')
            IStatusMessage(self.request).addStatusMessage(err_str, type="error")
            return False

        return True



    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(UserType, self).form_fields

        return myfields

    @button.buttonAndHandler(
        _(u'label_register', default=u'Next Step'), name='register'
    )
    def custom_register(self, action):

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        acl_users = getToolByName(self.context, 'acl_users')
        url = self.context.absolute_url()


        data, errors = self.extractData()

        if self.validate_registration(action, data) == False:
            self.request.response.redirect(url + '/register')
        else:

            if data['user_type'] == 'Client':
                role='Client'
                redirect=url  + "/all-clients/++add++Client"
            else:
                role='Makeup Artist'
                redirect = url + "/all-artists/++add++MakeupArtist"

            properties = dict(
                fullname=data['fullname'],
            )

            user = api.user.create(email=data['email'], username=data['username'], password=data['password'], properties=properties)

            api.user.grant_roles(username=data['username'],
                                 roles=[role, 'Reviewer']
                                 )

            if role == 'Makeup Artist':
                api.user.grant_roles(username=data['username'],roles=['Contributor'])

            acl_users = getToolByName(self, 'acl_users')

            usr = data['username'].encode('utf-8')

            # auto-login after form submission + redirect to add page
            acl_users.session._setupSession(usr, self.request.response)
            self.request.response.redirect(redirect)

UserTypeView = UserType



