# -*- coding: utf-8 -*-
import codecs
import re
from os import path
from distutils.core import setup
from setuptools import find_packages


def read(*parts):
    return codecs.open(path.join(path.dirname(__file__), *parts),
                       encoding='utf-8').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-superform',
    version=find_version('django_superform', '__init__.py'),
    author=u'Stephen Odara',
    author_email='darahsten@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/darahsten/django-superform',
    license='BSD licence, see LICENSE file',
    description='So much easier handling of formsets.',
    long_description=u'\n\n'.join((
        read('README.rst'),
        read('CHANGES.rst'))),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False,
)
