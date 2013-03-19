import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='gears-scss',
    version='0.1.0',
    url='https://github.com/wbond/gears-scss',
    license='MIT',
    author='Will Bond',
    author_email='will@wbond.net',
    description='Python/libsass-based SCSS compiler for Gears',
    long_description=read('README.rst'),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
    ],
    install_requires=[
        "sass >= 0.1.2"
    ],
)