import matplotlib as plt
import streamlit as st
from PIL import Image
import pandas as pd

def grafico_estudantes(nome_IES, IES, nome_CURSO, CURSO, dados1, escolha_graficos):

  if(len(escolha_graficos) == 0):
    st.subheader('')
    st.error('É necessária a escolha de pelo menos uma opção de gráfico. Por favor, tente novamente.')
  else:
    if(len(escolha_graficos) == 1):
      titulo = st.header('Gerando o Gráfico...')  
    if(len(escolha_graficos) > 1):
      titulo = st.header('Gerando os Gráficos...')

    if('Situações' in escolha_graficos):

        x1 = [1, 2, 3, 4, 5, 6, 7]
        y_masculino1 = []
        y_feminino1 = []

        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1)]['TP_SEXO'].count())
        y_masculino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2)]['TP_SEXO'].count())
        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
        y_masculino1.append( dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 7)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 7)]['TP_SITUACAO'].count())

        maiorcount = 0
        if(max(y_masculino1) > maiorcount):
          maiorcount = max(y_masculino1)
          if(max(y_feminino1) > max(y_masculino1)):
            maiorcount = max(y_feminino1)

        if maiorcount > 500:
          n = 50
        else:
          n = 25

        fig1 = plt.figure(figsize=(12, 8))
        plt.rcParams['hatch.linewidth'] = 0.4
        for i in range(0, len(x1), 1):
          plt.bar(x1[i]-0.2, y_masculino1[i], 0.4, color = 'turquoise', hatch = '/', edgecolor = 'black')
          plt.text(x1[i]-0.2, y_masculino1[i], f'\n{y_masculino1[i]}\n', ha = 'center')
          plt.bar(x1[i]+0.2, y_feminino1[i], 0.4, color = 'salmon', hatch = 'x', edgecolor = 'black')
          plt.text(x1[i]+0.2, y_feminino1[i], f'\n{y_feminino1[i]}\n', ha = 'center')

        plt.xticks(x1, ['Total', 'Cursando', 'Matricula\nTrancada', 'Desvinculados', 'Transferidos', 'Formados', 'Falecidos'])
        plt.yticks(range(0, maiorcount+100, n))
        plt.title(f'\nQuantidade de Estudantes entre Homens e Mulheres por Situações no Curso de\n{nome_CURSO} da {nome_IES} no Ano de 2019\n', fontsize = 14)
        plt.legend(['Homens', 'Mulheres'], prop={'size':14})

    if('Cor/Raça' in escolha_graficos):

      x2 = [1, 2, 3, 4, 5, 6, 7, 8]
      y_masculino2 = []
      y_feminino2 = []

      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())

      maiorcount = 0
      if(max(y_masculino2) > maiorcount):
        maiorcount = max(y_masculino2)
        if(max(y_feminino2) > max(y_masculino2)):
          maiorcount = max(y_feminino2)

      if maiorcount > 500:
        n = 50
      else:
        n = 25

      fig2 = plt.figure(figsize=(12, 8))
      plt.rcParams['hatch.linewidth'] = 0.4
      for i in range(0, len(x2), 1):
        plt.bar(x2[i]-0.2, y_masculino2[i], 0.4, color = 'turquoise', hatch = '/', edgecolor = 'black')
        plt.text(x2[i]-0.2, y_masculino2[i], f'\n{y_masculino2[i]}\n', ha = 'center')
        plt.bar(x2[i]+0.2, y_feminino2[i], 0.4, color = 'salmon', hatch = 'x', edgecolor = 'black')
        plt.text(x2[i]+0.2, y_feminino2[i], f'\n{y_feminino2[i]}\n', ha = 'center')

      plt.xticks(x2, ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Quis\nDeclarar', 'Não Informado'])
      plt.yticks(range(0, maiorcount+100, n))
      plt.title(f'\nQuantidade de Estudantes entre Homens e Mulheres por Cor/Raça no Curso de\n{nome_CURSO} da {nome_IES} no Ano de 2019\n', fontsize = 14)
      plt.legend(['Homens', 'Mulheres'], prop={'size':14})

    if('Idades' in escolha_graficos):

      x3 = [1, 2, 3, 4, 5, 6, 7]
      y_masculino3 = []
      y_feminino3 = []

      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] <= 20)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] <= 20)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 21) & (dados1['NU_IDADE'] <= 24)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 21) & (dados1['NU_IDADE'] <= 24)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 25) & (dados1['NU_IDADE'] <= 28)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 25) & (dados1['NU_IDADE'] <= 28)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 29) & (dados1['NU_IDADE'] <= 32)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 29) & (dados1['NU_IDADE'] <= 32)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 33) & (dados1['NU_IDADE'] <= 36)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 33) & (dados1['NU_IDADE'] <= 36)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 37)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['CO_IES'] == IES) & (dados1['CO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 37)]['TP_SEXO'].count())

      maiorcount = 0
      if(max(y_masculino3) > maiorcount):
        maiorcount = max(y_masculino3)
        if(max(y_feminino3) > max(y_masculino3)):
          maiorcount = max(y_feminino3)

      if maiorcount > 500:
        n = 50
      else:
        n = 25

      fig3 = plt.figure(figsize = (12, 8))
      plt.rcParams['hatch.linewidth'] = 0.4
      for i in range(0, len(x3), 1):
        plt.bar(x3[i]-0.2, y_masculino3[i], 0.4, color = 'turquoise', hatch = '/', edgecolor = 'black')
        plt.text(x3[i]-0.2, y_masculino3[i], f'{y_masculino3[i]}\n', ha = 'center')
        plt.bar(x3[i]+0.2, y_feminino3[i], 0.4, color = 'salmon', hatch = 'X', edgecolor = 'black')
        plt.text(x3[i]+0.2, y_feminino3[i], f'{y_feminino3[i]}\n', ha = 'center')

      plt.xlabel('\nIdades\n')
      plt.ylabel('\nEstudantes\n')
      plt.xticks(x3, ['Total', 'Até 20', '21 até 24', '25 até 28', '29 até 32', '33 até 36', 'Mais que 36'])
      plt.yticks(range(0, maiorcount+100, n))
      plt.title(f'\nQuantidade de Estudantes entre Homens e Mulheres por Idades no Curso de\n{nome_CURSO} da {nome_IES} no Ano de 2019\n', fontsize = 14)
      plt.legend(['Homens', 'Mulheres'], prop={'size':14})

    titulo.empty()
    if(len(escolha_graficos) == 1):
      st.header('Gráfico (Estudantes):') 
    if(len(escolha_graficos) > 1):
      st.header('Gráficos (Estudantes):')
    if('Situações' in escolha_graficos):
      st.subheader('')
      st.pyplot(fig1)
    if('Cor/Raça' in escolha_graficos):
      st.subheader('')
      st.pyplot(fig2)
    if('Idades' in escolha_graficos):
      st.subheader('')
      st.pyplot(fig3)
    st.subheader('')
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
        pagina_inicial()

def grafico_professores(nome_IES, IES, dados2, escolha_graficos):

  if(len(escolha_graficos) == 0):
    st.subheader('')
    st.error('É necessária a escolha de pelo menos uma opção de gráfico. Por favor, tente novamente.')
  else:
    if('Situações' in escolha_graficos):

      x1 = [1, 2, 3, 4, 5, 6, 7]
      y_masculino1 = []
      y_feminino1 = []

      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 1)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 1)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())

      maiorcount = 0
      if(max(y_masculino1) > maiorcount):
        maiorcount = max(y_masculino1)
        if(max(y_feminino1) > max(y_masculino1)):
          maiorcount = max(y_feminino1)

      if maiorcount > 1000:
        n = 100
      else:
        n = 50

      fig1 = plt.figure(figsize=(12, 8))
      plt.rcParams['hatch.linewidth'] = 0.4
      for i in range(0, len(x1), 1):
        plt.bar(x1[i]-0.2, y_masculino1[i], 0.4, color = 'turquoise', hatch = '/', edgecolor = 'black')
        plt.text(x1[i]-0.2, y_masculino1[i], f'\n{y_masculino1[i]}\n', ha = 'center')
        plt.bar(x1[i]+0.2, y_feminino1[i], 0.4, color = 'salmon', hatch = 'x', edgecolor = 'black')
        plt.text(x1[i]+0.2, y_feminino1[i], f'\n{y_feminino1[i]}\n', ha = 'center')

      plt.xticks(x1, ['Total', 'Em Exerxíxio', 'Em Qualificação', 'Em Outra\nEntidade', 'Afastados\n(Saúde)', 'Afastados\n(Outros)', 'Falecidos'])
      plt.yticks(range(0, maiorcount+200, n))
      plt.title(f'\nQuantidade de Professores entre Homens e Mulheres por Situações da {nome_IES} no Ano de 2019\n', fontsize = 14)
      plt.legend(['Homens', 'Mulheres'], prop={'size':14})

    if('Cor/Raça' in escolha_graficos):

      x2 = [1, 2, 3, 4, 5, 6, 7, 8]
      y_masculino2 = []
      y_feminino2 = []

      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())

      maiorcount = 0
      if(max(y_masculino2) > maiorcount):
        maiorcount = max(y_masculino2)
        if(max(y_feminino2) > max(y_masculino2)):
          maiorcount = max(y_feminino2)

      if maiorcount > 1000:
        n = 100
      else:
        n = 50

      fig2 = plt.figure(figsize=(12, 8))
      plt.rcParams['hatch.linewidth'] = 0.4
      for i in range(0, len(x2), 1):
        plt.bar(x2[i]-0.2, y_masculino2[i], 0.4, color = 'turquoise', hatch = '/', edgecolor = 'black')
        plt.text(x2[i]-0.2, y_masculino2[i], f'\n{y_masculino2[i]}\n', ha = 'center')
        plt.bar(x2[i]+0.2, y_feminino2[i], 0.4, color = 'salmon', hatch = 'x', edgecolor = 'black')
        plt.text(x2[i]+0.2, y_feminino2[i], f'\n{y_feminino2[i]}\n', ha = 'center')

      plt.xticks(x2, ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Quis\nDeclarar', 'Não Informado'])
      plt.yticks(range(0, maiorcount+200, n))
      plt.title(f'\nQuantidade de Professores entre Homens e Mulheres por Cor/Raça da {nome_IES} no Ano de 2019\n', fontsize = 14)
      plt.legend(['Homens', 'Mulheres'], prop={'size':14})

    if('Idades' in escolha_graficos):

      x3 = [1, 2, 3, 4, 5, 6, 7]
      y_masculino3 = []
      y_feminino3 = []

      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] <= 30)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] <= 30)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 31) & (dados2['NU_IDADE'] <= 34)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 31) & (dados2['NU_IDADE'] <= 34)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 35) & (dados2['NU_IDADE'] <= 38)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 35) & (dados2['NU_IDADE'] <= 38)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 39) & (dados2['NU_IDADE'] <= 42)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 39) & (dados2['NU_IDADE'] <= 42)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 43) & (dados2['NU_IDADE'] <= 46)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 43) & (dados2['NU_IDADE'] <= 46)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 47)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['CO_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 47)]['TP_SEXO'].count())

      maiorcount = 0
      if(max(y_masculino3) > maiorcount):
        maiorcount = max(y_masculino3)
        if(max(y_feminino3) > max(y_masculino3)):
          maiorcount = max(y_feminino3)

      if maiorcount > 1000:
        n = 100
      else:
        n = 50

      fig3 = plt.figure(figsize = (12, 8))
      plt.rcParams['hatch.linewidth'] = 0.4
      for i in range(0, len(x3), 1):
        plt.bar(x3[i]-0.2, y_masculino3[i], 0.4, color = 'turquoise', hatch = '/', edgecolor = 'black')
        plt.text(x3[i]-0.2, y_masculino3[i], f'{y_masculino3[i]}\n', ha = 'center')
        plt.bar(x3[i]+0.2, y_feminino3[i], 0.4, color = 'salmon', hatch = 'X', edgecolor = 'black')
        plt.text(x3[i]+0.2, y_feminino3[i], f'{y_feminino3[i]}\n', ha = 'center')

      plt.xlabel('\nIdades\n')
      plt.ylabel('\nProfessores\n')
      plt.xticks(x3, ['Total', 'Até 30', '31 até 34', '35 até 38', '39 até 42', '43 até 46', 'Mais que 46'])
      plt.yticks(range(0, maiorcount+200, 50))
      plt.title(f'\nQuantidade de Professores entre Homens e Mulheres por Idades da {nome_IES} no Ano de 2019\n', fontsize = 14)
      plt.legend(['Homens', 'Mulheres'], prop={'size':14})

    if(len(escolha_graficos) == 1):
      st.header('Gráfico (Professores):') 
    if(len(escolha_graficos) > 1):
      st.header('Gráficos (Professores):')
    if('Situações' in escolha_graficos):
      st.subheader('')
      st.pyplot(fig1)
    if('Cor/Raça' in escolha_graficos):
      st.subheader('')
      st.pyplot(fig2)
    if('Idades' in escolha_graficos):
      st.subheader('')
      st.pyplot(fig3)
    st.subheader('')
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
        pagina_inicial()

def pagina_inicial(dados1, dados2):

  titulo = st.title('Analisador Gráfico do Censo da Educação Superior de 2019')
  espaco1 = st.subheader('')
  sobre = st.header('Sobre:')
  descricao1 = st.subheader('O site realiza análises gráficas dos dados do Censo da Educação Superior de 2019, comparando a quantidade de estudantes e professores entre homens e mulheres presentes nos cursos e instituições de ensino superior do Brasil.')
  descricao2 = st.subheader('Desenvolvido por Guilherme Tomaselli Borchardt, junto ao grupo de Iniciação Científica sobre Evasão Escolar, orientado pela professora Isabela Gasparini e pertencente à Universidade do Estado de Santa Catarina (CCT).')
  st.sidebar.title('Opções:')
  escolha = st.sidebar.selectbox('O que deseja analisar:', ('Estudantes', 'Professores'))
  if(escolha == 'Estudantes'):
    escolha_IES = st.sidebar.selectbox('Qual IES deseja analisar:', ('UDESC', 'UFSC', 'Outra'))
    estudantes(titulo, espaco1, sobre, descricao1, descricao2, escolha_IES, dados1)
  if(escolha == 'Professores'):
    escolha_IES = st.sidebar.selectbox('Qual IES deseja analisar:', ('UDESC', 'UFSC', 'Outra'))
    professores(titulo, espaco1, sobre, descricao1, descricao2, escolha_IES, dados2)

def ajuda(titulo, espaco1, sobre, descricao1, descricao2):
  titulo.empty()
  espaco1.empty()
  sobre.empty()
  descricao1.empty()
  descricao2.empty()
  st.header('Ajuda:')
  st.subheader('1) Todos os códigos solicitados (Código da IES e Código do Curso), podem ser encontrados acessando o seguinte site: https://emec.mec.gov.br/')
  st.subheader('')
  st.subheader("2) Após acessar o site, clique na opção curso de graduação, como indicado na imagem abaixo:")
  st.subheader('')
  image1 = Image.open('Imagem1.jpg')
  st.image(image1)
  st.subheader('3) Agora preencha os dois campos indicados na imagem, com a sigla ou nome da instituição de ensino e também com o nome do curso que deseja analisar.')
  st.subheader('')
  image2 = Image.open('Imagem2.jpg')
  st.image(image2)
  st.subheader('4) Informe a localização da instituição de ensino, a qual o curso que deseja analisar está inserido.')
  st.subheader('')
  image6 = Image.open('Imagem6.jpg')
  st.image(image6)
  st.subheader('5) Com os dados sobre a instituição de ensino e curso preenchidos, determine as seguintes informações mostradas na imagem abaixo:')
  st.subheader('')
  image3 = Image.open('Imagem3.jpg')
  st.image(image3)
  st.subheader('6) Enfim, com todos os campos necessários devidamente preenchidos, apenas escreva o código de verificação e em seguida clique em pesquisar.')
  st.subheader('')
  image4 = Image.open('Imagem4.jpg')
  st.image(image4)
  st.subheader('7) Os códigos procurados aparecerão no final da página, como no exemplo abaixo, onde o código da instituição é o número 43 e o código do curso é o 54520.')
  st.subheader('')
  image5 = Image.open('Imagem5.jpg')
  st.image(image5)       
  st.subheader('')
  button_pagina_incical = st.button('Página Inicial')
  if(button_pagina_incical):
    pagina_inicial()

def estudantes(titulo, espaco1, sobre, descricao1, descricao2, escolha_IES, dados1):

  if(escolha_IES == 'UDESC'):
    codigo_IES = 43
    escolha_CURSO = st.sidebar.selectbox('Qual curso deseja analisar:', ('Administração Pública (BC)', 'Administração Pública (Florianópolis)', 'Agronomia', 'Arquitetura e Urbanismo', 'Artes Visuais', 'Biblioteconomia', 'Ciência da Computação', 'Ciências Biológicas (Biodiversidade)', 'Ciências Biológicas (Biol. Marinha)', 'Ciências Contábeis', 'Ciências Econômicas', 'Design Gráfico', 'Design Industrial', 'Educação Física', 'Enfermagem', 'Engenharia Ambiental e Sanitária', 'Engenharia Civil (Ibirama)', 'Engenharia Civil (Joinville)', 'Engenharia de Alimentos', 'Engenharia de Pesca', 'Engenharia de Petróleo', 'Engenharia de Produção e Sistemas', 'Engenharia de Software', 'Engenharia Elétrica', 'Engenharia Florestal', 'Engenharia Mecânica', 'Engenharia Química', 'Engenharia Sanitária', 'Fisioterapia', 'Geografia', 'História', 'Licenciatura em Artes Visuais', 'Licenciatura em Educação Física', 'Licenciatura em Física', 'Licenciatura em Geografia', 'Licenciatura em História', 'Licenciatura em Matemática', 'Licenciatura em Música', 'Licenciatura em Química', 'Licenciatura em Teatro', 'Medicina Veterinária', 'Moda', 'Música (Piano)', 'Música (Violão)', 'Música (Violino e Viola)', 'Música (Violoncelo)', 'Pedagogia', 'Tecnologia em Análise e Desenvolvimento de Sistemas', 'Zootecnia'))
    escolha_graficos = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
    if(escolha_CURSO == 'Administração Pública (BC)'):
      codigo_CURSO = 1287475
    if(escolha_CURSO == 'Administração Pública (Florianópolis)'):
      codigo_CURSO = 117348
    if(escolha_CURSO == 'Agronomia'):
      codigo_CURSO = 2536
    if(escolha_CURSO == 'Arquitetura e Urbanismo'):
      codigo_CURSO = 112414
    if(escolha_CURSO == 'Artes Visuais'):
      codigo_CURSO = 117350
    if(escolha_CURSO == 'Biblioteconomia'):
      codigo_CURSO = 2531
    if(escolha_CURSO == 'Ciência da Computação'):
      codigo_CURSO = 54520
    if(escolha_CURSO == 'Ciências Biológicas (Biodiversidade)'):
      codigo_CURSO = 1363761
    if(escolha_CURSO == 'Ciências Biológicas (Biol. Marinha)'):
      codigo_CURSO = 1357571
    if(escolha_CURSO == 'Ciências Contábeis'):
      codigo_CURSO = 53596
    if(escolha_CURSO == 'Ciências Econômicas'):
      codigo_CURSO = 113291
    if(escolha_CURSO == 'Design Gráfico'):
      codigo_CURSO = 54163
    if(escolha_CURSO == 'Design Industrial'):
      codigo_CURSO = 54162
    if(escolha_CURSO == 'Educação Física'):
      codigo_CURSO = 123128
    if(escolha_CURSO == 'Enfermagem'):
      codigo_CURSO = 74136
    if(escolha_CURSO == 'Engenharia Ambiental e Sanitária'):
      codigo_CURSO = 113289
    if(escolha_CURSO == 'Engenharia Civil (Ibirama)'):
      codigo_CURSO = 1442124
    if(escolha_CURSO == 'Engenharia Civil (Joinville)'):
      codigo_CURSO = 2538
    if(escolha_CURSO == 'Engenharia de Alimentos'):
      codigo_CURSO = 81544
    if(escolha_CURSO == 'Engenharia de Pesca'):
      codigo_CURSO = 1147471
    if(escolha_CURSO == 'Engenharia de Petróleo'):
      codigo_CURSO = 1178687
    if(escolha_CURSO == 'Engenharia de Produção e Sistemas'):
      codigo_CURSO = 82192
    if(escolha_CURSO == 'Engenharia de Software'):
      codigo_CURSO = 1267253
    if(escolha_CURSO == 'Engenharia Elétrica'):
      codigo_CURSO = 2534
    if(escolha_CURSO == 'Engenharia Florestal'):
      codigo_CURSO = 81538
    if(escolha_CURSO == 'Engenharia Mecânica'):
      codigo_CURSO = 2537
    if(escolha_CURSO == 'Engenharia Quimíca'):
      codigo_CURSO = 1327406
    if(escolha_CURSO == 'Engenharia Sanitária'):
      codigo_CURSO = 1149596
    if(escolha_CURSO == 'Fisioterapia'):
      codigo_CURSO = 2544
    if(escolha_CURSO == 'Geografia'):
      codigo_CURSO = 302541
    if(escolha_CURSO == 'História'):
      codigo_CURSO = 302540
    if(escolha_CURSO == 'Licenciatura em Artes Visuais'):
      codigo_CURSO = 117352
    if(escolha_CURSO == 'Licenciatura em Educação Física'):
      codigo_CURSO = 123124
    if(escolha_CURSO == 'Licenciatura em Física'):
      codigo_CURSO = 2545
    if(escolha_CURSO == 'Licenciatura em Geografia'):
      codigo_CURSO = 2541
    if(escolha_CURSO == 'Licenciatura em História'):
      codigo_CURSO = 2540
    if(escolha_CURSO == 'Licenciatura em Matemática'):
      codigo_CURSO = 113295
    if(escolha_CURSO == 'Licenciatura em Música'):
      codigo_CURSO = 92200
    if(escolha_CURSO == 'Licenciatura em Química'):
      codigo_CURSO = 1147485
    if(escolha_CURSO == 'Licenciatura em Teatro'):
      codigo_CURSO = 107850
    if(escolha_CURSO == 'Medicina Veterinária'):
      codigo_CURSO = 2535
    if(escolha_CURSO == 'Moda'):
      codigo_CURSO = 2547
    if(escolha_CURSO == 'Música (Piano)'):
      codigo_CURSO = 33323
    if(escolha_CURSO == 'Música (Violão)'):
      codigo_CURSO = 96661
    if(escolha_CURSO == 'Música (Violino e Viola)'):
      codigo_CURSO = 31468
    if(escolha_CURSO == 'Música (Violoncelo)'):
      codigo_CURSO = 123137
    if(escolha_CURSO == 'Pedagogia'):
      codigo_CURSO = 2529
    if(escolha_CURSO == 'Tecnologia em Análise e Desenvolvimento de Sistemas'):
      codigo_CURSO = 62742
    if(escolha_CURSO == 'Zootecnia'):
      codigo_CURSO = 74134
    button_gerar = st.sidebar.button('Gerar Gráficos')
    if(button_gerar):
      titulo.empty()
      espaco1.empty()
      sobre.empty()
      descricao1.empty()
      descricao2.empty()
      grafico_estudantes(escolha_IES, codigo_IES, escolha_CURSO, codigo_CURSO, dados1, escolha_graficos)

  if(escolha_IES == 'UFSC'):
    codigo_IES = 585
    escolha_CURSO = st.sidebar.selectbox('Qual curso deseja analisar:', ('Administração', 'Agronomia (Curitibanos)', 'Agronomia (Florianópolis)', 'Animação', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes Cênicas', 'Biblioteconomia', 'Ciência da Informação', 'Ciência e Tecnologia', 'Ciência e Tecnologia de Alimentos', 'Ciências Biológicas', 'Ciências Contábeis (A Distância)', 'Ciências Contábeis (Presencial)', 'Ciências da Computação', 'Ciências Econômicas (A Distância)', 'Ciências Econômicas (Presencial)', 'Ciências Sociais', 'Cinema', 'Design', 'Design de Produto', 'Direito', 'Educação Física', 'Enfermagem', 'Engenharia Aeroespacial', 'Engenharia Automotiva', 'Engenharia Civil', 'Engenharia Civil de Infraestrutura','Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Computação', 'Eng. de Controle e Automação (Blumenau)', 'Eng. de Controle e Automação (Florianópolis)', 'Engenharia de Energia', 'Engenharia de Materiais (Blumenau)', 'Engenharia de Materiais (Florianópolis)', 'Engenharia de Produção Civil', 'Engenharia de Produção Elétrica', 'Engenharia de Produção Mecânica', 'Eng. de Transporte e Logística', 'Engenharia Elétrica', 'Engenharia Eletrônica', 'Eng. Ferroviária e Metroviária', 'Engenharia Florestal', 'Engenharia Mecânica', 'Engenharia Mecatrônica', 'Engenharia Naval', 'Engenharia Química', 'Engenharia Têxtil', 'Farmácia', 'Filosofia', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Geologia', 'História', 'Jornalismo', 'Letras (Língua Alemã)', 'Letras (Língua Espanhola)', 'Letras (Língua Francesa)', 'Letras (Língua Inglesa)', 'Letras (Língua Italiana)', 'Letras (Língua Portuguesa)', 'Licenciatura em Ciências Sociais', 'Licenciatura em Educação Física', 'Lic. em Filosofia (A Distância)', 'Lic. em Filosofia (Presencial)', 'Licenciatura em Geografia', 'Licenciatura em História', 'Lic. em Letras (Língua Alemã)', 'Lic. em Letras (Língua Francesa)', 'Lic. em Letras (Língua Italiana)', 'Lic. em Matemática (A Distância)', 'Lic. em Matemática (Blumenau)', 'Lic. em Matemática (Florianópolis)', 'Matemática', 'Medicina', 'Medicina Veterinária', 'Meteorologia', 'Museologia', 'Nutrição', 'Oceanografia', 'Odontologia', 'Pedagogia', 'Psicologia', 'Relações Internacionais', 'Secretariado Executivo', 'Serviço Social', 'Zootecnia'))
    escolha_graficos = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
    if(escolha_CURSO == 'Administração'): 
      codigo_CURSO = 14213
    if(escolha_CURSO == 'Agronomia (Curitibanos)'): 
      codigo_CURSO = 1184410
    if(escolha_CURSO == 'Agronomia (Florianópolis)'): 
      codigo_CURSO = 14214
    if(escolha_CURSO == 'Animação'): 
      codigo_CURSO = 1333514
    if(escolha_CURSO == 'Antropologia'): 
      codigo_CURSO = 1115811
    if(escolha_CURSO == 'Arquitetura e Urbanismo'): 
      codigo_CURSO = 14215
    if(escolha_CURSO == 'Arquivologia'): 
      codigo_CURSO = 1108414
    if(escolha_CURSO == 'Artes Cênicas'): 
      codigo_CURSO = 111962
    if(escolha_CURSO == 'Biblioteconomia'): 
      codigo_CURSO = 14216
    if(escolha_CURSO == 'Ciência da Informação'): 
      codigo_CURSO = 1330164
    if(escolha_CURSO == 'Ciência e Tecnologia'):   
      codigo_CURSO = 1084137
    if(escolha_CURSO == 'Ciência e Tecnologia de Alimentos'): 
      codigo_CURSO = 116534
    if(escolha_CURSO == 'Ciências Biológicas'): 
      codigo_CURSO = 314218
    if(escolha_CURSO == 'Ciências Contábeis (A Distância)'): 
      codigo_CURSO = 113467
    if(escolha_CURSO == 'Ciências Contábeis (Presencial)'): 
      codigo_CURSO = 14219
    if(escolha_CURSO == 'Ciências da Computação'): 
      codigo_CURSO = 14217
    if(escolha_CURSO == 'Ciências Econômicas (A Distância)'):   
      codigo_CURSO = 113465
    if(escolha_CURSO == 'Ciências Econômicas (Presencial)'):  
      codigo_CURSO = 14220
    if(escolha_CURSO == 'Ciências Sociais'):   
      codigo_CURSO = 314221
    if(escolha_CURSO == 'Cinema'):   
      codigo_CURSO = 86625
    if(escolha_CURSO == 'Design'):   
      codigo_CURSO = 116526
    if(escolha_CURSO == 'Design de Produto'):   
      codigo_CURSO = 116530
    if(escolha_CURSO == 'Direito'):
      codigo_CURSO = 14223
    if(escolha_CURSO == 'Educação Física'):
      codigo_CURSO = 97099
    if(escolha_CURSO == 'Enfermagem'):
      codigo_CURSO = 14225
    if(escolha_CURSO == 'Engenharia Aeroespacial'):
      codigo_CURSO = 1270287
    if(escolha_CURSO == 'Engenharia Automotiva'):
      codigo_CURSO = 1270297
    if(escolha_CURSO == 'Engenharia Civil'): 
      codigo_CURSO = 14241
    if(escolha_CURSO == 'Engenharia Civil de Infraestrutura'): 
      codigo_CURSO = 1270310
    if(escolha_CURSO == 'Engenharia de Alimentos'): 
      codigo_CURSO = 14226
    if(escolha_CURSO == 'Engenharia de Aquicultura'): 
      codigo_CURSO = 20133
    if(escolha_CURSO == 'Engenharia de Computação'): 
      codigo_CURSO = 1133610
    if(escolha_CURSO == 'Eng. de Controle e Automação (Blumenau)'): 
      codigo_CURSO = 1270376
    if(escolha_CURSO == 'Eng. de Controle e Automação (Florianópolis)'): 
      codigo_CURSO = 14249
    if(escolha_CURSO == 'Engenharia de Energia'): 
      codigo_CURSO = 1105824
    if(escolha_CURSO == 'Engenharia de Materiais (Blumenau)'):  
      codigo_CURSO = 1270375
    if(escolha_CURSO == 'Engenharia de Materiais (Florianópolis)'): 
      codigo_CURSO = 20135
    if(escolha_CURSO == 'Engenharia de Produção Civil'): 
      codigo_CURSO = 35550
    if(escolha_CURSO == 'Engenharia de Produção Elétrica'): 
      codigo_CURSO = 31945
    if(escolha_CURSO == 'Engenharia de Produção Mecânica'): 
      codigo_CURSO = 23960
    if(escolha_CURSO == 'Eng. de Transporte e Logística'): 
      codigo_CURSO = 1270311
    if(escolha_CURSO == 'Engenharia Elétrica'): 
      codigo_CURSO = 14242
    if(escolha_CURSO == 'Engenharia Eletrônica'): 
      codigo_CURSO = 122341
    if(escolha_CURSO == 'Eng. Ferroviária e Metroviária'): 
      codigo_CURSO = 1270303
    if(escolha_CURSO == 'Engenharia Florestal'): 
      codigo_CURSO = 1184098
    if(escolha_CURSO == 'Engenharia Mecânica'): 
      codigo_CURSO = 14243
    if(escolha_CURSO == 'Engenharia Mecatrônica'): 
      codigo_CURSO = 1270305
    if(escolha_CURSO == 'Engenharia Naval'): 
      codigo_CURSO = 1270308
    if(escolha_CURSO == 'Engenharia Química'): 
      codigo_CURSO = 14247
    if(escolha_CURSO == 'Engenharia Têxtil'): 
      codigo_CURSO = 1270377
    if(escolha_CURSO == 'Farmácia'): 
      codigo_CURSO = 14227
    if(escolha_CURSO == 'Filosofia'): 
      codigo_CURSO = 314228
    if(escolha_CURSO == 'Fisioterapia'): 
      codigo_CURSO = 1126962
    if(escolha_CURSO == 'Fonoaudiologia'): 
      codigo_CURSO = 122343
    if(escolha_CURSO == 'Geografia'): 
      codigo_CURSO = 314230
    if(escolha_CURSO == 'Geologia'): 
      codigo_CURSO = 1114547
    if(escolha_CURSO == 'História'): 
      codigo_CURSO = 314231
    if(escolha_CURSO == 'Jornalismo'): 
      codigo_CURSO = 14222
    if(escolha_CURSO == 'Letras (Língua Alemã)'): 
      codigo_CURSO = 351917
    if(escolha_CURSO == 'Letras (Língua Espanhola)'): 
      codigo_CURSO = 351937
    if(escolha_CURSO == 'Letras (Língua Francesa)'): 
      codigo_CURSO = 351938
    if(escolha_CURSO == 'Letras (Língua Inglesa)'): 
      codigo_CURSO = 351941
    if(escolha_CURSO == 'Letras (Língua Italiana)'): 
      codigo_CURSO = 351943
    if(escolha_CURSO == 'Letras (Língua Portuguesa)'): 
      codigo_CURSO = 351945
    if(escolha_CURSO == 'Licenciatura em Ciências Sociais'): 
      codigo_CURSO = 14221
    if(escolha_CURSO == 'Licenciatura em Educação Física'): 
      codigo_CURSO = 14224
    if(escolha_CURSO == 'Lic. em Filosofia (A Distância)'): 
      codigo_CURSO = 113457
    if(escolha_CURSO == 'Lic. em Filosofia (Presencial)'): 
      codigo_CURSO = 14228
    if(escolha_CURSO == 'Licenciatura em Geografia'): 
      codigo_CURSO = 14230
    if(escolha_CURSO == 'Licenciatura em História'): 
      codigo_CURSO = 14231
    if(escolha_CURSO == 'Lic. em Letras (Língua Alemã)'): 
      codigo_CURSO = 51917
    if(escolha_CURSO == 'Lic. em Letras (Língua Francesa)'): 
      codigo_CURSO = 51938
    if(escolha_CURSO == 'Lic. em Letras (Língua Italiana)'): 
      codigo_CURSO = 51943
    if(escolha_CURSO == 'Lic. em Matemática (A Distância)'): 
      codigo_CURSO = 99460
    if(escolha_CURSO == 'Lic. em Matemática (Blumenau)'): 
      codigo_CURSO = 1270371
    if(escolha_CURSO == 'Lic. em Matemática (Florianópolis)'): 
      codigo_CURSO = 14233
    if(escolha_CURSO == 'Matemática'): 
      codigo_CURSO = 25831
    if(escolha_CURSO == 'Medicina'): 
      codigo_CURSO = 14234
    if(escolha_CURSO == 'Medicina Veterinária'):  
      codigo_CURSO = 1175716
    if(escolha_CURSO == 'Meteorologia'): 
      codigo_CURSO = 1169589
    if(escolha_CURSO == 'Museologia'): 
      codigo_CURSO = 1115842
    if(escolha_CURSO == 'Nutrição'): 
      codigo_CURSO = 14235
    if(escolha_CURSO == 'Oceanografia'): 
      codigo_CURSO = 111956
    if(escolha_CURSO == 'Odontologia'): 
      codigo_CURSO = 14236
    if(escolha_CURSO == 'Pedagogia'): 
      codigo_CURSO = 14237
    if(escolha_CURSO == 'Psicologia'): 
      codigo_CURSO = 14238
    if(escolha_CURSO == 'Relações Internacionais'): 
      codigo_CURSO = 116532
    if(escolha_CURSO == 'Secretariado Executivo'): 
      codigo_CURSO = 82368
    if(escolha_CURSO == 'Serviço Social'): 
      codigo_CURSO = 14240
    if(escolha_CURSO == 'Zootecnia'): 
      codigo_CURSO = 111954
    button_gerar = st.sidebar.button('Gerar Gráficos')
    if(button_gerar):
      titulo.empty()
      espaco1.empty()
      sobre.empty()
      descricao1.empty()
      descricao2.empty()
      grafico_estudantes(escolha_IES, codigo_IES, escolha_CURSO, codigo_CURSO, dados1, escolha_graficos)

  if(escolha_IES == 'Outra'): 
    try:
      nome_IES = st.sidebar.text_input('Nome ou sigla da IES:')
      codigo_IES = st.sidebar.text_input('Código da IES:', help = 'Caso não saiba, clique no botão ajuda no final da página.')
      nome_CURSO = st.sidebar.text_input('Nome do Curso:')
      codigo_CURSO = st.sidebar.text_input('Código do Curso:', help = 'Caso não saiba, clique no botão ajuda no final da página.')
      escolha_graficos = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
      button_gerar = st.sidebar.button('Gerar Gráficos')
      button_ajuda = st.sidebar.button('Ajuda')
      if(button_gerar):
        titulo.empty()
        espaco1.empty()
        sobre.empty()
        descricao1.empty()
        descricao2.empty()
        grafico_estudantes(nome_IES, int(codigo_IES), nome_CURSO, int(codigo_CURSO), dados1, escolha_graficos)
      if(button_ajuda):
        ajuda(titulo, espaco1, sobre, descricao1, descricao2)
    except ValueError:
      st.subheader('')
      st.error('Ocorreu algum erro com os dados inseridos. Por favor, tente novamente.')

def professores(titulo, espaco1, sobre, descricao1, descricao2, escolha_IES, dados2):

  if(escolha_IES == 'UDESC'):
    codigo_IES = 43
    escolha_graficos = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
    button_gerar = st.sidebar.button('Gerar Gráficos')
    if(button_gerar):
      titulo.empty()
      espaco1.empty()
      sobre.empty()
      descricao1.empty()
      descricao2.empty()
      grafico_professores(escolha_IES, codigo_IES, dados2, escolha_graficos)
  if(escolha_IES == 'UFSC'):
    codigo_IES = 585
    escolha_graficos = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
    button_gerar = st.sidebar.button('Gerar Gráficos')
    if(button_gerar):
      titulo.empty()
      espaco1.empty()
      sobre.empty()
      descricao1.empty()
      descricao2.empty()
      grafico_professores(escolha_IES, codigo_IES, dados2, escolha_graficos)
  if(escolha_IES == 'Outra'):
    try:
      nome_IES = st.sidebar.text_input('Nome ou sigla da IES:')
      codigo_IES = st.sidebar.text_input('Código da IES:', help = 'Caso não saiba, clique no botão Ajuda.')
      escolha_graficos = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
      button_gerar = st.sidebar.button('Gerar Gráficos')
      button_ajuda = st.sidebar.button('Ajuda')
      if(button_gerar):
        titulo.empty()
        espaco1.empty()
        sobre.empty()
        descricao1.empty()
        descricao2.empty()
        grafico_professores(nome_IES, int(codigo_IES), dados2, escolha_graficos)
      if(button_ajuda):
        ajuda(titulo, espaco1, sobre, descricao1, descricao2)
    except ValueError:
      st.subheader('')
      st.error('Ocorreu algum erro com os dados inseridos. Por favor, tente novamente.')

@st.cache(allow_output_mutation=True, show_spinner=False)
def load_data_alunos():
  dados_alunos1 = pd.read_csv('SUP_ALUNO1.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos2 = pd.read_csv('SUP_ALUNO2.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos3 = pd.read_csv('SUP_ALUNO3.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos4 = pd.read_csv('SUP_ALUNO4.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos5 = pd.read_csv('SUP_ALUNO5.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos6 = pd.read_csv('SUP_ALUNO6.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos7 = pd.read_csv('SUP_ALUNO7.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos8 = pd.read_csv('SUP_ALUNO8.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos9 = pd.read_csv('SUP_ALUNO9.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos10 = pd.read_csv('SUP_ALUNO10.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos11 = pd.read_csv('SUP_ALUNO11.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos12 = pd.read_csv('SUP_ALUNO12.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos13 = pd.read_csv('SUP_ALUNO13.CSV', sep='|', encoding='ISO-8859-1')
  dados_alunos = pd.concat([dados_alunos1, dados_alunos2, dados_alunos3, dados_alunos4, dados_alunos5, dados_alunos6, dados_alunos7, dados_alunos8, dados_alunos9, dados_alunos10, dados_alunos11, dados_alunos12, dados_alunos13])
  return dados_alunos

@st.cache(allow_output_mutation=True, show_spinner=False)
def load_data_professores():
  dados_professores = pd.read_csv('SUP_DOCENTE_2019.CSV', sep='|', encoding='ISO-8859-1')
  return dados_professores

if __name__ == '__main__':

  st.set_page_config(page_title='Analisador Educacional')
  titulo_inicial = st.title('Realizando a Leitura dos Dados...')
  espaco_inicial = st.subheader('')
  descricao_inicial = st.subheader('Por favor aguarde um momento, a aplicação já irá iniciar.')
  dados1 = load_data_alunos()
  dados2 = load_data_professores()
  titulo_inicial.empty()
  espaco_inicial.empty()
  descricao_inicial.empty()
  pagina_inicial(dados1, dados2)
