#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    setup_requires=['pbr'],
    pbr=True,
)


# setup(
#     name='your_package',
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         'dependencies==x.x.x',
#     ],
#     author='Dipen Parmar',
#     author_email='dparmar@xerohome.com',
#     description='Simple package, Designed for testing and learning, aimed at enhancing our workflow for increased efficiency ',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     url='https://github.com/xerohome/your_package',
#     classifiers=[
#         'Development Status :: 3 - Alpha',
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
# )