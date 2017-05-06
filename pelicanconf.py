#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'visibilityspots'
SITENAME = 'Gezinsbond Humbeek'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'nl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/pelican-gezinsbond"

SIDEBAR_DIGEST = 'Dit is de webstek van de Gezinsbond afdeling Humbeek'
FAVICON = '/theme/images/favicon.ico'
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
    ('HOME', SITEURL),
    ('TWEEDEHANDSBEURS', '/pages/tweedehandsbeurs.html'),
    ('CONTACT', '/pages/contact.html'),
    )
