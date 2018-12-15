import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riksbank",
    version="0.0.1",
    author="Thomas Petig",
    author_email="thomas@petig.eu",
    description="Read from riksbankens SOAP API to pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thpe/riksbank",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
