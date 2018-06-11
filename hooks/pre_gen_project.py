#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

# Validate package name.
PACKAGE_REGEX = r'^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+[0-9a-z_]$'

package_name = '{{ cookiecutter.package_name }}'

if not re.match(PACKAGE_REGEX, package_name):
  print('ERROR: %s is not a valid Java package!' % package_name)
  # exits with status 1 to indicate failure
  sys.exit(1)

# Validate project name
project_name = '{{ cookiecutter.project_name }}'
if len(project_name) > 60:
  print('Project Name is too long. Max 60 char.!')
  # exits with status 1 to indicate failure
  sys.exit(1)