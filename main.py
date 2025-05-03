import streamlit as st
import requests
import pandas as pd
from io import BytesIO
import openýxl
LOGO_URL_LARGE = "https://streamlit.io/images/brand/streamlit-mark-color.png" 
st.set_page_config(page_title="Consulta CNPJ", layout="wide")
st.title("Consulta de Dados via CNPJ")
with st.sidebar:
    st.logo(
    LOGO_URL_LARGE,
    link="https://adolfohugosilvaportifolio.streamlit.app",
    icon_image=LOGO_URL_LARGE,
)
    cnpj_input = st.text_input("Insira o CNPJ:", max_chars=18, placeholder="00.000.000/0000-00")
    consultar = st.button("Consultar")

    st.markdown("""
     🔗 [LinkedIn](https://www.linkedin.com/in/adolfo-hugo-silva-a298751aa)
                  
     📂 [GitHub](https://github.com/Adolfo-Hugo)
                
    🔗 [Portfólio](https://adolfohugosilvaportifolio.streamlit.app)
                
    📧 Email: adolfohugosilva@gmail.com
                  
     📞 WhatsApp: (82) 99683-8463                 

    """)

if consultar and cnpj_input:
    cnpj_numero = cnpj_input.replace('.', '').replace('-', '').replace('/', '')
    url = f'https://publica.cnpj.ws/cnpj/{cnpj_numero}'

    with st.spinner("Consultando dados..."):
        resposta = requests.get(url)

        if resposta.status_code != 200:
            st.error("Erro ao consultar o CNPJ. Verifique se está correto.")
        else:
            dados = resposta.json()

            dados_empresa = {
                'Razão Social': dados.get('razao_social'),
                'Nome Fantasia': dados.get('nome_fantasia'),
                'Natureza Jurídica': dados['natureza_juridica']['descricao'],
                'Porte': dados['porte']['descricao'],
                'Capital Social': dados['capital_social'],
                'Situação Cadastral': dados['estabelecimento']['situacao_cadastral'],
                'Simples Nacional': dados['simples']['simples'],
                'Exclusão do MEI': dados['simples']['data_exclusao_mei'],
                'Exclusão do Simples': dados['simples']['data_exclusao_simples'],
                'Atividade Principal': dados['estabelecimento']['atividade_principal']['descricao'],
                'CNAE Principal': dados['estabelecimento']['atividade_principal']['id'],
                'Cidade': dados['estabelecimento']['cidade']['nome'],
                'CEP': dados['estabelecimento']['cep'],
                'Email': dados['estabelecimento']['email'],
            }
            df_empresa = pd.DataFrame([dados_empresa])
            
            inscricoes = dados['estabelecimento']['inscricoes_estaduais']
            lista_inscricoes = []
            for insc in inscricoes:
                lista_inscricoes.append({
                    'Inscrição Estadual': insc['inscricao_estadual'],
                    'UF': insc['estado']['sigla'],
                    'Situação': 'Ativa' if insc['ativo'] else 'Inativa'
                })
            df_inscricoes_estaduais = pd.DataFrame(lista_inscricoes)

    
            atividades = dados['estabelecimento']['atividades_secundarias']
            cnaes = [a['id'] for a in atividades]
            descricoes = [a['descricao'] for a in atividades]
            df_atividades_secundarias = pd.DataFrame(
                list(zip(cnaes, descricoes)),
                columns=['CNAE Secundário', 'Descrição da Atividade']
            )

            lista_socios = []
            for socio in dados['socios']:
                lista_socios.append({
                    'Nome': socio['nome'],
                    'Qualificação': socio['qualificacao_socio']['descricao'],
                    'Faixa Etária': socio['faixa_etaria'],
                    'Data de Entrada': socio['data_entrada'],
                    'Tipo de Pessoa': socio['tipo']
                })
            df_socios = pd.DataFrame(lista_socios)
         
            st.subheader(" Dados da Empresa")
            st.dataframe(df_empresa)

            st.subheader(" Atividades Secundárias")
            st.dataframe(df_atividades_secundarias)

            st.subheader(" Inscrições Estaduais")
            st.dataframe(df_inscricoes_estaduais)

            st.subheader(" Sócios")
            st.dataframe(df_socios)

            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df_empresa.to_excel(writer, sheet_name='Empresa', index=False)
                df_atividades_secundarias.to_excel(writer, sheet_name='Atividades Secundárias', index=False)
                df_socios.to_excel(writer, sheet_name='Sócios', index=False)
                df_inscricoes_estaduais.to_excel(writer, sheet_name='Inscrições Estaduais', index=False)
            buffer.seek(0)

            st.download_button(
                label=" Baixar arquivo Excel",
                data=buffer,
                file_name=f"dados_cnpj_{cnpj_numero}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
st.markdown("---")
st.markdown("<p style='text-align: right; font-size: 14px;'>© 2025 Adolfo Hugo Silva </p>", unsafe_allow_html=True)


