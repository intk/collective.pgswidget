# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface

class IPGSWidgetControlPanel(Interface):
    api_key = schema.TextLine(
        title=u'API key',
        required=False
    )

    widget_url = schema.TextLine(
        title=u'Widget url (Javascript)',
        required=False
    )

class PGSWidgetControlPanelForm(RegistryEditForm):
    schema = IPGSWidgetControlPanel
    label = u'PGS Widget control panel'

class PGSWidgetControlPanelView(ControlPanelFormWrapper):
    form = PGSWidgetControlPanelForm
