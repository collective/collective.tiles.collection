# -*- coding: utf-8 -*-
from collective.tiles.collection.interfaces import ICollectionTileRenderer
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.customerize import registration
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class CollectionRenderersVocabulary(object):

    def __call__(self, context):
        views = registration.getViews(IBrowserRequest)
        renderers = filter(self.isCollectionRenderer, views)
        return SimpleVocabulary(map(self.generateTerms, renderers))

    def isCollectionRenderer(self, view):
        """
        Filter only views that implements a certain interface.
        Also checks if the use can access to that view.
        An user can't access to the view for different reasons:
        - invalid permissions
        - invalid browserlayer (product with the view not installed)
        """
        if not ICollectionTileRenderer.implementedBy(view.factory):
            return False
        # try to access this view. If the use can't access the view,
        # return False
        portal = api.portal.get()
        request = getRequest()
        try:
            view = api.content.get_view(
                context=portal,
                name=view.name,
                request=request)
            return view and True or False
        except InvalidParameterError:
            return False

    def generateTerms(self, view):
        """
        Return a SimpleTerm with id and translated view name
        """
        factory = view.factory
        name = view.name
        human_name = getattr(factory, 'display_name', name)
        request = getRequest()
        return SimpleVocabulary.createTerm(
            name,
            name,
            translate(human_name, context=request),
        )


CollectionRenderersVocabularyFactory = CollectionRenderersVocabulary()
