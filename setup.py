import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description=fh.read()

PACKAGE_NAME = "Perceptron_pkg"
PROJECT_NAME = "Perceptron-pkg"
USER_NAME = "iambalakrishnan"

setuptools.setup(
    name=f"{PACKAGE_NAME}",
    version="0.0.3",
    author=USER_NAME,
    author_email="imbkrishnaa@gmail.com",
    description="A small package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy==1.21.4",
        "pandas==1.3.4",
        "joblib==1.1.0"]
    )