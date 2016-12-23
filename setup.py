from setuptools import setup, find_packages
import os

setup(name='eea.zeohealthcheck',
      version='1.0',
      description='Check database connection',
      classifiers=[
        "Programming Language :: Python",
      ],
      author='Dragos Chirila (Eaudeweb)',
      author_email='dragos.chirila@eaudeweb.ro',
      url='https://svn.eionet.europa.eu/repositories/Zope/trunk/eea.zeohealthcheck',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
)
