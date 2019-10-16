from setuptools import setup, find_packages

setup(
    name='convert',
    version='0.1.1',
    author='Will Thompson',
    author_email='wkt@northwestern.edu',
    maintainer='Will Thompson',
    maintainer_email='wkt@northwestern.edu',
    url='https://github.com/rs-kellogg/corelogic',
    packages=find_packages(include=['convert', 'convert.*']),
    install_requires=[
        'pymongo'
      ],
    extras_require={
        'interactive': ['jupyter']
    },
    entry_points={
        'console_scripts': ['bson2json=convert.bson:main'
                            ]
    },
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
)
