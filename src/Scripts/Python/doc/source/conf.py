# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
source_path = os.path.abspath('../../')
# print(source_path)
sys.path.insert(0, source_path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LabVIEW module'
copyright = '2023, ViTechnologies'
author = 'ViTechnologies'
version = "alpha 0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #'sphinx_rtd_theme',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',    
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']


html_theme_options = { # see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
    'logo_only': False,
    'prev_next_buttons_location': "bottom",
}

