from distutils.core import setup

setup(name='Nginxparser',
      version='0.3',
      description='Nginx Parser',
      author='Fatih Erikli',
      author_email='fatiherikli@gmail.com',
      url='https://github.com/fatiherikli/nginxparser',
      py_modules=['nginxparser'],
      install_requires = [
          'pyparsing>=1.5.5'
      ]
)
