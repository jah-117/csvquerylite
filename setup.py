from setuptools import setup, find_packages

setup(
    name="csvquerylite",
    version="0.1.5",
    author="Jahfar Muhammed",
    author_email="jahfarbinmuhammed117@gmail.com",
    description="Run SQL-like queries on CSV files using a simple Python library or CLI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jah-117/csvquerylite",  # replace with your actual repo
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "csvquerylite=csv_query.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas"
    ],
    include_package_data=True,
)
