#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Avel GUÉNIN--CARLUT'
SITENAME = 'Polarisation & mondialisation en France'
SITEURL = 'https://avelguenin.github.io/france-polarisation-code/'
PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'FR'

THEME = "/home/avel/.pelican/pelican-themes/pelican-alchemy/alchemy"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Mon site personnel', 'http://enkitex.wordpress.com/'),
         ("Équipe Cliométrie et Complexité", "http://www.ixxi.fr/recherche/cliometrie-et-complexite"),
         )
# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
