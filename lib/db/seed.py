from setuptools import setup, find_packages

setup(
    name='pocket companions',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pygame',
        'faker',
    ],
    entry_points='''
        [console_scripts]
        pocket_companions=pet_game:cli
    ''',
)
