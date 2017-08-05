# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from makeup.platform import _
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import URI
from makeup.platform import utils

from plone import api
import unicodedata

from plone.namedfile.field import NamedBlobImage

def username_as_title():

    current = api.user.get_current()
    id = unicode(current.getProperty('id'), "utf-8")
    return id


class IMakeupPlatformLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IArtist(model.Schema):

    website = URI(
        title=_(u"Website"),
        required=False
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=True,
        constraint=utils.check_phone,
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

