#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')

AUTHOR = 'nanang suryadi'
SITENAME = 'PyCon Indonesia 2017'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

from utils import filters

JINJA_FILTERS = {'foo': filters.printfoo, 'sidebar': filters.sidebar}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/fmdfrank'),
          ('linkedin', 'http://www.linkedin.com/pub/frank-valcarcel/3a/142/a92'),
          ('github', 'http://github.com/frankv'),
          ('bitbucket', 'http://bitbucket/frankv'),)

DEFAULT_PAGINATION = 3
POST_LIMIT = 3

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')


# Formatting for urls
# ARTICLE_DIR = 'blog'
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

ARCHIVES_URL = "blog"
ARCHIVES_SAVE_AS = "blog/index.html"

PAGE_DIR = 'pages'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

USE_FOLDER_AS_CATEGORY = True

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True


THEME = "themes/stellar"

STATIC_PATHS = ['images',
                'fonts',
                'css',
                'js',
                ]

import datetime
now = datetime.datetime.utcnow()
YEAR = now.strftime("%Y")
