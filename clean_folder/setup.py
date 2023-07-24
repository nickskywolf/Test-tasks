from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='0.01b',
      description='Clean Folder',
      author='Nick',
      author_email='nick@python.test',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']}
)