# Beatiful Soup Tutorial

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

The examples in this documentation should work the same way in Python 2.7 and Python 3.2.

Documentation : https://www.crummy.com/software/BeautifulSoup/bs4/doc/


### Prerequisites
If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

$ apt-get install python-bs4 (for Python 2)

$ apt-get install python3-bs4 (for Python 3)

Beautiful Soup 4 is published through PyPi, so if you can’t install it with the system packager, you can install it with easy_install or pip. The package name is beautifulsoup4, and the same package works on Python 2 and Python 3. Make sure you use the right version of pip or easy_install for your Python version (these may be named pip3 and easy_install3 respectively if you’re using Python 3).

$ easy_install beautifulsoup4

$ pip install beautifulsoup4

(The BeautifulSoup package is probably not what you want. That’s the previous major release, Beautiful Soup 3. Lots of software uses BS3, so it’s still available, but if you’re writing new code you should install beautifulsoup4.)

If you don’t have easy_install or pip installed, you can download the Beautiful Soup 4 source tarball and install it with setup.py.

$ python setup.py install

If all else fails, the license for Beautiful Soup allows you to package the entire library with your application. You can download the tarball, copy its bs4 directory into your application’s codebase, and use Beautiful Soup without installing it at all.

I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it should work with other recent versions.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Agustin Blacker** 

## Acknowledgments

* More info : https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
