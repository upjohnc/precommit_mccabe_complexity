from setuptools import setup

setup(
    packages=['flake8'],
    entry_points={
        'console_scripts': [
            'mccabe-complexity = mccabe_complexity.complexity_check:main',
        ],
    },
)
