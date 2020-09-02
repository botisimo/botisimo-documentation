# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme
import youtube

# -- Project information -----------------------------------------------------

project = 'Botisimo'
copyright = '2020, Botisimo'
author = 'Botisimo'

# -- YouTube Embed Directive -------------------------------------------------
youtube.setup()

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options
html_theme_options = {
  # 'typekit_id': 'hiw1hhg',
  # 'analytics_id': '',
  # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
  'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
  'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
  # 'display_version': True,  # Display the docs version
  # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
  "display_github": True, # Integrate GitHub
  "github_user": "botisimo", # Username
  "github_repo": "botisimo-documentation", # Repo name
  "github_version": "master", # Version
  "conf_py_path": "/", # Path in the checkout to the docs root
}

html_logo = 'images/botisimo-logo.png'

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
  'css/custom.css',
]
html_js_files = [
  'js/user-echo.js',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'
source_suffix = ['.rst', '.md']
html_show_sphinx = False
html_favicon = 'favicon.ico'