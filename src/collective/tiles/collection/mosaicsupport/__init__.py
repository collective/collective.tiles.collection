# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces.installable import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    """This hides zope2 profile from the quick installer tool and plone cpanel"""

    _hidden = [
        u"collective.tiles.collection.mosaicsuppport:default",
    ]

    def getNonInstallableProducts(self):
        return self._hidden

    def getNonInstallableProfiles(self):
        return self._hidden