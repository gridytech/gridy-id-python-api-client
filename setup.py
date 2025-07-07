# coding: utf-8

"""
    Gridy ID API

    <p> Gridy ID is a Multi-Factor authentication (MFA) API service & Authenticator application for Android, IOS, Windows, MacOS, Linux & Web . </p> <p>Use Gridy to replace your existing username/password authentication or Integrate Gridy ID into your adaptive authentication workflow in minutes using our API service and clients</p><p>When using the API Explorer, you will need to use the HMAC tool to generate the required headers for each request. <p>

"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "gridyapi_client"
VERSION = "0.5.0"
PYTHON_REQUIRES = ">= 3.7"
REQUIRES = [
    "urllib3 <= 1.24.9",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Gridy ID API Python client",
    author="gridy.io",
    author_email="support@gridy.io",
    url="https://gridy.io",
    keywords=["Gridy ID API Python client"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    &lt;p&gt; Gridy ID is a Multi-Factor authentication (MFA) API service &amp; Authenticator application for Android, IOS, Windows, MacOS, Linux &amp; Web . &lt;/p&gt; &lt;p&gt;Use Gridy to replace your existing username/password authentication or Integrate Gridy ID into your adaptive authentication workflow in minutes using our API service and clients&lt;/p&gt;&lt;p&gt;When using the API Explorer, you will need to use the HMAC tool to generate the required headers for each request. &lt;p&gt;
    """,  # noqa: E501
    package_data={"gridyapi_client": ["py.typed"]},
)
