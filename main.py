import streamlit as st
import upload as up
import pandas as pd
from slugify import slugify

def processar_formacao_carga(arquivo):
    st.markdown(f'### -> Formação de Carga')
    progresso = st.progress(0, 'Lendo arquivo...')

    try: 
        data_frame = pd.read_excel(arquivo, header=2, skipfooter=1)
    except Exception as e:
        progresso.empty()
        st.error(f'Erro ao abrir arquivo. Erro: {e}')
        return

    progresso.progress(1/4, 'Validando planilha...')

    try:
        up.validar_planilha(
            data_frame, 
            ['Empresa', 'Dt. Neg.', 'Nome Fantasia (Empresa Negociação)', 'Local',
            'Caixa', 'Nro. Único', 'Parceiro', 'Nome Parceiro (Parceiro)',
            'Vlr. Nota', 'Nome Cidade (Parceiro)', 'Ordem de carga',
            'Sequência da carga', 'Apelido', 'Peso a Entregar', 'Região (Cidade)',
            'Descrição (Tipo de Operação)', 'Tipo de entrega', 'ENTREGUE',
            'Tipo Operação', 'OBSERVAÇÃO COMERCIAL 2',
            'Cód. Região Cidade (Parceiro)'
            ],
            ['Dt. Neg.' ]
        )
    except Exception as e:
        progresso.empty()
        st.error(f'Planilha inválida. Erro: {e}')
        return
    
    data_frame.columns = [slugify(column, separator='_') for column in data_frame.columns.to_list()]
    
    progresso.progress(2/4, 'Filtrando Registros...')

    try:
        novos_dados = up.filtrar_novos_dados(data_frame, "formacao_de_carga_megaferro", 'nro_unico')
    except Exception as e:
        progresso.empty()
        st.error(f'Erro ao se conectar ao banco de dados. Erro: {e}')
        return

    if novos_dados.empty:
        progresso.empty()
        st.warning('Não há dados novos na planilha')
        return

    progresso.progress(3/4, 'Enviando Dados...')

    try:
        up.adicionar_registros(novos_dados, 'formacao_de_carga_megaferro')
        progresso.progress(4/4, 'Finalizado!')
        progresso.empty()
        st.success(f'Base de dados atualizada com sucesso! {len(novos_dados)} registros adicionados')
    except Exception as e:
        progresso.empty()
        st.warning(f'Houve um erro ao enviar dados. Erro: {e}')
        return

def processar_portal_vendas(arquivo):
    st.markdown(f'### -> Portal de Vendas')
    progresso = st.progress(0, 'Lendo arquivo...')

    try: 
        data_frame = pd.read_excel(arquivo, header=2, skipfooter=1)
    except Exception as e:
        progresso.empty()
        st.error(f'Erro ao abrir arquivo. Erro: {e}')
        return

    progresso.progress(1/4, 'Validando planilha...')

    try:
        up.validar_planilha(
            data_frame, 
            ['Empresa', 'Dt. do Faturamento', 'Ordem de carga', 'Status NF-e',
            'Nro. Único', 'Nro. Nota', 'Parceiro', 'Nome Parceiro (Parceiro)',
            'Valor', 'Descrição (Tipo de Negociação)', 'Peso', 'ENTREGUE',
            'NOME RÁPIDO', 'Vendedor', 'Apelido (Vendedor)', 'Vlr. Nota',
            'Descrição (Tipo de Pedido)', 'Descrição (Tipo de Operação)',
            'Status da Nota', 'Nome (Usuário Alteração)', 'Anular Comissão',
            'Comissão', 'Confirmada', 'Cód. Usuário', 'Cód. Usuário Inclusão',
            'Nome (Usuário Inclusão)', 'Número Pedido',
            'Indicador de Presença para NF-e/NFC-e', 'Status NFS-e', 'Liberação',
            'Dt. Neg.', 'Nome Fantasia (Empresa)', 'Apelido (Vendedor Técnico)',
            'Tipo Operação', 'Tipo Negociação', 'Natureza', 'Descrição (Natureza)',
            'Centro Resultado', 'Descrição (Centro de Resultado)',
            'Vlr. da Substituição', 'Vlr. do ICMS'],
            ['Dt. do Faturamento', 'Dt. Neg.']
        )
    except Exception as e:
        progresso.empty()
        st.error(f'Planilha inválida. Erro: {e}')
        return
    
    data_frame.columns = [slugify(column, separator='_') for column in data_frame.columns.to_list()]

    progresso.progress(2/4, 'Filtrando Registros...')

    try:
        novos_dados = up.filtrar_novos_dados(data_frame, "portal_de_vendas_megaferro", 'nro_nota')
    except Exception as e:
        progresso.empty()
        st.error(f'Erro ao se conectar ao banco de dados. Erro: {e}')
        return

    if novos_dados.empty:
        progresso.empty()
        st.warning('Não há dados novos na planilha')
        return

    progresso.progress(3/4, 'Enviando Dados...')

    try:
        up.adicionar_registros(novos_dados, 'portal_de_vendas_megaferro')
        progresso.progress(4/4, 'Finalizado!')
        progresso.empty()
        st.success(f'Base de dados atualizada com sucesso! {len(novos_dados)} registros adicionados')
    except Exception as e:
        progresso.empty()
        st.warning(f'Houve um erro ao enviar dados. Erro: {e}')
        return

def processar_valores_carga(arquivo):
    st.markdown(f'### -> Valores de Carga')
    progresso = st.progress(0, 'Lendo arquivo...')

    try: 
        data_frame = pd.read_excel(arquivo, header=2, skipfooter=1)
    except Exception as e:
        progresso.empty()
        st.error(f'Erro ao abrir arquivo. Erro: {e}')
        return

    progresso.progress(1/4, 'Validando planilha...')

    try:
        up.validar_planilha(
            data_frame, 
            ['Ordem Mãe', 'Cód Veículo', 'Veículo', 'Rota', 'Situação da OC',
            'Motorista', 'TOTAL', 'DESPESAS', 'PERCC', 'RPA', 'TERCERIZADO',
            'COMBUSTIVEL', 'CHAPA', 'Despesa 501', 'PEDAGIO', 'DIARIA',
            'ALIMENTACAO', 'VALOR', 'Peso Máximo', 'PESO', 'Cód Região',
            'CAPACIDADE', 'VALE_FRETE', 'OUTRAS', 'TRANSFERENCIAS'],
        )
    except Exception as e:
        progresso.empty()
        st.error(f'Planilha inválida. Erro: {e}')
        return
    
    data_frame.columns = [slugify(column, separator='_') for column in data_frame.columns.to_list()]

    progresso.progress(2/4, 'Filtrando Registros...')

    try:
        novos_dados = up.filtrar_novos_dados(data_frame, "ordem_mae_megaferro", 'ordem_mae')
    except Exception as e:
        progresso.empty()
        st.error(f'Erro ao se conectar ao banco de dados. Erro: {e}')
        return

    if novos_dados.empty:
        progresso.empty()
        st.warning('Não há dados novos na planilha')
        return

    progresso.progress(3/4, 'Enviando Dados...')

    try:
        up.adicionar_registros(novos_dados, 'ordem_mae_megaferro')
        progresso.progress(4/4, 'Finalizado!')
        progresso.empty()
        st.success(f'Base de dados atualizada com sucesso! {len(novos_dados)} registros adicionados')
    except Exception as e:
        progresso.empty()
        st.warning(f'Houve um erro ao enviar dados. Erro: {e}')
        return

def page_upload():
    st.write("# Logística Megaferro")
    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.header("Enviar para o banco de dados", divider=True)

        formacao_carga = st.file_uploader("**Planilha Formação de Carga**", ['xlsx', 'xls'])
        portal_vendas = st.file_uploader('**Planilha Portal de Vendas**', ['xlsx', 'xls'])
        valores_carga = st.file_uploader('**Planilha Valores de Carga**', ['xlsx', 'xls'])

        botao = st.button('Enviar')

    with col2:
        st.header('Logs', divider=True)

        if (formacao_carga or portal_vendas or valores_carga) and botao:
            if formacao_carga:
                processar_formacao_carga(formacao_carga)
            
            if portal_vendas:
                processar_portal_vendas(portal_vendas)
            
            if valores_carga:
                processar_valores_carga(valores_carga)
                

def main():
    st.set_page_config(layout='wide', page_title="Logística Megaferro")
    page_upload()

if __name__ == "__main__":
    main()