=========================
collective.pgswidget
=========================

Provides an integration of the PGS widget user reviews (https://z.jewellabs.net/pgs_widget/pgs-widget-manual.html) for Plone.

Currently tested with
---------------------

* Plone-5.0.x [andreesg]
* Plone-5.1.x [andreesg]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.pgswidget.interfaces.IPGSwidget" />
    ...
  </property>
