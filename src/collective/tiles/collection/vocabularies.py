# -*- coding: utf-8 -*-
from collective.tiles.collection.interfaces import ICollectionTileRenderer
from plone import api
from zope.component import getSiteManager
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import providedBy
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class CollectionRenderersVocabulary(object):
    def __call__(self, context):
        """
        Return a list of registered views for ICollectionTileRenderer
        """
        # copied from plone.api "get_view" method
        sm = getSiteManager()
        portal = api.portal.get()
        request = getRequest()

        available_views = sm.adapters.lookupAll(
            required=(providedBy(portal), providedBy(request)), provided=Interface
        )
        renderers = []
        for name, factory in available_views:
            if not ICollectionTileRenderer.implementedBy(factory):
                continue
            renderers.append(self.generateTerms(name=name, factory=factory))

        return SimpleVocabulary(sorted(renderers, key=lambda k: k.title))

    def generateTerms(self, name, factory):
        """
        Return a SimpleTerm with id and translated view name
        """
        human_name = getattr(factory, "display_name", name)
        return SimpleTerm(
            value=name, token=name, title=api.portal.translate(human_name)
        )


CollectionRenderersVocabularyFactory = CollectionRenderersVocabulary()
