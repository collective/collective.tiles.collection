# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from collective.tiles.collection import _
from plone.app.vocabularies.catalog import CatalogSource as CatalogSourceBase
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class CatalogSource(CatalogSourceBase):
    """
    Collection tile specific catalog source to allow targeted widget.
    Without this hack, validation doesn't pass
    """
    def __contains__(self, value):
        return True  # Always contains to allow lazy handling of removed objs


class ICollectionTileRenderer(Interface):
    """
    """


class ICollectiveTilesCollectionLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectionTileData(model.Schema):
    title = schema.TextLine(
        title=_('collection_tile_title',
                u'Tile title'),
        description=_(
            'collection_tile_title_help',
            u'The title of the tile. Leave blank to not show it.'),
        required=False,
    )

    collection_uid = schema.Choice(
        title=_(
            'collection_tile_collectionuid',
            u'Collection'),
        description=_(
            'collection_tile_collectionuid_help',
            u'Select a collection.'),
        source=CatalogSource(portal_type=('Topic', 'Collection')),
        required=True,
    )

    limit = schema.Int(
        title=_(
            'collection_tile_limit',
            u'Number of results'),
        required=False,
    )

    show_dates = schema.Bool(
        title=_(
            'collection_tile_showdates',
            u'Show dates'),
        required=False,
        default=False,
    )

    random = schema.Bool(
        title=_(u'Select random items'),
        description=_(u'If enabled, items will be selected randomly from the '
                      u'collection, rather than based on its sort order.'),
        required=False,
        default=False)

    show_more = schema.Bool(
        title=_(u'Show more... link'),
        description=_(u'If enabled, a more... link will appear in the footer '
                      u'of the tile, linking to the underlying '
                      u'Collection.'),
        required=False,
        default=True)

    show_more_label = schema.TextLine(
        title=_(u'Show more... label'),
        description=_(u'This value override default \"More...\" label.'),
        required=False,
        default=u'')

    show_more_collection_uid = schema.Choice(
        title=_(
            'collection_tile_showmorecollectionuid',
            u'Custom "more..." collection'),
        description=_(
            'collection_tile_showmorecollectionuid_help',
            u'Select an object in the site, for the "more..." link. '
            u'If empty, the link will be the collection.'),
        source=CatalogSource(portal_type=('Topic', 'Collection')),
        required=False,
    )

    exclude_context = schema.Bool(
        title=_(u'Exclude the Current Context'),
        description=_(
            u'If enabled, the listing will not include the current item the '
            u'tile is rendered for if it otherwise would be.'),
        required=True,
        default=True)

    renderer = schema.Choice(
        title=_(
            'collection_tile_renderer',
            u'Renderer'),
        description=_(
            'collection_tile_renderer_help',
            u'Select one of the available possible layouts for this tile.'),
        vocabulary='collective.tiles.collection.vocabulary.renderers',
        required=True,
        default='base_tile_collection_renderer',
    )

    css_class = schema.TextLine(
        title=_(
            'collection_tile_css_class',
            u'CSS class'),
        description=_(
            'collection_tile_css_class_help',
            u'Insert a list of additional css classes for this tile.'),
        required=False,
        default=u'',
    )
