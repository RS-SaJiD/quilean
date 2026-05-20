from setuptools import setup, find_packages

setup(
    name="quilean",
    version="1.1.0",
    description="A fast, smart and modern Python CLI tool to organize, clean and manage files",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RS-SaJiD",
    author_email="your.email@example.com",   # I can give you my email if you want.
    url="https://github.com/RS-SaJiD/quilean",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "questionary>=2.0.0",
        "colorama>=0.4.6",
        "toml>=0.10.2",
        "tomli>=2.0.0; python_version < '3.11'",
        "tqdm>=4.66.0",
    ],
    entry_points={
        "console_scripts": [
            "quilean = quilean.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Desktop Environment :: File Managers",
    ],
    keywords="file organizer, cleaner, duplicate finder, cli tool, productivity",
)
