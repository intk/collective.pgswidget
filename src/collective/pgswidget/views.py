# -*- coding: utf-8 -*-
from Acquisition import aq_parent
from plone.app.event import _

from plone.event.interfaces import IEventAccessor
from plone.event.interfaces import IOccurrence
from plone.event.interfaces import IRecurrenceSupport
from plone.registry.interfaces import IRegistry
from plone.registry.interfaces import IRegistry
from collective.pgswidget.behavior import IPGSwidget
from collective.pgswidget.controlpanel import IPGSWidgetControlPanel

from plone.memoize import view
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter

from zope.component import getUtility


class PGSwidgetView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = IPGSwidget(self.context)

        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IPGSWidgetControlPanel)

    @property
    def get_icin(self):
        return getattr(self.data, 'icin', None)

    @property
    def get_key(self):
        api_key = getattr(self.settings, 'api_key', None)
        return api_key

    @property
    def get_widget_url(self):
        api_key = getattr(self.settings, 'widget_url', None)
        return api_key



