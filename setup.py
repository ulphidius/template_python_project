from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    CONTENT_README = readme.read()

setup(
    name='template_python_project',
    version='0.1.0',
    author='ulphidius',
    url='https://github.com/ulphidius/template_python_project',
    description='Template test for python bin',
    long_description=CONTENT_README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        template_python_project=template_python_project.main:main 
    '''
)