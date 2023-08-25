#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-widget-tweaks",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    author="Mikhail Korobov",
    author_email="kmike84@gmail.com",
    url="https://github.com/jazzband/django-widget-tweaks",
    description="Tweak the form field rendering in templates, not in python-level form definitions.",
    long_description=open("README.rst").read() + "\n\n" + open("CHANGES.rst").read(),
    long_description_content_type="text/x-rst",
    license="MIT license",
    python_requires=">=3.8",
    requires=["django (>=2.2)"],
    packages=["widget_tweaks", "widget_tweaks.templatetags"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
