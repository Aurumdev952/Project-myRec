from setuptools import setup, find_packages


setup(
    name="myRec_CLI",
    author="Aurumdev", 
    author_email="benjdev2007@gmail.com",
    description="this is the CLI client for myrec system",
    packages=find_packages(),
    install_requires=[
        "click",
        "httpx"
    ],
    version="1.0.1",
    entry_points='''
    [console_scripts]
    myrec=cli.main:master
    '''
)