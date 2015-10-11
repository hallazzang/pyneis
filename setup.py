import re
import codecs

from setuptools import setup

def get_values(path):
    values = {}
    pattern = re.compile('^__([\w_]+)__\s*=\s*\'(.+)\'$')
    with codecs.open(path, encoding='utf-8') as f:
        for line in f:
            matched = pattern.match(line)
            if matched:
                values.update(dict([matched.groups()]))
    return values

with codecs.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

values = get_values('neis/__init__.py')

setup(
    name='pyneis',
    version=values['version'],

    description='python http client for Neis service(http://neis.go.kr/)',
    long_description=long_description,

    url='https://github.com/HallaZzang/pyneis',

    author=values['author'],
    author_email=values['author_email'],

    license='MIT License',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords=['pyneis', 'neis'],

    packages=['neis'],

    install_requires=['requests', 'BeautifulSoup4']
)