from Products.Five import BrowserView
from plone import api
import googlemaps

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

    def has_photos(self):

        imgs = self.image_listing()
        if len(imgs) > 1:
            return True

    def mua_name(self):
        return 'Makeup Artist: {}'.format(self.context.name)

    def has_description(self):
        if self.context.description:
            return self.context.description

        return False

    def has_address(self):
        if self.context.address:
            return 'Studio address: {}'.format(self.context.address)

    def phone_nr(self):
        return 'Phone number: {}'.format(self.context.phone)

    def map_studio(self):
        results = {}

        gmaps = googlemaps.Client(key='AIzaSyDsPapEJ0GGmrkiJ5jXG1uKcvf8xk4hMw8')
        geocode_result = gmaps.geocode(self.context.address)

        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        results['lat'] = lat
        results['lng'] = lng

        # return 'http://maps.google.com/?q={},{}'.format(lat,lng)

        return results

class MuaListing(BrowserView):

    def mua_listing(self):

        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')

        brains = portal_catalog(
            portal_type="MakeupArtist",
            sort_on='created',
            sort_order='descending',
        )

        for brain in brains:

            mua = brain.getObject()

            if mua.website:
                website = mua.website
            else:
                website = "-"

            if mua.address:
                studio = mua.address
            else:
                studio = "-"


            container = mua.unrestrictedTraverse(mua.virtual_url_path())
            path = container.absolute_url()

            results.append({
                'name': mua.name,
                'phone': mua.phone,
                'site': website,
                'address': studio,
                'link': path,
            })

        return results
