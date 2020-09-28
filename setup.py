import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DateTimeTools",
    version="0.0.9",
    author="Matthew Knight James",
    author_email="mattkjames7@gmail.com",
    description="A package containing some simple tools to manage dates and times.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattkjames7/DateTimeTools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
		'numpy',
		'scipy',
		'cdflib',
	],
	include_package_data=True,
)
