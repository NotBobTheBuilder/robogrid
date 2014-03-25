from setuptools import setup

setup(
    name="robogrid",
    version="0.5.0",
    description="A robot simulator for rectangular grids and mazes",
    url="https://github.com/NotBobTheBuilder/robogrid",
    author="Jack Wearden",
    author_email="jack@jackwearden.co.uk",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
    ],
    keywords="beginner robot grid maze",
    packages=["robogrid"],
    test_suite="tests",
)

