from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cloudwatch-weather-station",
    version="0.0.1",
    description="AWS CloudWatch API Weather Station",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="tbd",
    author="Giorgio Carta",
    author_email="giorgiocarta@gmail.com",
    license="Apache2",
    packages=find_packages(),
    install_requires=[],
    test_suite="tests",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
