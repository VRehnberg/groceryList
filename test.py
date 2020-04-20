import pandas as pd

def main():
    artcarbonara = pd.read_csv('Recipes/Ärtcarbonara_4p.csv')
    gronkalspasta = pd.read_csv('Recipes/Grönkålspasta_4p.csv')
    citronigkgryta = pd.read_csv(
        'Recipes/Citronig_kikärtsgryta_4p.csv'
    )  # ggr 6
    artsoppa = pd.read_csv('Recipes/Ärtsoppa_8p.csv')
    jordnotsgryta = pd.read_csv(
        'Recipes/Jordnötsgryta_med_oumph_4p.csv'
    )  # ggr 2
    gottbullar = pd.read_csv(
        'Recipes/Göttbullar_med_potatismos_och_brunsås_och_lingon_4p.csv'
    )
    citron_och_mgryta = pd.read_csv(
        'Recipes/Citron_och_morotsgryta_med_rosmarin_4p.csv'
    )  # ggr 6
    kantarellpasta = pd.read_csv('Recipes/Kantarellpasta_4p.csv')
    lasagne_i_langpanna = pd.read_csv(
        'Recipes/Lasagne_i_långpanna_8p.csv'
    )  # ggr 3
    frames = [
        artcarbonara,
        gronkalspasta,
        citronigkgryta, citronigkgryta, citronigkgryta,
        citronigkgryta, citronigkgryta, citronigkgryta,
        artsoppa,
        jordnotsgryta, jordnotsgryta,
        gottbullar,
        citron_och_mgryta, citron_och_mgryta, citron_och_mgryta,
        citron_och_mgryta, citron_och_mgryta, citron_och_mgryta,
        kantarellpasta,
        lasagne_i_langpanna, lasagne_i_langpanna, lasagne_i_langpanna,
    ]
    groceryList = pd.concat(frames)
    print('==================================================')
    print(groceryList.groupby(['Artikel', 'Enhet']).sum())

if __name__=='__main__':
    main()
