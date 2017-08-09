from Products.Five import BrowserView
from plone import api

class MuaView(BrowserView):
    """View a makeup artist page"""

    def image_listing(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())

        brains = portal_catalog(
            portal_type="Image",
            sort_on='created',
            sort_order='descending',
            path=current_path
        )

        for brain in brains:
            image = brain.getObject()
            results.append(image.absolute_url())

        return results
