import re
import os
from glob import iglob
import readline

import pandas as pd


readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)


class Recipe:
    '''
    Contains the information for one receip

    Args:
        filename (str): Name of file in Recipes

    Attributes:
        name (str): Name of file in Recipes
        items (dataframe): Items in the recipe
        size_str (str): How the size was specified
        fillings (float): Number of fillings recipe is made for
    '''
    def __init__(self, filename):
        self.name = os.path.basename(filename)
        self.items = pd.read_csv(filename)
        self.size_str = os.path.splitext(filename)[-2].split('_')
        self.fillings = re.match('^[0-9]+', self.size_str).group()


class GroceryList:
    '''
    Class to build a grocery list from Recipes

    Attributes:
        items (dataframe): Items in the grocery list built from recepies
    '''
    def __init__(self):
        self.recipes = [Recipe(fn) for fn in iglob('Recipes/*.csv')]
        self.filenames = [r.name for r in recipes]
        self.items = pd.DataFrame()

    def add_to_list(self, filename=None):
        pass

