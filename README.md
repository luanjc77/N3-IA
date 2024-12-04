# Previsão de Preços de Casas 

Este projeto utiliza algoritmos de Regressão Linear e Árvores de Decisão para prever preços de casas com base em dados históricos. O código carrega os dados, divide-os em conjuntos de treinamento e teste, treina dois modelos de aprendizado de máquina e avalia suas performances usando métricas como Mean Squared Error (MSE) e Coeficiente de Determinação (R²).

Requisitos do Projeto
As seguintes bibliotecas Python são necessárias para executar o projeto:

pandas: Manipulação e análise de dados.
    Comando para a instalação: pip install pandas

scikit-learn: Implementação dos algoritmos de aprendizado de máquina e métricas de avaliação.
    Comando para instalação: pip install scikit-learn

Depois de executar os comandos para instalação das bibliotecas, basta executar o comando para a execução do código: python casas.py
Executando este comando, o código irá ler o arquvo CSV que está definido, atualmente está validando o sample_submission.csv, e depois no próprio console irá aparecer os resultados dos algoritimos de Regressçai Linear e da Árvore de Decisão, gerando uma resposta neste formato:

Regressão Linear:
MSE: 220000.00
R²: 0.75

Árvore de Decisão:
MSE: 180000.00
R²: 0.80


