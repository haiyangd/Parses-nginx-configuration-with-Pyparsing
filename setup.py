from distutils.core import setup

setup(name='Nginxparser',
      version='0.2',
      description='Nginx Parser',
      author='Fatih Erikli',
      author_email='fatiherikli@gmail.com',
      url='https://github.com/fatiherikli/nginxparser',
      packages=['nginxparser'],
      install_requires = [
          'pyparsing==1.5.5'
      ]
)
