from setuptools import setup, find_packages

with open('README.md') as readme_file:
    long_description = readme_file.read()
with open('LICENSE.txt') as license_file:
    license = license_file.read()

setup(
    name='tagtomarkdown',
    version='0.2.7',
    description='Python3 markdown extension for converting tags to Markdown table',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['markdown'],
    py_modules=['tagtomarkdown'],
    author='Christian Hauris Sorensen',
    author_email='chrhauris@hotmail.com',
    url='https://github.com/chrhauris/tagtomarkdown',
    license=license,
    keywords='Markdown MkDocs tables',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Documentation',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing',
    ],
    # markdown.extensions is for Python Markdown and MkDocs
    # console_scripts is for getting the product's version number using these commands:
    #   import tagtomarkdown
    #   print(tagtomarkdown.version())
    #
    entry_points={
      'markdown.extensions': ['tagtomarkdown = tagtomarkdown:TableTagExtension'],
      'console_scripts': ['version = tagtomarkdown:version']
    }
)