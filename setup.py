from setuptools import setup, find_packages

setup(
    name="osst",
    version="0.1.0",
    description="Operating System Story Teller (OSST)",
    author="enabler",
    packages=find_packages(),
    entry_points={"console_scripts": ["osst=osst.__main__:main"]},
    python_requires=">=3.6",
    install_requires=[
        "psutil",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
)
