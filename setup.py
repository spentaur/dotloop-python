import setuptools


if __name__ == '__main__':
    with open('README.md', 'r') as fh:
        long_description = fh.read()

    setuptools.setup(
        name='dotloop-python',
        version='0.0.6',
        packages=setuptools.find_packages(),
        install_requires=['requests'],
        author='Ben Russell',
        author_email='benr@cal-am.com',
        description='Python wrapper around the dotloop API.',
        keywords=['dotloop', 'api', 'wrapper', 'requests', 'zillow', 'oauth'],
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/benr-calam/dotloop-python',
        project_urls={
            'Documentation': 'https://github.com/benr-calam/dotloop-python',
            'Source Code': 'https://github.com/benr-calam/dotloop-python',
        },
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.7',
    )

    # python setup.py sdist bdist_wheel
    # twine upload dist/*
