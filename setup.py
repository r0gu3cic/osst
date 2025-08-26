from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="osst",
    version="0.1.0",
    description="Operating System Story Teller (OSST)",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
