from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='spotify_song_analysis',
      version="0.0.4",
      description="Analysis of Spotify song 100k dataset",
      license="MIT",
      author="Mischa Dhar",
      author_email="mischadhar94@gmailcom",
      url="https://github.com/MDhar94/music_analysis",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
