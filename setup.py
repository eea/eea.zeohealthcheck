from setuptools import setup, find_namespace_packages

setup(name='eea.zeohealthcheck',
      version='2.0',
      description='Check database connection',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Dragos Chirila (Eaudeweb)',
      author_email='dragos.chirila@eaudeweb.ro',
      url='https://github.com/DragosChirila/eea.zeohealthcheck.git',
      license='GPL',
      packages=find_namespace_packages(include=['eea.*']),
      python_requires='>=3.7',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
