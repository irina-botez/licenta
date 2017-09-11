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

def mua_full_name():

    current = api.user.get_current()
    name = unicode(current.getProperty('fullname'), "utf-8")
    return name



class IMakeupPlatformLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IArtist(model.Schema):

    name = schema.TextLine(
        title=_(u"Full name"),
        required=True,
        defaultFactory=mua_full_name
    )

    website = URI(
        title=_(u"Website"),
        required=False
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=True,
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

    self_image = NamedBlobImage(
        title=_(u"Upload an image of yourself with no makeup"),
        required=False
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=True,
        constraint=utils.check_phone,
    )

    title = schema.TextLine(
        title=_(u"Client username"),
        required=True,
        defaultFactory=username_as_title,
    )

class MinMax(object):
    pass

class DefaultMapLayers(object):
    pass
