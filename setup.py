from setuptools import setup, find_packages

setup(
    name="datagraph",  # This is the name on PyPI
    version="0.1.0",  # Update this for each new release
    author="J Joshua Haniel",
    author_email="j06haniel@gmail.com",
    description="A simple data visualization library using matplotlib and pandas.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joshuahanielgts/datagraph",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
