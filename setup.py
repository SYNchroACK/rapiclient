from setuptools import setup

setup(
    name='rapiclient',
    version='1.0.0',
    description='Python client for a RESTFULL API (e.g. Django REST Framework)',
    url='https://github.com/synchroack/rapiclient',
    author='SYNchroACK',
    author_email="synchroack@protonmail.ch",
    license='The Unlicense',
    packages=[
        'rapiclient',
    ],
    install_requires=[
        'requests',
    ],
    keywords=[
        "djangorestframework",
        "django",
        "REST",
        "API",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)