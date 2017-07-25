from plone.app.layout.viewlets import ViewletBase
from zope.component.hooks import getSite
from plone import api

def is_homepage(link):
    site = getSite()
    return link == site.absolute_url()

class MuaViewlet(ViewletBase):

    def get_role(self):
        user = api.user.get_current()

        if 'Client' in user.getRoles() or api.user.is_anonymous():
            if is_homepage(self.context.absolute_url()):
                return True

        return False

    def get_mua_page(self):
        site = getSite()

        return site.absolute_url() + '/@@view_mua'

class RegisterViewlet(ViewletBase):

    def is_anonymous(self):
        return api.user.is_anonymous() and is_homepage(self.context.absolute_url())

    def get_register_page(self):
        site = getSite()
        return site.absolute_url() + '/register'

