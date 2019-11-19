from distutils.core import setup
setup(
  name = 'HelloWorld',
  packages = ['HelloWorld'],
  version = '0.1',
  license='MIT',
  description = 'Don\'t use',
  author = 'your name',                   # Type in your name
  author_email = 'your_email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/user/HelloWorld',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/HelloWorld/archive/HelloWorld-0.1.whl', # Provide either the link to your github or to your website download
  keywords = ['Test', 'Useless', 'Don\'t'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)