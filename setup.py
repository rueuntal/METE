from setuptools import setup, find_packages

setup(name = 'mete',
      version= '0.1',
      description = 'Tools for analying the Maximum Entropy Theory of Ecology',
      author = "Ethan White, Dan McGlinn, Xiao Xiao, Sarah Supp, and Katherine Thibault",
      url = 'https://github.com/weecology/mete',
      packages = find_packages(),
      package_data = {'mete': ['beta_lookup_table.pck']},
      license = 'MIT',
)
