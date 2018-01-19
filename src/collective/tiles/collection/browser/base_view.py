# -*- coding: utf-8 -*-
from collective.tiles.collection import _
from collective.tiles.collection.interfaces import ICollectionTileRenderer
from Products.Five.browser import BrowserView
from zope.interface import implementer


@implementer(ICollectionTileRenderer)
class BaseView(BrowserView):

    display_name = _('Base renderer')
