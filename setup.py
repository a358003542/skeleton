#!/usr/bin/env python3
#-*-coding:utf-8-*-

from setuptools import setup ,find_packages

#+BEGIN_DELETE
import os.path
#anditional to make  a tar.gz file
import tarfile
with tarfile.open("skeleton.tar.gz", "w:gz") as tar:
    for name in ["setup.py","LICENSE","README.md","skeleton","tests"]:
        tar.add(name)
import os
os.replace('skeleton.tar.gz','skeleton/skeleton.tar.gz')
#+END_DELETE

import skeleton
import codecs

def long_description():
    with codecs.open('README.md', encoding='utf-8') as f:
        return f.read()

REQUIREMENTS = ['pytest-runner']

setup(
    name='skeleton',
    version=skeleton.__version__,
    description='make you create a python module quickly',
    url='https://github.com/a358003542/skeleton',
    long_description=long_description(),
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer = 'wanze',
    maintainer_email = 'a358003542@gmail.com',
    license='GPL 2',
    platforms = 'Linux',
    keywords =['skeleton','python'],
    classifiers = ['Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_data = {"skeleton":['skeleton.tar.gz'],},
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
    test_require=['pytest'],
    entry_points = {
        'console_scripts' :[ 'skeleton=skeleton.__main__:main',],
#       'gui_scripts':['xskeleton=skeleton.main:gui'],
        }
    )



