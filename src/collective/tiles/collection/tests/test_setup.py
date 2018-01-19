# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.tiles.collection.testing import COLLECTIVE_TILES_COLLECTION_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.tiles.collection is properly installed."""

    layer = COLLECTIVE_TILES_COLLECTION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.tiles.collection is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.tiles.collection'))

    def test_browserlayer(self):
        """Test that ICollectiveTilesCollectionLayer is registered."""
        from collective.tiles.collection.interfaces import (
            ICollectiveTilesCollectionLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveTilesCollectionLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_TILES_COLLECTION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.tiles.collection'])

    def test_product_uninstalled(self):
        """Test if collective.tiles.collection is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.tiles.collection'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTilesCollectionLayer is removed."""
        from collective.tiles.collection.interfaces import ICollectiveTilesCollectionLayer  # noqa
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveTilesCollectionLayer, utils.registered_layers())   # noqa
