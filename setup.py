from distutils.core import setup
setup(name='pdf_render',
      version='0.1',
      packages=['pdf_render',],
      install_requires=open('requirements.txt').readlines(),
      )