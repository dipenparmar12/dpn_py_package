#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description. Simple package, Designed for testing and learning, aimed at enhancing our workflow for increased efficiency'

setup(
    setup_requires=['pbr'],
    pbr=True,
)


# setup(
#     name='xh_py',
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         'dependencies==x.x.x',
#     ],
#     author='Dipen Parmar',
#     author_email='dipensavji@gmail.com',
#     description=DESCRIPTION,
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     url='https://github.com/dipenparmar12/py_package',
#     classifiers=[
#         'Development Status :: 3 - Alpha',
#         'Intended Audience :: Education',
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
# )