from distutils.core import setup
setup(
  name='Django-Hexadecimal-Field',        
  packages=['Django-Hexadecimal-Field'],   
  version='0.1',    
  license='MIT',      
  description='TYPE YOUR DESCRIPTION HERE', 
  author='YOUR NAME',                   # Type in your name
  author_email='your.email@domain.com',      # Type in your E-Mail
  url='https://github.com/user/reponame',   # Provide the link to your github
  download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords 
  install_requires=[            # I get to this in a second
          'validators',
          'django',
          'python',
  ],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',   # Again, pick a license
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
  ],
)