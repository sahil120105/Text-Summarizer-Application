import setuptools

# Open and read the README.md file to use as the package long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()  # Store README content inside long_description variable

# Define the current version of the package (update this for every new release)
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Application"       # Name of the GitHub repository
AUTHOR_USER_NAME = "sahil120105"                # GitHub username of the author
SRC_REPO = "textSummarizer"                     # Actual Python package name (folder name inside src/)
AUTHOR_EMAIL = "sahilranadive12@gmail.com"      # Author contact email


# Core setup configuration function for packaging
setuptools.setup(

    name=SRC_REPO,                                                                          # Name of the package (used in pip install command)
    version=__version__,                                                                    # Version of the package
    author=AUTHOR_USER_NAME,                                                                # Package author name
    author_email=AUTHOR_EMAIL,                                                              # Package author email
    description="A small python package for NLP app",                                       # Short one-line description of the project
    long_description=long_description,                                                      # Detailed project description (taken from README.md)
    long_description_content_type="text/markdown",                                          # Specify that the long description is written in Markdown format
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",                               # URL pointing to the project repository
    project_urls={                                                                          # Additional project-related URLs (like issue tracker)
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    # Specify that all packages are located inside the "src" directory
    # "" represents the root namespace
    package_dir={"": "src"},

    # Automatically discover all Python packages inside "src"
    # Only directories containing __init__.py are considered packages
    packages=setuptools.find_packages(where="src")
)
