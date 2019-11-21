# -*- coding: utf-8 -*-
from Acquisition import aq_parent
from plone.app.event import _
from plone.event.interfaces import IEventAccessor
from plone.event.interfaces import IOccurrence
from plone.event.interfaces import IRecurrenceSupport
from plone.memoize import view
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from zope.contentprovider.interfaces import IContentProvider


JAVASCRIPT_HTML = '<script type="text/javascript" src="https://z.jewellabs.net/pgs_widget/pgs-widget-1.js"></script>'
USER_REVIEWS_HTML = '<div class="tf-widget" data-icin="%s" data-pgs-key="%s" data-show-reactions="1" data-allow-reactions="1" data-show-reviews="1" data-author-fields="{}" data-collapsed="1"></div>'

class PGSwidgetView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def has_icin(self):
        return True

    @property
    def get_user_reviews(self):
        return ""

