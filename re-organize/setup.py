import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-Image-Classification"
AUTHOR_USER_NAME = "bala1802"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "bala1802@live.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Balaguru Sivasambagupta",
    author_email="bala1802@live.com",
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/bala1802/End-to-End-Image-Classification",
    project_urls={
        "Bug Tracker": f"https://github.com/bala1802/End-to-End-Image-Classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)