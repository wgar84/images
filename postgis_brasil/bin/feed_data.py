# %%
from unidecode import unidecode as un
import lib.db as pg
import pandas as pd
import geopandas as gp
import lib.db as pg

# %%
brasil = gp.read_file('geodata-br/geojson/geojs-100-mun.json')
ufs = pd.read_csv('data/codigos_ibge.csv')

brasil = (
    brasil
    .assign(
        nome_limpo=[un(row.name.upper()) for row in brasil.itertuples()],
        codigo_uf=[int(row.id) // 100000 for row in brasil.itertuples()],
        geometria=[str(row.geometry) for row in brasil.itertuples()]
    )
    .merge(
        ufs, left_on='codigo_uf', right_on='cod', how='left'
    )
    .drop(columns=['cod', 'description', 'geometry'])
)

# %%
brasil.columns

# %%
in_cols = brasil.columns

out_cols = [
    'ibge', 
    'nome', 
    'nome_limpo', 
    'codigo_uf',
    'geometria', 
    'sigla_uf',
    'nome_uf',
    'regiao_uf'
]

rename_cols = dict(zip(in_cols, out_cols))

brasil = brasil.rename(columns=rename_cols)

# %%
for row in brasil.to_dict(orient='records'):
    entry = pg.Municipio(**row)
    pg.session.add(entry)

pg.session.commit()