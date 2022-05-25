#!/usr/bin/env python3

# stdlib
import os
import re
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath(".."))

# 3rd party
from __pkginfo__ import __author__, __copyright__, __version__, modname

project = modname
slug = re.sub(r'\W+', '-', modname.lower())
release = __version__
author = __author__
language = "en"

source_suffix = ".rst"
exclude_patterns = []

suppress_warnings = ["image.nonlocal_uri"]
pygments_style = "default"

version = f"{modname} {__version__}"
copyright = (
		f"{__copyright__}. License GPLv3+: GNU GPL version 3 or later "
		f"<http://gnu.org/licenses/gpl.html>\n\n"
		"This is free software: you are free to change and redistribute it under certain conditions.\n\n"
		"There is NO WARRANTY, to the extent permitted by law."
		)

master_doc = "manpage"
man_pages = [("manpage", slug, modname, [author], 1)]
