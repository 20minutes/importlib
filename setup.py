from distutils.core import setup

version_classifiers = ['Programming Language :: Python :: %s' % version
                        for version in ['2', '2.3', '2.4', '2.5', '2.6',
                                        '3', '3.0']]
other_classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Python Software Foundation License',
    ]

readme_file = open('README', 'r')
try:
    detailed_description = readme_file.read()
finally:
    readme_file.close()


setup(
        name='importlib',
        version='1.0.2',
        description='Backport of importlib.import_module() from Python 2.7',
        long_description=detailed_description,
        author='Brett Cannon',
        author_email='brett@python.org',
        url='http://svn.python.org/view/sandbox/trunk/importlib/',
        packages=['importlib'],
        classifiers=version_classifiers + other_classifiers,
    )