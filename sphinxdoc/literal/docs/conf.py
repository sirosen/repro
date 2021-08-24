import os
import sys

sys.path.insert(0, os.path.abspath(".."))

nitpick_ignore_regex = [
    (r"py:.*", r"thirdpartything\..*"),
]

project = "reproproj"
copyright = "2021, me"
author = "me"
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
exclude_patterns = ["_build"]
html_theme = "alabaster"
html_static_path = ["_static"]
