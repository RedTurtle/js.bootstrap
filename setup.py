from setuptools import setup, find_packages
import os

version = '1.3.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
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
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
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
            'bootstrap = js.boostrap:library',
            ],
        },
    )
