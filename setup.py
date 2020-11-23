import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AirDataUAV",
    version="0.0.1",
    author="Jan-Hendrik Ewers",
    author_email="jh.ewers@gmail.com",
    description="A nice interface to AirDataUAV CSV files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iwishiwasaneagle/AirDataUAV",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
