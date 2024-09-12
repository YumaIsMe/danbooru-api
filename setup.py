from setuptools import setup, find_packages

setup(
    name='danbooru-api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A lightweight wrapper for the Danbooru API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yuma',
    author_email='',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
