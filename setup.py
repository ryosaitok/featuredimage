from setuptools import find_packages, setup

setup(
    name='featuredimg',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Click~=7.0',
        'Pillow>=6.2,<8.4',
        'requests~=2.22.0',
    ],
    entry_points={
        'console_scripts': [
            'featuredimg=featuredimg.core:cli'
        ]
    }
)
