import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yt-downloader-cli",
    version="1.0.0",
    author="Endurance",
    author_email="hendurhance.dev@gmail.com",
    description="A YouTube video and playlist downloader command-line interface (CLI) tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hendurhance/yt-downloader-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pytube"],
    entry_points={
        "console_scripts": [
            "yt-downloader-cli=cli:main",
        ],
    },
)
