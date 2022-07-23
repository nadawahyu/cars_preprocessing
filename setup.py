import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'cars_prediction',
    version = '0.0.1',
    author = 'nada',
    author_email = 'nadawahyu@gmail.com',
    description = 'simple repo for assignment',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = '',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    install_requires = [
        "matplotlib",
        "numpy",
        "pandas==1.1.4",
        "pydantic==1.6.1",
        "scikit-learn",
        "seaborn==0.11.0",
        ],
    python_requires = '>=3.7'
)