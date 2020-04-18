import pandas as pd

def main():
    example = pd.read_csv('Recipes/example.csv')
    print(example.groupby(['Ingredienser', 'Enhet']).sum())

if __name__=='__main__':
    main()
