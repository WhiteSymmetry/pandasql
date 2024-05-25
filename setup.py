from distutils.core import setup
from setuptools import find_packages


version = "0.0.1"
# Extract version from CHANGES.md
with open("./CHANGES.md", "r") as file:
    for line in file:
        if line.strip():
            version = line.strip()
            break
        
setup(
    name="pandasql-lts",
    version=version,
    author="Greg Lamp",
    author_email="greg@yhathq.com",
    maintainer="Bui Hoang Tu",
    maintainer_email="bhtu.work@gmail.com",
    url="https://github.com/BuiHoangTu/pandasql/tree/release",
    license="MIT",
    packages=find_packages(),
    package_dir={"pandasql": "pandasql"},
    package_data={"pandasql": ["data/*.csv"]},
    description="sqldf for pandas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["numpy", "pandas", "sqlalchemy"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)
