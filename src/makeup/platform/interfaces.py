# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from makeup.platform import _
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import URI
from makeup.platform import utils
from plone import api
from plone.namedfile.field import NamedBlobImage


from zope import schema

def username_as_title():

    current = api.user.get_current()
    id = unicode(current.getProperty('id'), "utf-8")
    return id

# def mua_full_name():
#
#     current = api.user.get_current()
#     name = current.getProperty('fullname').encode('utf-8')
#     return name



class IMakeupPlatformLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IArtist(model.Schema):

    name = schema.TextLine(
        title=_(u"Full name"),
        required=True,
        # defaultFactory=mua_full_name
    )

    website = URI(
        title=_(u"Website"),
        required=False
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=False,
        constraint=utils.check_phone,
    )

    description = schema.Text(
        title=_(u"Describe yourself and your work in a few words"),
        required=False,
    )

    address = schema.TextLine(
        title=_(u"Studio address (e.g. strada Castanilor, 10, Bucuresti)"),
        required=False,
    )

class IClient(model.Schema):

    age = schema.Int(
        title=_(u"Age"),
        required=True,
        min=15,
        max=80,
    )

    self_image = NamedBlobImage(
        title=_(u"Upload an image of yourself with no makeup"),
        required=False
    )

    skin_type = schema.Choice(
        title=_(u"Skin type"),
        required=True,
        default=u'Normal',
        values=[_(u'Normal'), _(u'Combination'), _(u'Dry'), _(u'Oily')]
    )

    title = schema.TextLine(
        title=_(u"Username"),
        required=True,
        defaultFactory=username_as_title,
    )

    name = schema.TextLine(
        title=_(u"Full name"),
        required=True,
    )

class MinMax(object):
    pass

class DefaultMapLayers(object):
    pass
