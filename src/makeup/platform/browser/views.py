from Products.Five import BrowserView
from plone import api
import googlemaps
import urllib
from Products.CMFCore.utils import getToolByName

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


class ClientView(BrowserView):
    def get_name(self):
        return self.context.name

    def get_img(self):
        if self.context.self_image:
            return self.context.self_image.filename
        return False

    def get_age(self):
        return self.context.age

    def get_skin_type(self):
        return self.context.skin_type

class MuaView(BrowserView):
    """View a makeup artist page"""
    def mua_email(self):
        to_check = self.context.name.encode('utf-8')
        membership = getToolByName(self.context, 'portal_membership')
        for member in membership.listMembers():
            if 'Makeup Artist' in member.getRoles():
                if to_check == member.getProperty('fullname'):
                    return member.getProperty('email')
        return 'Something is wrong'


    def is_logged_mua(self):
        if api.user.is_anonymous():
            return False
        return api.user.get_current().getProperty('fullname')

    def is_logged_client(self):

        user = api.user.get_current()

        if 'Client' in user.getRoles():
            return True

        return False

    def is_admin(self):
        return 'admin' == api.user.get_current()

    def has_site(self):
        if self.context.website:
            return self.context.website
        return False

    def get_client_page(self):
        user = api.user.get_current()
        user_id = user.getProperty('id');

        portal_catalog = api.portal.get_tool('portal_catalog')

        brains = portal_catalog(
            portal_type="Client",
            sort_on='created',
            sort_order='descending',
        )

        for brain in brains:
            client = brain.getObject()
            if client.title == user_id.encode('utf-8'):
                container = user.unrestrictedTraverse(client.virtual_url_path())
                return container.absolute_url()

        return '#'

    def get_client_name(self):
        user = api.user.get_current()
        return user.getProperty('fullname')

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
        results = []

        gmaps = googlemaps.Client(key='AIzaSyDsPapEJ0GGmrkiJ5jXG1uKcvf8xk4hMw8')
        geocode_result = gmaps.geocode(self.context.address)

        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        results.append({
            'lat': lat,
            'lng': lng,
        })

        # return 'http://maps.google.com/?q={},{}'.format(lat,lng)

        return results


class MuaListing(BrowserView):

    def get_current_rating(self, path):

        mua_page = urllib.urlopen(path)
        mua_page_html = mua_page.read()

        div = '<div class="current-rating" '
        closed_div = '</div>'

        rating = find_between(mua_page_html, div, closed_div)
        if rating == '' :
            rating = 0.0
        else:
            rating = round(float(rating[rating.find('>')+1:]),1)

        return rating

    def mua_listing(self):

        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')

        brains = portal_catalog(
            portal_type="MakeupArtist",
            sort_on='created',
            sort_order='descending',
            review_state='published'
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
                'rating': self.get_current_rating(path),
            })

        return results
