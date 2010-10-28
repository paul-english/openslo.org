from distutils.core import setup

setup(
    name = "openslo",
    url = "http://github.com/openslo/openslo.org/",
    author = "Sean Bleier",
    author_email = "sebleier@gmail.com",
    version = "0.1a",
    packages = ["openslo"],
    description = "Apps powering openslo.org",
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
