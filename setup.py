from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    name='pylearning',

    version='3.2.2b1',

    description='Simple high-level library to use machine learning algorithms',
    long_description=long_description,

    url="https://github.com/amstuta/pylearning.git",

    author="Arthur Amstutz",
    author_email="arthur.amstutz@gmail.com",

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],

    keywords='machine learning data decision trees random forest nearest neighbours kmeans clustering',

    packages=find_packages(exclude=['contrib','docs','tests']),

    install_requires=['numpy','six','futures;python_version<"3"']

)
