import pandas as pd
import numpy as np

df_base = pd.read_csv(r'/home/ricardo/Documents/Projects/analise_alm/data/base_clientes_varejo_simulada.csv')
df_clientes = df_base.copy()


# 1. Mapeamento de PD (Métrica baseada na Res. 2.682)
pd_mapping = {'AA': 0.001, 'A': 0.005, 'B': 0.010, 'C': 0.030, 
              'D': 0.100, 'E': 0.300, 'F': 0.500, 'G': 0.700, 'H': 1.000}

# 2. Mapeamento de LGD (Padrão de mercado para Varejo sem garantia)
lgd_mapping = {'Cartao_Credito': 0.85, 'Emprestimo_Pessoal': 0.75, 'Parcelado_Loja': 0.65}

# 3. Cálculo de EAD (Exposure at Default)
def calc_ead(row):
    if row['Produto'] == 'Cartao_Credito':
        # Simula um Limite Total (20% a 50% acima do uso atual)
        limite = row['Valor_Nocional'] * np.random.uniform(1.2, 1.5)
        # Aplica o CCF de 50% (Credit Conversion Factor)
        return row['Valor_Nocional'] + ((limite - row['Valor_Nocional']) * 0.50)
    return row['Valor_Nocional']

# Aplicando as transformações no DataFrame df_clientes
df_clientes['PD'] = df_clientes['Rating_2682'].map(pd_mapping)
df_clientes['LGD'] = df_clientes['Produto'].map(lgd_mapping)
df_clientes['EAD'] = df_clientes.apply(calc_ead, axis=1).round(2)

# Salvar como CSV
df_clientes.to_csv(r'/home/ricardo/Documents/Projects/analise_alm/data/base_clientes_varejo_simulada_pds.csv', index=False)
