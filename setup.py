import setuptools

with open('README.rst', 'r') as f:
    readme = f.read()

setuptools.setup(
    name='bloxplorer',
    version='0.1.1',
    description='Bitcoin and Liquid blockchain explorer',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Dumitru Valeriu Voicu',
    author_email='valinsky@protonmail.com',
    url='https://github.com/valinsky/bloxplorer',
    license='MIT',
    packages=['bloxplorer'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
