from setuptools import setup

setup(name='django-api-generator',
      version='0.1',
      description='django genrator api package for my cms',
      url='https://github.com/omarenis/django-api-genrator.git',
      author='Omar Triki',
      author_email='omartriki712@gmail.com',
      license='MIT',
      packages=['django-api-generator'],
      include_package_data=True,
      install_requires=[
          'django',
          'djangorestframework',
          'django-cors-headers'
      ],
      zip_safe=False)
