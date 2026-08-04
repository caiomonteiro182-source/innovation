import streamlit as st
import pandas as pd
import base64
import plotly.graph_objects as go

# 1. Configuração da página
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

# 2. Injeção de CSS com Marca d'Água, Dark Mode, Glassmorphism e Tabela Customizada
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

    /* Container do Gráfico em Glassmorphism */
    .chart-card {{
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(6px);
        border: 1px solid rgba(0, 153, 229, 0.3);
        padding: 12px;
        border-radius: 10px;
        margin-top: 10px;
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

    /* ESTILO DA TABELA PERSONALIZADA (GLASSMORPHISM + BADGES) */
    .table-container {{
        width: 100%;
        overflow-x: auto;
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(8px);
        border-radius: 12px;
        border: 1px solid rgba(0, 153, 229, 0.3);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-top: 10px;
        margin-bottom: 20px;
    }}

    .custom-table {{
        width: 100%;
        border-collapse: collapse;
        text-align: left;
        font-size: 0.95rem;
    }}

    .custom-table th {{
        background-color: rgba(30, 41, 59, 0.85);
        color: #38BDF8;
        padding: 14px 16px;
        font-weight: 700;
        border-bottom: 2px solid rgba(0, 153, 229, 0.4);
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }}

    .custom-table td {{
        padding: 14px 16px;
        color: #E2E8F0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .custom-table tbody tr:hover {{
        background-color: rgba(0, 153, 229, 0.12);
        transition: background-color 0.2s ease;
    }}

    /* BADGES DE IMPACTO */
    .badge {{
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.8rem;
        display: inline-block;
        text-align: center;
        letter-spacing: 0.3px;
    }}

    .badge-muito-alto {{
        background-color: rgba(239, 68, 68, 0.2);
        color: #EF4444;
        border: 1px solid rgba(239, 68, 68, 0.5);
    }}

    .badge-alto {{
        background-color: rgba(245, 158, 11, 0.2);
        color: #F59E0B;
        border: 1px solid rgba(245, 158, 11, 0.5);
    }}

    .badge-medio {{
        background-color: rgba(16, 185, 129, 0.2);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.5);
    }}

    .badge-baixo {{
        background-color: rgba(100, 116, 139, 0.2);
        color: #94A3B8;
        border: 1px solid rgba(100, 116, 139, 0.5);
    }}

    /* AJUSTES RESPONSIVOS PARA DISPOSITIVOS MÓVEIS (CELULAR) */
    @media (max-width: 768px) {{
        .block-container {{
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
            padding-top: 1rem !important;
        }}

        /* Redimensiona as logos no celular */
        [data-testid="stImage"] img {{
            max-width: 120px !important;
            height: auto !important;
            margin: 0 auto !important;
            display: block !important;
        }}

        [data-testid="stImage"] {{
            display: flex;
            justify-content: center;
            margin: 0 auto 10px auto;
        }}

        h1 {{
            font-size: 1.4rem !important;
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
    }}
    </style>
""", unsafe_allow_html=True)

# Header de 3 Colunas (Logo Esquerda | Título Central | Logo Innovation Direita)
col_logo, col_titulo, col_innovation = st.columns([1.5, 4, 1.5], vertical_alignment="center")

with col_logo:
    st.image("logo.png", width=220)

with col_titulo:
    st.title("Fluxo de Atendimento de Consultores")
    st.caption("Visão atual dos gargalos operacionais e proposta de reestruturação dos fluxos da equipe.")

with col_innovation:
    st.image("logo_innovation2026.png", width=180)

st.divider()

# Dados Atualizados - 10 Situações Mapeadas
dados_acionamentos = [
    {
        "id": 1,
        "problema_atual": "Falta de Equipamento",
        "detalhamento": "Falta de equipamentos e itens especificados na OS (Equipamento de Manutenção e Pedido Comercial).",
        "canal_atual": "WhatsApp / E-mail",
        "acionado_atual": "Consultor",
        "destino_correto": "Planejamento / Suprimentos",
        "impacto": "Alto",
        "acao_recomendada": "Criar fluxo direto para o time de Planejamento e validação de estoque antes do envio da OS."
    },
    {
        "id": 2,
        "problema_atual": "Problema na Oficina",
        "detalhamento": "Problemas de oficina com cliente (atendimento, falta de equipamento, improdutividade, reclamação, alta demanda e remanejamento).",
        "canal_atual": "WhatsApp / Slack",
        "acionado_atual": "Consultor",
        "destino_correto": "Gestão de Oficinas",
        "impacto": "Alto",
        "acao_recomendada": "Painel de visibilidade em tempo real sobre capacidade, demanda e fila de atendimento."
    },
    {
        "id": 3,
        "problema_atual": "Falta de Inventário na Oficina",
        "detalhamento": "A ausência de inventário correto na oficina impede a verificação de estoque, gerando acionamentos indevidos ao consultor.",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Back Office / Sistema de Estoque",
        "impacto": "Muito Alto",
        "acao_recomendada": "Obrigatoriedade de verificação e rotina de inventário prévio no sistema antes do acionamento."
    },
    {
        "id": 4,
        "problema_atual": "Avarias, Danos e Riscos",
        "detalhamento": "Necessidade de vistoria no equipamento, avarias, danos detectados ou questões de qualidade do serviço prestado.",
        "canal_atual": "E-mail / WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Setor de Qualidade / Vistoria",
        "impacto": "Médio",
        "acao_recomendada": "Formulário padronizado com upload obrigatório de fotos e laudo preliminar de vistoria."
    },
    {
        "id": 5,
        "problema_atual": "Acionamento Back Office Oficina",
        "detalhamento": "Acionamento direto ao Back Office da oficina em primeiro nível; acionar o consultor apenas em caso de não atendimento.",
        "canal_atual": "Slack / WhatsApp",
        "acionado_atual": "Consultor (Bypass)",
        "destino_correto": "Back Office da Oficina",
        "impacto": "Médio",
        "acao_recomendada": "Redirecionamento automático e trava no sistema: acionar consultor apenas como Nível 2 de transbordo."
    },
    {
        "id": 6,
        "problema_atual": "Integração e Documentação",
        "detalhamento": "Falta de documentação da oficina com pedidos de apoio ao consultor para esclarecer dúvidas documentais.",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Portal de Conhecimento / Self-Service",
        "impacto": "Baixo",
        "acao_recomendada": "Central de ajuda online com download de documentação técnica, manuais e checklists em formato self-service."
    },
    {
        "id": 7,
        "problema_atual": "Trava no Cliente (Acionamento Oficina)",
        "detalhamento": "Oficina pede apoio ao consultor por travamentos no cliente (ex: falta de equipamento ou frota ausente no local).",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Consultor (Válido)",
        "impacto": "Alto",
        "acao_recomendada": "Ficha de impeditivo rápida de campo para atuação pontual e comercial do consultor."
    },
    {
        "id": 8,
        "problema_atual": "Falta de Dados na OS",
        "detalhamento": "Ausência de endereço do cliente ou localização exata da frota no momento do serviço.",
        "canal_atual": "WhatsApp / E-mail",
        "acionado_atual": "Consultor",
        "destino_correto": "Emissor da OS / Validação Automática",
        "impacto": "Médio",
        "acao_recomendada": "Trava no sistema bloqueando a abertura ou envio de OS sem o preenchimento de dados de localização."
    },
    {
        "id": 9,
        "problema_atual": "Encaixe de Agendamento",
        "detalhamento": "Acionamento do consultor solicitando encaixe na agenda, procedimento que cabe diretamente ao Back Office da Oficina.",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Back Office Oficina",
        "impacto": "Médio",
        "acao_recomendada": "Fila única e centralizada de agendamentos e encaixes gerenciada exclusivamente pelo Back Office."
    },
    {
        "id": 10,
        "problema_atual": "Suporte a Tecnologia",
        "detalhamento": "Módulo sem atualização de firmware, falhas no aplicativo móvel ou erro de integração de OS.",
        "canal_atual": "WhatsApp / Chamado",
        "acionado_atual": "Consultor",
        "destino_correto": "Suporte Técnico / TI",
        "impacto": "Alto",
        "acao_recomendada": "Abertura direta de ticket na central de TI com diagnósticos e logs automatizados."
    }
]

df = pd.DataFrame(dados_acionamentos)

# Cálculos dinâmicos
total_situacoes = len(df)
desvios_funcao = len(df[df["destino_correto"] != "Consultor (Válido)"])
pct_desvio = round((desvios_funcao / total_situacoes) * 100, 1)

# Função para formatar o badge HTML do impacto
def get_impact_badge(impacto):
    if impacto == "Muito Alto":
        return '<span class="badge badge-muito-alto">Muito Alto</span>'
    elif impacto == "Alto":
        return '<span class="badge badge-alto">Alto</span>'
    elif impacto == "Médio":
        return '<span class="badge badge-medio">Médio</span>'
    else:
        return '<span class="badge badge-baixo">Baixo</span>'

# Link do Vídeo (Modo Preview)
video_url = "https://drive.google.com/file/d/1hvDAr2C4TuyFXhvmDDwADHv1nZZoijsb/preview"

# Navegação por Abas
aba1, aba2 = st.tabs(["📊 Visão Geral Atual", "🔄 Detalhamento - Como Resolver?"])

# ABA 1: VISÃO GERAL ATUAL
with aba1:
    col_texto, col_video = st.columns([1, 1])
    
    with col_texto:
        st.subheader("Métricas do Processo Atual")
        
        # 1. GRÁFICO DE PIZZA / ROSCA (NÍVEIS DE IMPACTO)
        contagem_impacto = df['impacto'].value_counts()
        
        cores_mapa = {
            'Muito Alto': '#EF4444',
            'Alto': '#F59E0B',
            'Médio': '#10B981',
            'Baixo': '#94A3B8'
        }
        
        labels = contagem_impacto.index.tolist()
        values = contagem_impacto.values.tolist()
        colors = [cores_mapa.get(l, '#0099E5') for l in labels]

        fig_pizza = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.55,
            marker=dict(colors=colors, line=dict(color='#0A141D', width=2)),
            hoverinfo="label+value+percent",
            textinfo="value",
            textfont=dict(color='#FFFFFF', size=14, family="sans-serif")
        )])

        fig_pizza.update_layout(
            title=dict(
                text="Distribuição por Nível de Impacto",
                font=dict(color="#94A3B8", size=14, family="sans-serif")
            ),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.25,
                xanchor="center",
                x=0.5,
                font=dict(color="#E2E8F0", size=12)
            ),
            margin=dict(t=35, b=25, l=10, r=10),
            height=250,
            paper_bgcolor='rgba(15, 23, 42, 0.65)',
            plot_bgcolor='rgba(0,0,0,0)',
            annotations=[dict(
                text=f'<b>{total_situacoes}</b><br><span style="font-size:10px;color:#94A3B8">Total</span>',
                x=0.5, y=0.5, font_size=18, font_color="#FFFFFF", showarrow=False
            )]
        )

        st.plotly_chart(fig_pizza, use_container_width=True, config={'displayModeBar': False})
        
        # 2. BARRA DE PROGRESSO DO GARGALO OPERACIONAL
        st.html(f"""
            <div style="background: rgba(15, 23, 42, 0.65); backdrop-filter: blur(6px); border: 1px solid rgba(0, 153, 229, 0.3); padding: 16px; border-radius: 10px; margin-top: 10px;">
                <div style="color: #94A3B8; font-size: 0.9rem; font-weight: 600; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                    <span>Gargalo da Equipe de Consultores</span>
                    <span style="color: #EF4444; font-weight: bold; background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(239, 68, 68, 0.4);">
                        {pct_desvio}% Desvio de Função
                    </span>
                </div>
                <div style="width: 100%; background-color: rgba(255,255,255,0.08); border-radius: 6px; height: 12px; overflow: hidden; padding: 2px;">
                    <div style="width: {pct_desvio}%; background: linear-gradient(90deg, #F59E0B 0%, #EF4444 100%); height: 100%; border-radius: 4px; box-shadow: 0 0 10px rgba(239, 68, 68, 0.5);"></div>
                </div>
                <div style="color: #64748B; font-size: 0.78rem; margin-top: 8px;">
                    *Indica que {desvios_funcao} de {total_situacoes} acionamentos direcionados ao consultor deveriam ser tratados por outros canais/áreas.
                </div>
            </div>
        """)
        
    with col_video:
        st.subheader("📺 Vídeo de Apresentação")
        st.components.v1.iframe(video_url, height=360)

    st.markdown("---")
    st.markdown("### Resumo das Situações Atuais")

    # CONSTRUÇÃO DO HTML DA TABELA CUSTOMIZADA
    rows_html = ""
    for _, row in df.iterrows():
        badge = get_impact_badge(row["impacto"])
        rows_html += f"<tr><td><strong>{row['id']}. {row['problema_atual']}</strong></td><td>{row['canal_atual']}</td><td>{row['acionado_atual']}</td><td>{row['destino_correto']}</td><td>{badge}</td></tr>"

    table_html = f"""<div class="table-container"><table class="custom-table"><thead><tr><th>Problema Atual</th><th>Canal Atual</th><th>Quem é Acionado Hoje</th><th>Destino Correto</th><th>Nível de Impacto</th></tr></thead><tbody>{rows_html}</tbody></table></div>"""
    
    st.html(table_html)

# ABA 2: DETALHAMENTO - COMO RESOLVER?
with aba2:
    st.subheader("Detalhamento Ponto a Ponto: Como Resolver")
    
    opcoes_select = [f"{row['id']}. {row['problema_atual']}" for _, row in df.iterrows()]
    
    item_selecionado_str = st.selectbox(
        "Selecione o Problema Atual para Analisar a Solução:",
        options=opcoes_select
    )
    
    selected_id = int(item_selecionado_str.split(".")[0])
    detalhe = df[df["id"] == selected_id].iloc[0]
    
    st.markdown("---")
    
    col_esquerda, col_direita = st.columns(2)
    
    with col_esquerda:
        st.markdown("### ❌ Como é feito hoje")
        st.warning(f"**Problema Atual:** {detalhe['problema_atual']}")
        st.write(f"**Descrição do Cenário:** {detalhe['detalhamento']}")
        st.write(f"**Canal de Entrada:** {detalhe['canal_atual']}")
        st.write(f"**Quem é acionado:** {detalhe['acionado_atual']}")
        st.write(f"**Impacto Operacional:** {detalhe['impacto']}")
        
    with col_direita:
        st.markdown("### ✅ Fluxo Proposto (Solução)")
        st.success(f"**Destino Correto:** {detalhe['destino_correto']}")
        st.info(f"**Ação Recomendada:** {detalhe['acao_recomendada']}")

    # SEÇÃO DESTINADA AO DESTRINCHAMENTO APROFUNDADO DOS TÓPICOS
    if selected_id == 1:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 1: Falta de Equipamento")
        
        col_1_1, col_1_2 = st.columns(2)
        
        with col_1_1:
            st.markdown("### 1.1 Equipamento de Manutenção")
            st.info("""
            **Ação Necessária:**
            * Implementação de rotina de **inventário mensal atualizado** diretamente na oficina.
            * Sincronização contínua com o sistema para impedir a emissão de ordens de serviço sem saldo físico em estoque.
            """)
            
        with col_1_2:
            st.markdown("### 1.2 Equipamento de Pedido Comercial")
            
            st.error("""
            **Como é feito hoje?**
            * **Caso 1:** Cliente pede 5 kits e chegam faltando 5 câmeras laterais. O técnico aciona o consultor perguntando se pode fazer instalação parcial. Se não for ADAS ou DSM, o processo é liberado.
            * **Caso 2:** Durante a instalação, se faltar um item que o técnico possui em seu estoque próprio, ele realiza a reposição por conta própria e depois avisa o consultor.
            """)
            
            st.warning("""
            **Impactos Financeiros e Operacionais:**
            * **Improdutivo:** Se o técnico não realizar a instalação parcial, o agendamento é perdido, gerando reagendamento e **custo duplicado** de deslocamento para a empresa.
            * **Instalação Parcial:** Gera **cobrança duplicada**, pois o técnico precisa retornar futuramente até o cliente apenas para instalar o item remanescente.
            """)
