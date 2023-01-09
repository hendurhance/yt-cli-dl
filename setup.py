import setuptools
from yt_cli_dl.version import Version

setuptools.setup(
    name='yt-cli-dl',
    version=Version('1.0.0').number,
    author='Endurance',
    author_email='hendurhance.dev@gmail.com',
    description='A YouTube video and playlist downloader command-line interface (CLI) tool',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    url='https://github.com/hendurhance/yt-downloader-cli',
    packages=setuptools.find_packages(),
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    py_modules=['yt_cli_dl'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'yt-cli-dl=yt_cli_dl.cli:main',
        ],
    },
)
