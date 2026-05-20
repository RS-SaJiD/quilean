from setuptools import setup, find_packages

setup(
    name="quilean",
    version="1.1.0",                    # Updated version
    description="A powerful Python CLI tool to organize, clean and manage files",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "questionary>=2.0.0",
        "colorama>=0.4.6",
        "toml>=0.10.2",
        "tqdm>=4.66.0"
    ],
    entry_points={
        "console_scripts": [
            "quilean = quilean.cli:main",
        ],
    },
    python_requires=">=3.8",
)
