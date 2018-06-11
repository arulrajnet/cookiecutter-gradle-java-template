#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

project_name = '{{ cookiecutter.project_name }}'.strip()
package_name = '{{ cookiecutter.package_name }}'.strip()

package_path = package_name.replace('.', '/')
os.makedirs('src/main/java/%s' % package_path)
os.makedirs('src/test/java/%s' % package_path)
os.rename('src/main/java/App.java.template', 'src/main/java/%s/%s' % (package_path, 'App.java'))
os.rename('src/test/java/AppTest.java.template', 'src/test/java/%s/%s' % (package_path, 'AppTest.java'))
