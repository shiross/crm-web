from distutils.core import setup
from setuptools import find_packages

requires = ['tornado', 'sqlalchemy', 'configparser', 'schedule','openpyxl','pymysql']

setup(
    name='Base Project',
    version='1',
    packages=find_packages(),
    url='',
    license='Free',
    author='Brian Rot Sagredo Lijeron',
    author_email='brianroy78@hotmail.com',
    description='Server Base on Tornado framework',
    install_requires=requires
)