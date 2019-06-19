import setuptools
import taskman

with open('README.md', 'r') as f:
    long_description = f.read()


print(setuptools.find_packages())

setuptools.setup(
    name=taskman.__appname__,
    version=taskman.__version__,
    author='Matthias Gilch',
    author_email='matthias.gilch.mg@gmail.com',
    description='A little and simple task manager',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.github.com:DaGuich/taskman.git',
    packages=['taskman'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'appdirs==1.4.3'
    ]
)
