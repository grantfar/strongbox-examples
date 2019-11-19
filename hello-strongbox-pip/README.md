This is an example of how to use the Strongbox artifact repository manager with PIP
## Prerequisites
 - Python 3
 - PIP
## Prepare project workspace
Go to the root project folder and execute the following commands:
### For Linux:
```
$ mkdir HelloWorld 
$ touch LICENSE.txt
$ touch setup.py
$ touch setup.cfg
$ touch HelloWorld/__init__.py
$ touch HelloWorld/hello.py
```
### For Windows:
```
> mkdir HelloWorld 
> type nul > LICENSE.txt
> type nul > setup.py
> type nul > setup.cfg
> type nul > HelloWorld/__init__.py
> type nul > HelloWorld/hello.py
```
## Making Hello World Project
### Writing Code
Open each file and input the corresponding text. Make sure that the white space is correct because python has white space syntax.

hello.py:
```
class hello:
    def __init__(self):
        super().__init__()
    def world(self):
        print("hello world")
```

\_\_init\_\_.py:
```
from HelloWorld.hello import hello
```

setup.py:
```
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
```

LICENSE.txt:
```
MIT License
Copyright (c) 2018 YOUR NAME
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
### Creating Packages
Go to the root project folder and execute the following commands:
```
python -m pip install --user --upgrade setuptools wheel
