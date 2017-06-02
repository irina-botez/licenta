from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class PortfolioView(BrowserView):


    template = ViewPageTemplateFile('templates/portfolio_view.pt')
    def __call__(self):

        """"""
        self.template_var = getattr(self.context, 'template_var', 'World')
        return self.template()
