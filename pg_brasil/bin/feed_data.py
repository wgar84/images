# %%
import re
import unidecode as un
import pandas as pd
import geopandas as gp
import lib.pg_brasil as pg
from shapely.geometry.multipolygon import MultiPolygon


def clear_string(s):
    new_s = un.unidecode(s)
    new_s = new_s.upper()
    new_s = re.sub('[^A-Z 0-9]', ' ', new_s)
    return new_s


# %%
brasil = gp.read_file('geodata-br/geojson/geojs-100-mun.json')
ufs = pd.read_csv('data/codigos_ibge.csv')
ufs_mapa = gp.read_file('data/brasil.json')

# %%
brasil = (
    brasil
    
    .assign(
        nome_limpo=[clear_string(row.name) for row in brasil.itertuples()],
        codigo_uf=[int(row.id) // 100000 for row in brasil.itertuples()],
        geometria=[str(row.geometry) for row in brasil.itertuples()]
    )
    
    .merge(
        ufs, left_on='codigo_uf', right_on='cod', how='left'
    )
    
    .drop(columns=['cod', 'description', 'geometry'])
)

brasil = (
    brasil  
    .assign(
        nome_limpo_uf=[clear_string(row.uf) for row in brasil.itertuples()]
    )
)

# %%
# UFS

def poly2string(row):
    try: 
        return str(MultiPolygon([row.geometry]))
    except ValueError:
        return str(row.geometry)


ufs_mapa = ufs_mapa.drop(columns=['MICRO', 'MESO'])

ufs_mapa = ufs_mapa.assign(
    geometria=[poly2string(row) for row in ufs_mapa.itertuples()],
    nome_limpo=[clear_string(row.NOME_UF) for row in ufs_mapa.itertuples()]
)

ufs_mapa = ufs_mapa.drop(columns='geometry')

ins = ufs_mapa.columns

out = [
    'sigla',
    'regiao',
    'nome',
    'codigo_ibge',
    'geometria',
    'nome_limpo'
]

_rename = dict(zip(ins, out))

ufs_mapa = ufs_mapa.rename(columns=_rename)

# print(ufs_mapa.head())

for row in ufs_mapa.to_dict(orient='records'):
    entry = pg.UF(**row)
    pg.session.add(entry)

pg.session.commit()

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
    'regiao_uf',
    'nome_limpo_uf'
]

rename_cols = dict(zip(in_cols, out_cols))

brasil = brasil.rename(columns=rename_cols)


# %%
for label, uf in brasil.groupby('codigo_uf'):
    _uf = pg.session.query(pg.UF).filter(pg.UF.codigo_ibge == label).one()
    for row in uf.to_dict(orient='records'):
        entry = pg.Municipio(**row)
        _uf.municipios.append(entry)
        pg.session.add(entry)

pg.session.commit()

