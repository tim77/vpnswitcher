from setuptools import setup, find_packages

setup(
        name='vpnswitcher',
        version='1.0',
        packages=find_packages(),
        package_dir={
            'vpnswitcher': 'vpnswitcher'
            },
        url='https://github.com/xshram/vpnswitcher'
        entry_points={
            'console_scripts': [
                'vpnswitcher = '

                ],
            },

        license='MIT',
        install_requires=['python3-gobject','python3-devel','gtk3','python3-cairo-devel'],
        author='Vladislav Vekyu',
        author_email='xshram@protonmail.com',
        description='Desktop application for controlling Wireguard'


)
