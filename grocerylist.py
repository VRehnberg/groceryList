import pandas as pd

class Recipe:
    '''
    Contains the information for one receip

    Args:
        name (str): Name of file in Recipes

    Attributes:
        name (str): Name of file in Recipes
        items (dataframe): Items in the recipe
        fillings (float): Number of fillings recipe is made for
    '''
    def __init__(self):
        raise NotImplementedError('TODO')

class GroceryList:
    '''
    Class to build a grocery list from Recipes

    Attributes:
        items (dataframe): Items in the grocery list built from recepies
    '''
    def __init__(self):
        pass
