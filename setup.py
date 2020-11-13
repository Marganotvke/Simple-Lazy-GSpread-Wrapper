import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slgsw", # Replace with your own username
    version="0.2",
    author="Marganotvke",
    author_email="<current none>",
    description="A simple wrapper for gspread for people who have limited programming experience, or just simply too lazy to read the gspread docs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Marganotvke/Simple-Lazy-GSpread-Wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "gspread",
        "oauth2client"
    ],
    python_requires='>=3.6',
)