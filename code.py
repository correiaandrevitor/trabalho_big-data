import pandas as pd

# Criar um DataFrame com os dados especificados
df_regioes = pd.DataFrame({
    'sudeste': [111034, 35.1, 88200000],
    'centro-oeste': [27093, 8.6, 17200100],
    'sul': [51546, 16.3, 31300000],
    'nordeste': [98293, 31.0, 57200000],
    'norte': [28261, 9.0, 18800000]
})

# Atribuir nomes aos índices para maior clareza
df_regioes.index = ['N-LEITOS', 'Porcentagens', 'POPULAÇÃO']

# Exibir o DataFrame criado
display(df_regioes)
