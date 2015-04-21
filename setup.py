from setuptools import setup, find_packages
import os

version = '3.3.4'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'bootstrap', 'test_bootstrap.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.bootstrap',
    version=version,
    description="fanstatic twitter bootstrap.",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic twitter bootstrap redturtle',
    author='RedTurtle Developers',
    url='https://github.com/RedTurtle/js.bootstrap',
    author_email='sviluppoplone@redturtle.it',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap = js.bootstrap:library',
            ],
        },
    )
