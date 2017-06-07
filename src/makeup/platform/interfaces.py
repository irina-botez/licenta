# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from makeup.platform import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.supermodel import model
from zope.schema import URI

from plone.directives import form as directivesform
from plone.formwidget.multifile.widget import MultiFileFieldWidget
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
        required=True
    )

    email = schema.TextLine(
        title=_(u"Email"),
        required=True
    )

    website = URI(
        title=_(u"Website"),
        required=False
    )
