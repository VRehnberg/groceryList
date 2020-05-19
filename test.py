import os
import readline

import pandas as pd

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')


def main():
    items = pd.DataFrame()
    while True:
        filename = input('Enter file for recipe or stop to quit:')
        try:
            if filename == 'stop':
                break
            elif os.path.isfile(filename):
                rec = pd.read_csv(filename)
                multiple = float(input('Multiple?'))
                rec['Antal'] = rec['Antal'].apply(lambda x: x*multiple)
                items = pd.concat([items, rec])
                print(os.path.basename(filename), 'added.')
            else:
                print(f'{filename} is not a filename! Try again.')
        except Exception as e:
            print(e)
            print('Try again.')
    print('==================================================')
    print(items.groupby(['Artikel', 'Enhet']).sum())
    df.to_csv(r'tmp.txt', sep=' ', mode='a')

if __name__=='__main__':
    main()
