from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-countapicalls',
	version=version,
	description="Count API Calls",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='abulte',
	author_email='alexandre@bulte.net',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.countapicalls'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
		countapicalls=ckanext.countapicalls.plugin:CountAPICallsPlugin
	    
	    [paste.paster_command]
        initdb = ckanext.countapicalls.commands:InitDB
	# Add plugins here, eg
	# myplugin=ckanext.countapicalls:PluginClass
	""",
)
