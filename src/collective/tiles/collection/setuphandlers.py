# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from Products.GenericSetup.tool import UNKNOWN
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProducts(self):
        return [
            "collective.tiles.collection.mosaicsupport",
        ]

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and Add'on installation screen"""
        return [
            'collective.tiles.collection:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Note: context is the portal_setup tool.
    if context.getLastVersionForProfile('plone.app.mosaic:default') == UNKNOWN:
        return
    context.runAllImportStepsFromProfile(
        'collective.tiles.collection.mosaicsupport:default'
    )


def uninstall(context):
    """Uninstall script"""
    # Mark our optional mosaicsupport module as uninstalled.
    # Works fine, even when it was not installed, or is not available.
    context.unsetLastVersionForProfile(
        'collective.tiles.collection.mosaicsupport:default'
    )
