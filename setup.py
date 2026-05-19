from setuptools import setup, find_packages

setup(
    name="quilean",
    version="1.0.0",
    description="A fast and smart Python CLI tool to organize, clean and manage files",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "questionary>=2.0.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "quilean = quilean.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
