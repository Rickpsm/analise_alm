# Análise de Capital e RWA: Modelo Padronizado (S3) vs. Modelos Internos (S1)

Este projeto realiza uma simulação estocástica de uma carteira de crédito de varejo com 2.000 contratos para comparar a eficiência de capital entre as abordagens de bancos do **Segmento 1 (S1)** e **Segmento 3 (S3)**, conforme as normas do **Banco Central do Brasil**.

## Objetivos
* Calcular o **RWA (Risk-Weighted Assets)** sob a ótica padronizada (S3).
* Estimar o consumo de capital via modelos internos (**IRB**) para o Segmento 1.
* Realizar análise de **Breakeven de PD** para identificar a seletividade de risco do modelo avançado.
* Simular parâmetros de **PD**, **LGD** e **EAD** para uma carteira de varejo.

---

## Tecnologias Utilizadas
* **Python 3.12**
* **Pandas & NumPy**: Manipulação de dados e cálculo vetorial das fórmulas regulatórias.
* **Matplotlib & Seaborn**: Visualização da distribuição de riscos e curvas de capital.
* **SciPy**: Funções de distribuição normal para o cálculo do Requisito de Capital (K).

---

## Fundamentação Regulatória
O projeto segue rigorosamente as diretrizes de **Basileia III** adaptadas pelo BACEN:

### Risco de Crédito (S3 - Padronizado)
* **Resolução CMN nº 2.682/1999**: Classificação de risco (Rating AA a H) e provisionamento.
* **IN BCB nº 200/2021**: Definição dos pesos de risco (RW) fixos para varejo (75%) e operações vencidas (100%/150%).

### Risco de Crédito (S1 - IRB)
* **Resolução BCB nº 303/2023**: Fórmulas de correlação ($R$) e capital ($K$) para modelos internos de varejo.
* **Cálculo de EAD**: Aplicação do **CCF (Credit Conversion Factor)** para linhas de crédito rotativo.

### Adicionais de Capital (ACP)
* **Resolução CMN nº 4.958/2021**: Definição dos buffers de capital principal (Conservação e Sistêmico).

---

## Principais Insights
1. **Eficiência de Capital**: O modelo IRB mostrou-se significativamente mais eficiente para ratings AA e A devido à baixa PD, compensando o custo extra do ACP Sistêmico.
2. **Breakeven Point**: O ponto de equilíbrio do requisito de capital ($K$) entre S1 e S3 foi identificado em **5,48%**.
3. **Seletividade**: Acima do breakeven, o modelo avançado penaliza o capital de forma mais severa que o padronizado, exigindo estratégias de pricing mais agressivas.

---

## Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o notebook `data_analisys_portfolio.ipynb` para visualizar a comparação.

---

## Próximos Passos
* Implementação de curvas de juros para análise de **EVE** e **NII** (**IRRBB**).
* Simulação de cenários de estresse macroeconômico.

---
**Desenvolvido por Ricardo de Padua Souza Menezes** *Senior Market Risk Analyst*