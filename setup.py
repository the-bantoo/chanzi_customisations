from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in chanzi_customisations/__init__.py
from chanzi_customisations import __version__ as version

setup(
	name='chanzi_customisations',
	version=version,
	description='Chanzi Ltd Customisations',
	author='Bantoo Accounting',
	author_email='devs@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
