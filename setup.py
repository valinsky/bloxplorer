import setuptools

with open('README.rst', 'r') as f:
    readme = f.read()

setuptools.setup(
    name='bloxplorer',
    version='0.1.10',
    description='Bitcoin and Liquid blockchain explorer',
    long_description=readme,
    author='Vali Voicu',
    author_email='contact@valinsky.me',
    url='https://github.com/valinsky/bloxplorer',
    license='MIT',
    packages=['bloxplorer'],
    include_package_data=True,
    install_requires=['requests'],
    test_suite='tests',
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
