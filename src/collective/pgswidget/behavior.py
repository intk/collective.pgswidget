#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent
from zope.interface import alsoProvides
from zope.interface import implements
from zope.lifecycleevent import modified
from five import grok
from zope.interface import implementer
from zope.component import adapter
from zope.interface import Interface
from zope.interface import provider
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import implementer
from zope.component import adapter
from plone.supermodel import model
from zope import schema
from collective.pgswidget import _
from plone.indexer.decorator import indexer
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.app.z3cform.widget import AjaxSelectFieldWidget



@provider(IFormFieldProvider)
class IPGSwidget(model.Schema):
    """Interface for PGSwidget behavior."""

    # PGSwidget fieldset
    model.fieldset(
        'pgswidget',
        label=_(u'User reviews', default=u'User reviews'),
        fields=['icin'],
    )

    icin = schema.TextLine(
        title=_(u'ICIN number', default=u'ICIN number'),
        required=False
    )



        





