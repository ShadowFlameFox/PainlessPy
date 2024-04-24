from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Makes programming with Python easier.'

# Setting up
setup(
    name="painlesspy",
    version=VERSION,
    author="ShadowFlameFox",
    author_email="<shadow_flame_fox@web.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="""Coming soon...""",
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['Python', "WeatherAPI"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
