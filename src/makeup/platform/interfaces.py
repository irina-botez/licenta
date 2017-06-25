# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from makeup.platform import _
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import URI
from makeup.platform import utils

from plone.namedfile.field import NamedBlobImage




class IMakeupPlatformLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IArtist(model.Schema):

    title = schema.TextLine(
        title=_(u"Name"),
        required=True
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=True,
        constraint=utils.check_phone
    )

    email = schema.TextLine(
        title=_(u"Email"),
        required=True,
        constraint=utils.validate_email
    )

    website = URI(
        title=_(u"Website"),
        required=False
    )

class IClient(model.Schema):

    title = schema.TextLine(
        title=_(u"Name"),
        required=True
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False
    )

    phone = schema.TextLine(
        title=_(u"Phone number"),
        required=True,
        constraint=utils.check_phone
    )

    email = schema.TextLine(
        title=_(u"Email"),
        required=True,
        constraint=utils.validate_email
    )

    self_image = NamedBlobImage(
        title=_(u"Upload an image of yourself with no makeup"),
        required=False
    )

