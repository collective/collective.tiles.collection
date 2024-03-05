Changelog
=========

2.1.1 (unreleased)
------------------

- Avoid error when getting collection by UID.
  [daniele]


2.1.0 (2023-11-28)
------------------

- Add 'Show Description' option, default disabled to match rendering in previous versions of the tile.
  [fredvd]

- Plone 6 support: Refactor Mosaic addon support to use zcml condition instead of using the quickinstaller tool.
  [fredvd]

- Plone 6 support: Remove unused dependency on plone.formwidget.contenttree
  [fredvd]
  


2.0.0 (2022-09-14)
------------------

- Drop includeDependencies="." in order to work with pip
  [mamico]


1.3.1 (2021-09-27)
------------------

- Simplified and improved checks for registered renderers.
  [cekk]


1.3.0 (2021-09-10)
------------------

- Python3 compatibility.
  [cekk]
- Do not use templates registered from unavailable layers.
  [cekk]


1.2.1 (2021-05-07)
------------------

- Fix translations.
  [cekk]


1.2.0 (2019-01-09)
------------------

- Fixed permission to see empty tile collection message.
- Fixed vocabulary source for schema choice in tile collecton to support pam.
  [eikichi18]
- List of renderers is now sorted by title.
  [cekk]

1.1.3 (2018-08-21)
------------------

- Fix document outline [nzambello]
- Improved navigation experience when choosing the collection to use [daniele]  


1.1.2 (2018-08-02)
------------------
- Enable other content types to be chosen as the More link [daniele]
- Fixed a bug that hid a tile collection with no elements to display. If a user
  can edit the tiles, now he can see the empty tile.
  [arsenico13]
- Update some italian translations.
  [arsenico13]
- Fix templates for container styles in base view and in empty tile handling
  [nzambello]


1.1.1 (2018-03-06)
------------------
- Added Custom "more..." collection field
  [fdelia]

1.1 (11/10/2017)
----------------

- Production release
  [lucabel]

1.0a2 (2017-09-13)
------------------

- Removed unused css class
  [cekk]

1.0a1 (2017-03-31)
------------------

- Initial release.
  [cekk]

- Fix indentation on README.rst
