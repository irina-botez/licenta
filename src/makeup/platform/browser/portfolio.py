from Products.Five import BrowserView
from plone.autoform.view import WidgetsView

from makeup.platform.interfaces import IPortfolio

from zope.interface.interfaces import IMethod


#Tests
from zope.component import getUtility
from plone.namedfile.field import NamedFile, NamedImage, NamedBlobFile, NamedBlobImage

from plone.supermodel.interfaces import IFieldExportImportHandler
from plone.supermodel.interfaces import IFieldNameExtractor
from plone.supermodel.utils import prettyXML
import zope.schema
from makeup.platform.interfaces import IPortfolio

from lxml import etree

class MyView(WidgetsView):
    schema = IPortfolio


class PortfolioView(BrowserView):

    def image_listing(self):

        filename_list={}

        for name, desc in IPortfolio.namesAndDescriptions():

            # import pdb;pdb.set_trace()
            # value = getattr(self.context, name)
            # if IMethod.providedBy(desc):
            #     value = value()
            # for i in value:
            #
            #     # fieldType = IFieldNameExtractor(i)()
            #     # handler = getUtility(IFieldExportImportHandler, name=fieldType)
            #     # element = handler.write(field, u'dummy', fieldType)  # doctest: +ELLIPSIS
            #     filename_list.append(i.__getattribute__('filename'))
            #
            # return value

            fields = zope.schema.getFields(IPortfolio)
            return fields
            # i=0
            #
            # for key, value in fields.iteritems():
            #     filename_list[i] = value
            # import pdb;pdb.set_trace()
            # return filename_list

    def new_try(self):
        for name, desc in IPortfolio.namesAndDescriptions():

            value = getattr(self.context, name)
            import pdb;pdb.set_trace()






