from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='spacelaser',
    version='0.1',
    author='pmcoelho',
    author_email='pmcoelho@protonmail.com',
    url='https://github.com/pm-coelho/spacelaser',
    description='A spacemacs inspired menu to help you execute automated shortcuts',
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='GPLv3+',
    packages=find_packages(exclude=('test')),
    include_package_data=True,
    install_requires=['spacemenu', 'ConfigArgParse', 'PyYAML'],
    entry_points={
        'console_scripts': ['spacelaser=spacelaser.run:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
    ]
)
