from plone.app.layout.viewlets import ViewletBase
from zope.component.hooks import getSite

class MuaViewlet(ViewletBase):

    def get_mua_page(self):
        site = getSite()

        return site.absolute_url() + '/@@view_mua'

