from setuptools import find_packages, setup

setup(
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=['flake8'],
    entry_points={
        'console_scripts': [
            'mccabe-complexity = mccabe_complexity.complexity_check:main',
        ],
    },
)
