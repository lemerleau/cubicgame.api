from setuptools import (setup, find_packages)
from cubicgame import (__VERSION__, __AUTHOR__, __AUTHOR_EMAIL__)


def get_requirements():
    return open('requirements.txt').read().splitlines()


setup(
    name='cubicgame',
    version=__VERSION__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    description='Cubic game backend API',
    url='https://github.com/lemerleau/cubicgame.api',
    # download_urk='https://github.com/lemerleau/cubicgame.api/tarball/v%s' % __VERSION__,
    keywords=['Cubic', 'Game', 'django cubicgame API'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='GNUGPL-v3',
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    setup_requires=['numpy','pybind11', 'Cython', 'certifi'],
    install_requires=get_requirements(),
)
