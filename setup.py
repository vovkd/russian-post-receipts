from distutils.core import setup
setup(name='pdfrender',
      version='0.1',
      package_dir={'pdf_render': 'src/pdf_render'},
      packages=['pdf_render',],
      #install_requires=open('requirements.txt').readlines(),
      )