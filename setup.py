from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Collection of different APIs.'

# Setting up
setup(
    name="pythonapikit",
    version=VERSION,
    author="ShadowFlameFox",
    author_email="<shadow_flame_fox@web.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="""Coming soon...""",
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['Python', 'API', 'Weather', 'Collection', "Integration","Wrapper","Client","Request","Endpoint","HTTP","REST","Web Services","Connector","Utility","Toolset","Helper","Manager","Facade","Handler","Assist","Bundle","Kit","JSON"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)