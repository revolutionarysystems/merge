import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='merge',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A Django app to perform document merge.',
    install_requires = ['apiclient==1.0.2', 'colorama==0.3.7', 'django-extensions==1.6.1', 'django-password-protect==0.0.3', 
                            'google-api-python-client==1.5.0', 'httplib2==0.9.2', 'iso8601==0.1.11', 'markdown==2.6.5', 'mock==2.0.0', 
                            'oauth2client==2.0.0.post1', 'pbr==1.9.1', 'pdfminer3k==1.3.0', 'ply==3.8', 'py==1.4.31', 
                            'pyasn1-modules==0.0.8', 'pyasn1==0.1.9', 'pypdf2==1.27.5', 'pytest==2.9.1', 'python-docx==0.8.5', 
                            'pytz==2016.4', 'rsa==3.3', 'simplejson==3.8.2', 'six==1.10.0', 'uritemplate==0.6', 'urllib3==1.14', 
                            'xmltodict==0.10.1'],
    long_description=README,
    url='https://www.revolutionarysystems.co.uk/',
    author='Andrew Elliott',
    author_email='andrewelliott@revolutionarysystems.co.uk',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)