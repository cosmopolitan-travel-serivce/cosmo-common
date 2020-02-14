import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ctscommon',
    version='0.3.17',
    description='A python package to centralize everything common for CTS micro services',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cosmopolitan-travel-serivce/ctscommom',
    license='MIT',
    author='Cosmo Tech Service',
    author_email='mohamed@ctsfares.com',
    packages=setuptools.find_packages(),
    install_requires=[
        "pydantic",
        "python-dotenv",
        "fastapi",
        "pyjwt",
        "passlib[bcrypt]",
        "py_eureka_client",
        "requests",
        "PyYAML",
        "werkzeug",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
