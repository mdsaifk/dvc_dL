from setuptools import setup

with open("README.md","r",encoding = "utf-8") as f:
     long_decription = f.read()

setup(
    name = "src",
    version = "0.0.1",
    author = "mdsaifk",
    description = "A small package for dvc DL pipleine demo",
    long_description= long_decription,
    url = "https://github.com/mdsaifk/dvc_dL.git",
    author_email = "mdsaifkhan200@gmail.com",
    package_name= ["src"],
    license= "GNU",
    python_requires = ">=3.7",
    install_requires = ['dvc',
    'tensorflow',
    'matplotlib',
    'numpy',
    'pandas',
    'tqdm',
    'PyYaml',
    'boto3'])