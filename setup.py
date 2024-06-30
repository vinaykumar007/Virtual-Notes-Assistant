import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Virtual-Notes-Assistant"
AUTHOR_USER_NAME = "vinaykumar007"
SRC_REPO = "Virtual_notes_Assistant"
AUTHOR_EMAIL = "vinay.iitkgp0206@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/vinaykumar007/Virtual-Notes-Assistant",
    project_urls={
        "Bug Tracker": "https://github.com/vinaykumar007/Virtual-Notes-Assistant/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)