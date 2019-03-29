from setuptools import setup, find_packages
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='couchbase-stress-testing',

    version='1.0.0',

    description='Couchbase stress test',
    long_description=long_description,

    url='https://github.com/Travix-International/couchbase-stress-testing',

    # Author details
    author='Travix Internationals',
    author_email='malsharbaji@travix.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='couchbase stress testing',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'couchbase',
        'requests'
    ],

    entry_points={
        'console_scripts': [
            'couchbase-stress-test=couchbase_stress_test.__init__:main',
        ],
    },
)