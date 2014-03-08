# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-request-mock',
    version='0.1.4',
    author=u'Valérian Saliou',
    author_email='valerian@valeriansaliou.name',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/valeriansaliou/django-request-mock',
    license='MIT - http://opensource.org/licenses/mit-license.php',
    description='Create a Django request object that mocks a real one.',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
