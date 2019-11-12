from setuptools import setup, find_packages
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


install_requires = [
    'pandas',
]

setup(
    name='kuma',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='A package which adds new functions to a pandas dataframe or series.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='M3, inc.',
    url='https://github.com/m3dev/kuma',
    license='MIT License',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=[],
    test_suite='test',
    classifiers=['Programming Language :: Python :: 3.6'],
)
