from setuptools import setup

setup(
    install_requires=['flake8'],
    entry_points={
        'console_scripts': [
            'mccabe-complexity = mccabe_complexity.complexity_check:main',
        ],
    },
)
