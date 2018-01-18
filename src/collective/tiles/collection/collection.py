# -*- coding: utf-8 -*-
from plone import api
from plone import tiles
from plone.memoize import view

import random


class CollectionTile(tiles.PersistentTile):
    """
    A tile that show collection results
    """

    @property
    @view.memoize
    def collection(self):
        collection_uid = self.data.get('collection_uid')
        if not collection_uid:
            return None
        return api.content.get(UID=collection_uid)

    @property
    @view.memoize
    def show_more_collection(self):
        show_more_collection_uid = self.data.get('show_more_collection_uid')
        if not show_more_collection_uid:
            return None
        return api.content.get(UID=show_more_collection_uid)

    def results(self):
        if self.data.get('random', False):
            return self._random_results()
        else:
            return self._standard_results()

    def _standard_results(self):
        results = []
        collection = self.collection
        if collection is not None:
            context_path = '/'.join(self.context.getPhysicalPath())
            exclude_context = self.data.get('exclude_context', False)
            limit = self.data.get('limit', None)
            if limit and limit > 0:
                # pass on batching hints to the catalog
                results = collection.queryCatalog(
                    batch=True, b_size=limit + exclude_context)
                results = results._sequence
            else:
                results = collection.queryCatalog()
            if exclude_context:
                results = [
                    brain for brain in results
                    if brain.getPath() != context_path]
            if limit and limit > 0:
                results = results[:limit]
        return results

    def _random_results(self):
        # intentionally non-memoized
        results = []
        collection = self.collection
        if collection is not None:
            context_path = '/'.join(self.context.getPhysicalPath())
            exclude_context = self.data.get('exclude_context', False)
            results = collection.queryCatalog(sort_on=None)
            if results is None:
                return []
            if exclude_context:
                results = [
                    brain for brain in results
                    if brain.getPath() != context_path]
            limit = self.data.get('limit') or 0
            if not limit:
                limit = len(results)
            limit = min(len(results), limit)
            if len(results) < limit:
                limit = len(results)
            results = random.sample(results, limit)
        return results
