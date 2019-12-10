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

import json

# Product dependencies
from .error import raise_error
from .api_connection import APIConnection
from zope.component import getMultiAdapter


import dateutil.parser


class PGSreviewView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = IPGSwidget(self.context)

        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IPGSWidgetControlPanel)
        self.plone = getMultiAdapter((self.context, self.request), name="plone")

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

    def generate_stars(self, review):
        rating = review.get('rating', '')

        if rating:
            rating_html = []
            total_starts = rating / 20
            remaining_starts = 5 - total_starts

            for i in range(total_starts):
                rating_html.append("<i class='fa fa-star'></i>")

            if remaining_starts:
                for i in range(remaining_starts):
                    rating_html.append("<i class='fa fa-star-o'></i>")

            return "<span class='stars'>"+"".join(rating_html)+"</span>"
        else:
            return ""

    def generate_author_name(self, review):
        author = review.get('author', '')
        if author:
            author_name = ""
            first_name = author.get('first_name')
            last_name = author.get('last_name')
            
            if first_name:
                author_name = "%s" %(first_name)

            if last_name:
                author_name = "%s %s" %(author_name, last_name)

            author_name = author_name.strip()
            return author_name
        else:
            return ""

    def generate_review_date(self, review):
        date = review.get('published_at', '')
        if date:
            date_datetime = dateutil.parser.parse(date)
            return self.plone.toLocalizedTime(date_datetime)
        else:
            return ""

    def generate_theater(self, review):
        theater = review.get('location_name', '')
        if theater:
            theater_name = "- %s" %(theater)
            return theater_name
        else:
            return ""

    def generate_description(self, review):
        description = review.get('content', '')
        return description

    def build_reviews_html(self, reviews):

        review_template = "<li class='reactionsCard'><div class='title'>%s<span class='author'>%s</span><span class='theater'>%s</span><div class='timestamp'>%s</div></div><p class='review-description'>%s</p></li>"

        reviews_html = []

        if reviews:
            total_reviews = len(reviews)
            reviews_title = "Reacties (%s)" %(total_reviews)

            for review in reviews:
                if review:
                    starts = self.generate_stars(review)
                    author = self.generate_author_name(review)
                    review_date = self.generate_review_date(review)
                    theater = self.generate_theater(review)
                    description = self.generate_description(review)

                    new_review = review_template %(starts, author, theater, review_date, description)

                    reviews_html.append(new_review)
                else:
                    pass
            return "<h1>"+reviews_title+"</h1><ul id='reactionsList'>"+"".join(reviews_html)+"</ul>"
        else:
            return ""

    def get_reviews(self):
        icin = self.get_icin
        api_token = self.get_key
        api_settings = {"api_key": api_token}

        api_connection = APIConnection(api_settings)
        
        try:
            reviews = api_connection.get_reviews(icin=icin)
            reviews_html = self.build_reviews_html(reviews)
            return reviews_html
        except:
            raise


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



