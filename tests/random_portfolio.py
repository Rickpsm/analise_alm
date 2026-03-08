import pandas as pd
import numpy as np

# Configuração de semente para reprodutibilidade
np.random.seed(42)

n_rows = 2000

data = {
    'ID_Contrato': range(1001, 1001 + n_rows),
    'Produto': np.random.choice(['Emprestimo_Pessoal', 'Cartao_Credito', 'Parcelado_Loja'], n_rows),
    'Valor_Nocional': np.random.uniform(500, 50000, n_rows).round(2),
    'Taxa_Contratada_AA': np.random.uniform(0.12, 0.30, n_rows).round(4), # 12% a 30% aa
    'Prazo_Remanescente_Meses': np.random.randint(1, 48, n_rows),
    'Indexador': np.random.choice(['PRE', 'POS-CDI'], n_rows, p=[0.7, 0.3]),
    'Rating_2682': np.random.choice(['AA', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                                    , n_rows
                                    , p=[0.40, 0.30, 0.10, 0.05, 0.05, 0.04, 0.03, 0.02, 0.01]),
    'Dias_Atraso': np.random.choice([0, 5, 15, 45, 100, 200], n_rows, p=[0.8, 0.1, 0.05, 0.03, 0.01, 0.01])
}

df_clientes = pd.DataFrame(data)

# Salvar como CSV
df_clientes.to_csv(r'/home/ricardo/Documents/Projects/analise_alm/data/base_clientes_varejo_simulada.csv', index=False)
