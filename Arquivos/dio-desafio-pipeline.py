import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo Excel
file_path = "Arquivos/produtos_agro.csv"
df = pd.read_excel(file_path)

# Visualizar as primeiras linhas do DataFrame para verificar os dados
print(df.head())

# Calcular a estimativa para 2026 com 20% de aumento sobre preco_2025
df['estimativa_2026_otimista'] = df['preco_2025'] * 1.20

# Calcular a estimativa para 2026 com 15% de decréscimo sobre preco_2025
df['estimativa_2026_pessimista'] = df['preco_2025'] * 0.85

# Selecionar apenas as colunas necessárias
df_transformado = df[['produtos', 'estimativa_2026_otimista', 'estimativa_2026_pessimista']]

# Renomear colunas
df_transformado = df_transformado.rename(columns={
    'produtos': 'Produtos', 
    'estimativa_2026_otimista': 'Estimativa Otimista 2026',
    'estimativa_2026_pessimista': 'Estimativa Pessimista 2026'
})

# Visualizar o DataFrame transformado
print(df_transformado)

# Exportar o DataFrame transformado para um novo arquivo CSV
output_file_path = "estimativas_precos_2026.csv"
df_transformado.to_csv(output_file_path, index=False)
print(f'Dados transformados exportados para {output_file_path}')

# Configurar o gráfico com duas barras lado a lado
fig, ax = plt.subplots(figsize=(12, 6))

x = range(len(df_transformado))
width = 0.35

ax.bar([i - width/2 for i in x], df_transformado['Estimativa Otimista 2026'], width, label='Otimista (+20%)')
ax.bar([i + width/2 for i in x], df_transformado['Estimativa Pessimista 2026'], width, label='Pessimista (-15%)')

# Configurar título e rótulos
plt.title('Estimativas de Preços para 2026', fontsize=14, fontweight='bold')
plt.xlabel('Produtos', fontsize=12)
plt.ylabel('Preço Estimado (R$)', fontsize=12)
plt.xticks(x, df_transformado['Produtos'], rotation=45, ha='right')
plt.legend()

# Mostrar o gráfico e salvar
plt.tight_layout()
plt.savefig('grafico_estimativas_2026.png', dpi=300, bbox_inches='tight')
print('Gráfico salvo como: grafico_estimativas_2026.png')
plt.show()

