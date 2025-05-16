import pandas as pd
import numpy as np

def importar_base():
    despesa_ceaps_2019 = pd.read_csv('despesa_ceaps_2019.csv', sep=';', encoding='latin1')
    despesa_ceaps_2020 = pd.read_csv('despesa_ceaps_2020.csv', sep=';', encoding='latin1')
    despesa_ceaps_2021 = pd.read_csv('despesa_ceaps_2021.csv', sep=';', encoding='latin1')
    despesa_ceaps_2022 = pd.read_csv('despesa_ceaps_2022.csv', sep=';', encoding='latin1')
    
    return despesa_ceaps_2019, despesa_ceaps_2020, despesa_ceaps_2021, despesa_ceaps_2022

despesa_ceaps_2019, despesa_ceaps_2020, despesa_ceaps_2021, despesa_ceaps_2022 = importar_base()

def despesas_ceaps_2019(despesa_ceaps_2019):
    # Redefine o index
    despesa_ceaps_2019.reset_index(inplace=True)
    # Define a primeira linha como cabeçalho
    despesa_ceaps_2019.columns = despesa_ceaps_2019.iloc[0].values
    # Remove a primeira linha agora redundante
    despesa_ceaps_2019 = despesa_ceaps_2019[1:]
    
    return despesa_ceaps_2019

despesa_ceaps_2019 = despesas_ceaps_2019(despesa_ceaps_2019)

def despesas_ceaps_2020(despesa_ceaps_2020):
    # Redefine o index
    despesa_ceaps_2020.reset_index(inplace=True)
    # Define a primeira linha como cabeçalho
    despesa_ceaps_2020.columns = despesa_ceaps_2020.iloc[0].values
    # Remove a primeira linha agora redundante
    despesa_ceaps_2020 = despesa_ceaps_2020[1:]
    
    return despesa_ceaps_2020

despesa_ceaps_2020 = despesas_ceaps_2020(despesa_ceaps_2020)

def despesas_ceaps_2021(despesa_ceaps_2021):
    # Redefine o index
    despesa_ceaps_2021.reset_index(inplace=True)
    # Define a primeira linha como cabeçalho
    despesa_ceaps_2021.columns = despesa_ceaps_2021.iloc[0].values
    # Remove a primeira linha agora redundante
    despesa_ceaps_2021 = despesa_ceaps_2021[1:]
    
    return despesa_ceaps_2021

despesa_ceaps_2021 = despesas_ceaps_2021(despesa_ceaps_2021)

def despesas_ceaps_2022(despesa_ceaps_2022):
    # Redefine o index
    despesa_ceaps_2022.reset_index(inplace=True)
    # Define a primeira linha como cabeçalho
    despesa_ceaps_2022.columns = despesa_ceaps_2022.iloc[0].values
    # Remove a primeira linha agora redundante
    despesa_ceaps_2022 = despesa_ceaps_2022[1:]
    
    return despesa_ceaps_2022

despesa_ceaps_2022 = despesas_ceaps_2022(despesa_ceaps_2022)

def unir_despesas(despesa_ceaps_2019, despesa_ceaps_2020, despesa_ceaps_2021, despesa_ceaps_2022):
    # Cria um dataframe com os dados dos 4 anos
    despesas_ceaps = pd.concat([despesa_ceaps_2019, despesa_ceaps_2020, despesa_ceaps_2021, despesa_ceaps_2022], axis=0)
    # Redefine o index
    despesas_ceaps.reset_index(inplace=True)
    despesas_ceaps = despesas_ceaps.drop(columns=['index'])
    # Redefine o index
    despesas_ceaps = despesas_ceaps.reset_index(drop=True)
    despesas_ceaps['ANO'] = pd.to_datetime(despesas_ceaps['ANO'], format='%Y', errors='coerce').dt.year
    
    return despesas_ceaps

despesas_ceaps = unir_despesas(despesa_ceaps_2019, despesa_ceaps_2020, despesa_ceaps_2021, despesa_ceaps_2022)

def corrigir_formatos(despesas_ceaps):
    # Transforma a coluna de código do documento em números inteiros
    despesas_ceaps['COD_DOCUMENTO'] = despesas_ceaps['COD_DOCUMENTO'].astype(int)
    # Transforma a coluna de valores reembolsados em float
    despesas_ceaps['VALOR_REEMBOLSADO'] = (
        despesas_ceaps['VALOR_REEMBOLSADO']
        .str.replace(',', '.', regex=False)
        .astype(float)
    )
    
    return despesas_ceaps

despesas_ceaps = corrigir_formatos(despesas_ceaps)

def preencher_vazias(despesas_ceaps):
    despesas_ceaps['DETALHAMENTO'] = despesas_ceaps['DETALHAMENTO'].fillna('Despesa não detalhada')
    
    return despesas_ceaps

despesas_ceaps = preencher_vazias(despesas_ceaps)