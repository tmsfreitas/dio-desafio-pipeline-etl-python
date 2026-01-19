
# Santander Bootcamp 2025 - Ciência de Dados com Python

<div align="center">
  <img src="https://camo.githubusercontent.com/6891f939e604f86cbb6ce4888c31c016acdc7f165c7d65e9c36f7bbe2e533631/68747470733a2f2f6865726d65732e64696f2e6d652f747261636b732f30333235336666302d393562392d343930342d383465372d3230363365396436633232362e706e67" width="300" alt="Logo Bootcamp">
</div>

# Construindo um Pipeline ETL com Python - Estimativas de Preços Agrícolas 2026

Este é um desafio de projeto do Santander Bootcamp 2025 - Ciência de Dados com Python.

---

## 👨🏽‍💻 Meu projeto

**Contexto:** Meu desafio é criar uma pipeline ETL para extrair dados de um arquivo CSV disponibilizado por um fazendeiro a respeito dos valores obtidos em produtos agrícolas produzidos por ele nos anos de 2024 e 2025, com o intuito de ter estimativas pessimistas e otimistas para o próximo ano de 2026.

**Extração:** Feita a Extração dos dados, passarei para a fase de Transformação, na qual vou precisar calcular os percentuais para cada produto.

**Carregamento:** Por fim, devo realizar o Carregamento do dados transformados em um novo arquivo CSV, além de criar uma visualização gráfica dos resultados e já salvando o arquivo.

---

## 📋 Etapas do Pipeline de ETL

### 🎲 Extract

Nesta etapa, vamos extrair os dados de preços agrícolas do arquivo Excel `produtos_agro.csv`. Este arquivo traz informações referentes aos preços dos produtos nos anos 2024 e 2025. As colunas contidas no arquivo são as seguintes:

- **produtos**: Nome do produto agrícola
- **preco_2024**: Preço em 2024
- **preco_2025**: Preço em 2025

```python
import pandas as pd

# Carregar os dados
file_path = "Arquivos/produtos_agro.csv"
df = pd.read_excel(file_path)
print(df.head())
```

---

### 📝 Transform

Agora que já temos os dados carregados na fase de Extração, podemos calcular as estimativas para 2026 utilizando operações matemáticas com o pandas:

**Cenário Otimista:** Aplicamos um aumento de 20% sobre o preço de 2025
```python
df['estimativa_2026_otimista'] = df['preco_2025'] * 1.20
```

**Cenário Pessimista:** Aplicamos uma redução de 15% sobre o preço de 2025
```python
df['estimativa_2026_pessimista'] = df['preco_2025'] * 0.85
```

Após calcular as estimativas, selecionamos apenas as colunas relevantes e renomeamos para melhor legibilidade:

```python
df_transformado = df[['produtos', 'estimativa_2026_otimista', 'estimativa_2026_pessimista']]
df_transformado = df_transformado.rename(columns={
    'produtos': 'Produtos',
    'estimativa_2026_otimista': 'Estimativa Otimista 2026',
    'estimativa_2026_pessimista': 'Estimativa Pessimista 2026'
})
```

---

### 📊 Load

Nessa etapa vamos salvar os dados transformados em um novo arquivo CSV e criar um gráfico que possa ser visualizado em tela. Para isso, vou utilizar a biblioteca Matplotlib.

```python
import matplotlib.pyplot as plt

# Exportar para CSV
df_transformado.to_csv('estimativas_precos_2026.csv', index=False)

# Criar gráfico comparativo
fig, ax = plt.subplots(figsize=(12, 6))
x = range(len(df_transformado))
width = 0.35

ax.bar([i - width/2 for i in x], df_transformado['Estimativa Otimista 2026'], width, label='Otimista (+20%)')
ax.bar([i + width/2 for i in x], df_transformado['Estimativa Pessimista 2026'], width, label='Pessimista (-15%)')

plt.title('Estimativas de Preços para 2026', fontsize=14, fontweight='bold')
plt.xlabel('Produtos', fontsize=12)
plt.ylabel('Preço Estimado (R$)', fontsize=12)
plt.xticks(x, df_transformado['Produtos'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('grafico_estimativas_2026.png', dpi=300)
plt.show()
```

---

## 🧰 Ferramentas utilizadas

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c.svg?style=for-the-badge&logo=Matplotlib&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032.svg?style=for-the-badge&logo=Git&logoColor=white)

---

## 📁 Arquivos do Projeto

- **etl_Python.py** - Script principal do pipeline ETL
- **produtos_agro.csv** - Arquivo de entrada com dados de preços 2024-2025
- **estimativas_precos_2026.csv** - Arquivo de saída com estimativas calculadas
- **grafico_estimativas_2026.png** - Visualização gráfica dos resultados
- **readme.md** - Este arquivo de documentação

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação das Dependências

```bash
pip install pandas matplotlib openpyxl
```

### Executar o Projeto

```bash
cd "ETL com Python"
python Arquivos/etl_Python.py
```

### Saída Esperada

O script irá:
1. ✅ Carregar os dados do arquivo de entrada
2. ✅ Exibir as primeiras 5 linhas dos dados originais
3. ✅ Calcular as estimativas otimista e pessimista
4. ✅ Exibir os dados transformados
5. ✅ Gerar arquivo CSV: `estimativas_precos_2026.csv`
6. ✅ Gerar gráfico PNG: `grafico_estimativas_2026.png`
7. ✅ Exibir o gráfico na tela

---

## 📊 Exemplo de Dados

### Dados de Entrada
| produtos | preco_2024 | preco_2025 |
|----------|-----------|-----------|
| Soja (saca 60kg) | 165 | 173.25 |
| Milho (saca 60kg) | 75 | 78.75 |
| Arroz (saca 50kg) | 58 | 60.90 |

### Dados de Saída
| Produtos | Estimativa Otimista 2026 | Estimativa Pessimista 2026 |
|----------|--------------------------|--------------------------|
| Soja (saca 60kg) | 207.90 | 147.26 |
| Milho (saca 60kg) | 94.50 | 66.94 |
| Arroz (saca 50kg) | 73.08 | 51.77 |

---

## 📚 Conceitos Aprendidos

✅ Fundamentos de Python e Pandas  
✅ Extração de dados de múltiplas fontes  
✅ Transformação e limpeza de dados  
✅ Análise e cálculo de estatísticas  
✅ Visualização de dados com Matplotlib  
✅ Exportação de dados processados  
✅ Construção de um pipeline ETL completo  

---

## 🔗 Referências

- [Documentação Pandas](https://pandas.pydata.org/)
- [Documentação Matplotlib](https://matplotlib.org/)
- [Documentação Python](https://docs.python.org/3/)
- [Bootcamp Santander](https://www.santander.com.br/)

---

**Desenvolvido como desafio do Santander Bootcamp 2025 - Ciência de Dados com Python**

Data: 19 de janeiro de 2026

