from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("src", "collective", "pgswidget", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "pgswidget", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "pgswidget", "docs", "CONTRIBUTORS.rst")).read())


setup(
    name='collective.pgswidget',
    version='0.1',
    description="Provides an integration of the PGS widget for Plone.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone Museum',
    author='Andre Goncalves',
    author_email='andre@intk.com',
    url='https://github.com/intk/collective.pgswidget/',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'plone.behavior',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
