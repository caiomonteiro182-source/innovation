import streamlit as st
import pandas as pd
import base64

# 1. Configuração da página (Ícone da guia alterado para icon_consultor.png)
st.set_page_config(
    page_title="Platform Science - Fluxo de Atendimento de Consultores",
    page_icon="icon_consultor.png",
    layout="wide"
)

# Função para converter a imagem local em Base64 e usar como background
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

img_base64 = get_base64_of_bin_file("estradas.jpeg")

# 2. Injeção de CSS com Marca d'Água da imagem estradas.jpeg e Fundo Dark Mode
st.markdown(f"""
    <style>
    /* Marca d'água no fundo da aplicação */
    .stApp {{
        background: linear-gradient(135deg, rgba(10, 20, 29, 0.92) 0%, rgba(15, 35, 56, 0.90) 50%, rgba(23, 56, 92, 0.92) 100%),
                    url("data:image/jpeg;base64,{img_base64}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
        color: #F0F4F8 !important;
    }}

    /* Título Principal */
    h1 {{
        color: #FFFFFF !important;
        font-weight: 800 !important;
        margin-bottom: 0px !important;
    }}

    /* Subtítulos e Seções */
    h2, h3, h4 {{
        color: #0099E5 !important;
        font-weight: 700 !important;
    }}

    /* Textos gerais */
    p, span, label {{
        color: #E2E8F0 !important;
    }}

    /* Estilização Geral das Métricas do Streamlit */
    [data-testid="stMetricValue"] {{
        color: #38BDF8 !important;
        font-weight: bold !important;
        white-space: normal !important;
        word-break: break-word !important;
        font-size: 1.5rem !important;
    }}
    
    [data-testid="stMetricLabel"] {{
        color: #94A3B8 !important;
        font-weight: 600 !important;
        white-space: normal !important;
    }}

    /* Cartões / Containers das Métricas com efeito glassmorphism */
    [data-testid="stMetric"] {{
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(6px);
        border: 1px solid rgba(0, 153, 229, 0.3);
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
        min-height: 100px;
    }}

    /* Estilização das Abas */
    button[data-baseweb="tab"] {{
        color: #94A3B8 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }}

    button[data-baseweb="tab"][aria-selected="true"] {{
        color: #38BDF8 !important;
        border-bottom-color: #0099E5 !important;
    }}

    /* Caixas de Alerta */
    .stAlert {{
        border-radius: 8px !important;
        background-color: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(4px);
    }}

    /* Selectbox estilizado */
    div[data-baseweb="select"] > div {{
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #FFFFFF !important;
        border-color: #0099E5 !important;
    }}

    /* Linha Divisória */
    hr {{
        border-color: #0099E5 !important;
        opacity: 0.4;
    }}

    /* Ajustes responsivos para celular */
    @media (max-width: 768px) {{
        .block-container {{
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
            padding-top: 1rem !important;
        }}

        [data-testid="stImage"] {{
            display: flex;
            justify-content: center;
            margin: 0 auto 15px auto;
        }}

        h1 {{
            font-size: 1.6rem !important;
            text-align: center;
        }}

        h2, h3 {{
            font-size: 1.2rem !important;
        }}

        [data-testid="stMetricValue"] {{
            font-size: 1.2rem !important;
            line-height: 1.4 !important;
        }}

        iframe {{
            width: 100% !important;
            height: 220px !important;
        }}

        button[data-baseweb="tab"] {{
            font-size: 13px !important;
            padding: 6px 8px !important;
        }}

        [data-testid="stDataFrame"] {{
            width: 100% !important;
            overflow-x: auto !important;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# Header com a Logo e Título
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    st.image("logo.png", width=200)

with col_titulo:
    st.title("Fluxo de Atendimento de Consultores")
    st.caption("Visão atual dos gargalos operacionais e proposta de reestruturação dos fluxos da equipe.")

st.divider()

# Dados das Causas / Problemas Atuais
dados_acionamentos = [
    {
        "problema_atual": "Falta de Equipamento",
        "canal_atual": "WhatsApp / E-mail",
        "acionado_atual": "Consultor",
        "destino_correto": "Planejamento / Suprimentos",
        "impacto": "Alto",
        "acao_recomendada": "Criar fluxo direto para o time de Planejamento de estoque."
    },
    {
        "problema_atual": "Problemas na Oficina",
        "canal_atual": "WhatsApp / Slack",
        "acionado_atual": "Consultor",
        "destino_correto": "Gestão de Oficinas",
        "impacto": "Alto",
        "acao_recomendada": "Painel de visibilidade de capacidade e fila de atendimento."
    },
    {
        "problema_atual": "Falta de Inventário na Oficina",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Back Office / Sistema de Estoque",
        "impacto": "Muito Alto",
        "acao_recomendada": "Obrigatoriedade de checklist diário antes do acionamento."
    },
    {
        "problema_atual": "Avarias, Danos e Riscos",
        "canal_atual": "E-mail / WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Setor de Qualidade / Vistoria",
        "impacto": "Médio",
        "acao_recomendada": "Formulário padronizado com upload obrigatório de foto."
    },
    {
        "problema_atual": "Acionamento Back Office Oficina",
        "canal_atual": "Slack / WhatsApp",
        "acionado_atual": "Consultor (Bypass)",
        "destino_correto": "Back Office da Oficina",
        "impacto": "Médio",
        "acao_recomendada": "Trava de sistema: só liberar consultor se Back Office não atender."
    },
    {
        "problema_atual": "Integração / Documentação",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Portal de Conhecimento / Self-Service",
        "impacto": "Baixo",
        "acao_recomendada": "Disponibilizar central de ajuda com download de documentos."
    },
    {
        "problema_atual": "Trava no Cliente (Sem frota no local)",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Consultor (Válido)",
        "impacto": "Alto",
        "acao_recomendada": "Ficha de impeditivo rápida para atuação comercial do consultor."
    },
    {
        "problema_atual": "Falta de Dados na OS",
        "canal_atual": "WhatsApp / E-mail",
        "acionado_atual": "Consultor",
        "destino_correto": "Emissor da OS / Validação Automática",
        "impacto": "Médio",
        "acao_recomendada": "Bloqueio de abertura de OS sem campos de endereço e frota."
    },
    {
        "problema_atual": "Encaixe de Agendamento",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Back Office Oficina",
        "impacto": "Médio",
        "acao_recomendada": "Fila única de solicitações de encaixe no Back Office."
    }
]

df = pd.DataFrame(dados_acionamentos)

# Renomeando as colunas para exibição amigável
df_exibicao = df.rename(columns={
    "problema_atual": "Problema Atual",
    "canal_atual": "Canal Atual",
    "acionado_atual": "Quem é Acionado Hoje",
    "destino_correto": "Destino Correto",
    "impacto": "Nível de Impacto"
})

# Link do Vídeo (Modo Preview)
video_url = "https://drive.google.com/file/d/1CMn5TEiWUZ-Jzul_Z4das8bYXHNJk1q6/preview"

# Navegação por Abas
aba1, aba2 = st.tabs(["📊 Visão Geral Atual", "🔄 Detalhamento - Como Resolver?"])

# ABA 1: VISÃO GERAL ATUAL
with aba1:
    col_texto, col_video = st.columns([1, 1])
    
    with col_texto:
        st.subheader("Métricas do Processo Atual")
        
        st.metric("Problemas Mapeados", len(df))
        st.metric("Acionamentos Indevidos ao Consultor", "7 de 9", delta="-77%", delta_color="inverse")
        st.metric("Canais Pulverizados", "3 (WhatsApp, E-mail, Slack)")
        
    with col_video:
        st.subheader("📺 Vídeo de Apresentação")
        st.components.v1.iframe(video_url, height=360)

    st.markdown("---")
    st.markdown("### Tabela Resumo dos Gargalos Operacionais")
    st.dataframe(
        df_exibicao[["Problema Atual", "Canal Atual", "Quem é Acionado Hoje", "Destino Correto", "Nível de Impacto"]],
        use_container_width=True,
        hide_index=True
    )

# ABA 2: DETALHAMENTO - COMO RESOLVER?
with aba2:
    st.subheader("Detalhamento Ponto a Ponto: Como Resolver")
    
    item_selecionado = st.selectbox(
        "Selecione o Problema Atual para Analisar a Solução:",
        options=df["problema_atual"].tolist()
    )
    
    detalhe = df[df["problema_atual"] == item_selecionado].iloc[0]
    
    st.markdown("---")
    
    col_esquerda, col_direita = st.columns(2)
    
    with col_esquerda:
        st.markdown("### ❌ Como é feito hoje")
        st.warning(f"**Problema Atual:** {detalhe['problema_atual']}")
        st.write(f"**Canal de Entrada:** {detalhe['canal_atual']}")
        st.write(f"**Quem é acionado:** {detalhe['acionado_atual']}")
        st.write(f"**Impacto Operacional:** {detalhe['impacto']}")
        
    with col_direita:
        st.markdown("### ✅ Fluxo Proposto (Solução)")
        st.success(f"**Destino Correto:** {detalhe['destino_correto']}")
        st.info(f"**O que deve ser feito:** {detalhe['acao_recomendada']}")
