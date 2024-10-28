# Importação das bibliotecas
import folium
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Folium: Criando um mapa com marcadores para algumas cidades do Brasil
m = folium.Map(location=[-15.78, -47.93], zoom_start=4)

# Adicionando marcadores
cidades = {
    'São Paulo': [-23.55, -46.63],
    'Rio de Janeiro': [-22.91, -43.17],
    'Belo Horizonte': [-19.92, -43.94],
    'Brasília': [-15.78, -47.93]
}
for cidade, coords in cidades.items():
    folium.Marker(location=coords, popup=cidade).add_to(m)

# Salva o mapa em um arquivo HTML
m.save("mapa_brasil.html")

# 2. Plotly: Gráfico de barras com dados fictícios de população
dados_populacao = pd.DataFrame({
    'Cidade': list(cidades.keys()),
    'População (milhões)': [12.33, 6.72, 2.53, 3.04]
})
fig_plotly = px.bar(dados_populacao, x='Cidade', y='População (milhões)', title="População de Cidades do Brasil")
fig_plotly.show()

# 3. Matplotlib: Gráfico de linha para crescimento populacional ao longo dos anos
anos = [2000, 2005, 2010, 2015, 2020, 2025]
populacao = [1.5, 1.8, 2.2, 2.6, 3.1, 3.5]  # População em milhões (dados fictícios)
plt.plot(anos, populacao, marker='o')
plt.title("Crescimento Populacional de Cidade Fictícia")
plt.xlabel("Ano")
plt.ylabel("População (milhões)")
plt.grid(True)
plt.show()

# 4. Seaborn: Gráfico de dispersão para dados fictícios de renda versus idade
dados_ficticios = pd.DataFrame({
    'Idade': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Renda (mil R$)': [2.5, 3.1, 4.0, 5.2, 6.1, 7.0, 8.1, 7.9, 6.5, 5.2]
})
sns.scatterplot(data=dados_ficticios, x='Idade', y='Renda (mil R$)')
plt.title("Distribuição de Renda por Idade")
plt.show()
