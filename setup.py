from setuptools import setup
import pip


install_packages = ["pygame"]


# numpy is required but it can only be installed with pip
try:
    import numpy  # noqa
except ImportError:
    print("Installing numpy using pip...")
    pip.main(["install", "numpy"])


setup(name="pythonise_your_lab",
      version="0.0.0",
      url="https://github.com/fariza/pythonise_your_lab",
      install_requires=install_packages)
