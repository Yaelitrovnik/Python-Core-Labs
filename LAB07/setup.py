from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Yael Litrovnik",
    description="Reusable Python utility package with greetings and timestamps.",
)
