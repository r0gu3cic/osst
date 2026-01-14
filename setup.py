from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="osst",
    version="0.1.0",
    description="Operating System Story Teller (OSST)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="r0gu3cic",
    packages=find_packages(),
    entry_points={"console_scripts": ["osst=osst.__main__:main"]},
    python_requires=">=3.8",
    install_requires=[
        "psutil",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
)
