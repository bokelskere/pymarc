# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

install_requires = []
try:
    import xml.etree
except ImportError:
    install_requires.append('elementtree>=1.2.6')

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Text Processing :: General
"""

setup( 
    name = 'pymarc',
    version = '2.50',  # remember to update pymarc/__init__.py on release!
    url = 'http://github.com/edsu/pymarc',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/bsd-license.php',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'read, write and modify MARC bibliographic data',
    classifiers = filter(None, classifiers.split('\n')),
    test_suite = 'test',
)
