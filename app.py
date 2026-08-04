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

# Converte as duas logos para Base64
logo_ps_b64 = get_base64_of_bin_file("logo.png")
logo_inno_b64 = get_base64_of_bin_file("logo_innovation2026.png")

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

    /* Ajuste de margem superior */
    .block-container {{
        padding-top: 3.5rem !important;
    }}

    /* Layout Desktop do Cabeçalho */
    .header-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        width: 100%;
        padding: 5px 0;
    }}

    .header-logo-left {{
        height: 65px;
        object-fit: contain;
    }}

    .header-logo-right {{
        height: 55px;
        object-fit: contain;
    }}

    .header-center-title {{
        text-align: center;
        flex-grow: 1;
    }}

    .header-center-title h1 {{
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 2.3rem !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.2;
    }}

    .header-center-title p {{
        color: #CBD5E1 !important;
        margin: 8px 0 0 0 !important;
        font-size: 1.15rem !important;
        font-weight: 500 !important;
    }}

    /* Subtítulos e Seções */
    h2, h3, h4 {{
        color: #0099E5 !important;
        font-weight: 700 !important;
    }}

    p, span, label {{
        color: #E2E8F0 !important;
    }}

    /* CARTÃO DO GRÁFICO E VÍDEO COM EFEITO HOVER GLASSMORPHISM */
    .video-card-container, .chart-card-container {{
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 12px 32px 0 rgba(0, 0, 0, 0.45);
        transition: all 0.3s ease-in-out;
        margin-bottom: 12px;
    }}

    .video-card-container:hover, .chart-card-container:hover {{
        border-color: rgba(56, 189, 248, 0.8) !important;
        box-shadow: 0 0 25px rgba(0, 153, 229, 0.4) !important;
        transform: translateY(-2px);
    }}

    .video-card-header, .chart-card-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
    }}

    .video-card-title, .chart-card-title {{
        color: #FFFFFF;
        font-size: 1.1rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .video-badge, .chart-badge {{
        background: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        border: 1px solid rgba(56, 189, 248, 0.4);
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
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

    /* TABELA PERSONALIZADA */
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

    /* RESPONSIVIDADE MOBILE */
    @media (max-width: 768px) {{
        .block-container {{
            padding-top: 3.8rem !important;
            padding-left: 0.6rem !important;
            padding-right: 0.6rem !important;
        }}

        .header-container {{
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
        }}

        .header-logos-mobile {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin-bottom: 6px;
        }}

        .header-logo-left {{
            height: 32px !important;
        }}

        .header-logo-right {{
            height: 32px !important;
        }}

        .header-center-title {{
            width: 100%;
        }}

        .header-center-title h1 {{
            font-size: 1.5rem !important;
            line-height: 1.25 !important;
        }}

        .header-center-title p {{
            font-size: 0.9rem !important;
            line-height: 1.3 !important;
            margin-top: 6px !important;
        }}

        div[data-testid="stCustomComponentV1"] iframe {{
            height: 220px !important;
        }}

        button[data-baseweb="tab"] {{
            font-size: 12px !important;
            padding: 4px 6px !important;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO HTML NATIVO
src_logo_ps = f"data:image/png;base64,{logo_ps_b64}" if logo_ps_b64 else "logo.png"
src_logo_inno = f"data:image/png;base64,{logo_inno_b64}" if logo_inno_b64 else "logo_innovation2026.png"

st.html(f"""
    <div class="header-container">
        <div class="header-logos-mobile">
            <img src="{src_logo_ps}" class="header-logo-left" alt="Platform Science">
            <img src="{src_logo_inno}" class="header-logo-right" alt="Innovation Day 2026">
        </div>
        <div class="header-center-title">
            <h1>Fluxo de Atendimento de Consultores</h1>
            <p>Visão atual dos gargalos operacionais e proposta de reestruturação dos fluxos da equipe.</p>
        </div>
    </div>
""")

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
        "detalhamento": "Problemas de oficina com cliente (atendimento, no-show, reclamação do cliente e alta demanda de oficina).",
        "canal_atual": "WhatsApp / E-mail / Slack",
        "acionado_atual": "Consultor",
        "destino_correto": "Consultor (Somente Casos Graves)",
        "impacto": "Alto",
        "acao_recomendada": "Manter o acionamento ao consultor restrito a casos graves de alta complexidade ou risco ao relacionamento."
    },
    {
        "id": 3,
        "problema_atual": "Falta de Inventário na Oficina",
        "detalhamento": "A ausência de inventário correto na oficina impede a verificação de estoque, gerando cobranças indevidas ao consultor.",
        "canal_atual": "WhatsApp / Logística",
        "acionado_atual": "Consultor",
        "destino_correto": "Plataforma Web / Sistema de Estoque",
        "impacto": "Muito Alto",
        "acao_recomendada": "Gerenciamento automatizado de estoque via plataforma web, realizando baixa automática com a execução no sistema."
    },
    {
        "id": 4,
        "problema_atual": "Avarias, Danos e Riscos",
        "detalhamento": "Necessidade de vistoria no equipamento, avarias ou danos detectados que impactam a qualidade do serviço.",
        "canal_atual": "WhatsApp / E-mail / Slack",
        "acionado_atual": "Consultor",
        "destino_correto": "Análise Técnica N1/N2 (Transbordo)",
        "impacto": "Médio",
        "acao_recomendada": "Análise técnica prévia pela equipe de N1/N2. Intervenção do consultor somente se N1/N2 não identificarem o problema."
    },
    {
        "id": 5,
        "problema_atual": "Acionamento Back Office Oficina",
        "detalhamento": "Solicitações direcionadas ao consultor que deveriam ir direto ao Back Office da oficina ou agendamento GR.",
        "canal_atual": "WhatsApp / E-mail / Slack",
        "acionado_atual": "Consultor (Bypass)",
        "destino_correto": "Back Office Oficina / Agendamento GR",
        "impacto": "Médio",
        "acao_recomendada": "Acesso direto às oficinas e agendamento GR. Acionar o consultor apenas caso não obtenha retorno."
    },
    {
        "id": 6,
        "problema_atual": "Integração e Documentação",
        "detalhamento": "Falta ou demora na entrega da documentação da oficina com acionamento indevido ao consultor.",
        "canal_atual": "WhatsApp / Chamado",
        "acionado_atual": "Consultor",
        "destino_correto": "Setor de Inteligência (Robson)",
        "impacto": "Baixo",
        "acao_recomendada": "Redirecionar tratativas sobre documentos da oficina diretamente para o Setor de Inteligência."
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
desvios_funcao = len(df[~df["destino_correto"].str.contains("Consultor")])
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
    col_texto, col_video = st.columns([1, 1], vertical_alignment="top")
    
    with col_texto:
        # 1. CONTAINER GLASSMOPHISM DO GRÁFICO
        st.html("""
            <div class="chart-card-container">
                <div class="chart-card-header">
                    <div class="chart-card-title">
                        <span>📊 Distribuição por Nível de Impacto</span>
                    </div>
                    <span class="chart-badge">Métrica Global</span>
                </div>
            </div>
        """)
        
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
            marker=dict(
                colors=colors, 
                line=dict(color='#0A141D', width=2)
            ),
            hovertemplate="<b>Impacto %{label}</b><br>Ocorrências: <b>%{value}</b><br>Proporção: <b>%{percent}</b><extra></extra>",
            textinfo="value",
            textfont=dict(color='#FFFFFF', size=14, family="sans-serif")
        )])

        fig_pizza.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.25,
                xanchor="center",
                x=0.5,
                font=dict(color="#E2E8F0", size=12)
            ),
            hoverlabel=dict(
                bgcolor="rgba(15, 23, 42, 0.95)",
                bordercolor="#38BDF8",
                font_size=13,
                font_family="sans-serif",
                font_color="#FFFFFF"
            ),
            margin=dict(t=10, b=25, l=10, r=10),
            height=230,
            paper_bgcolor='rgba(0,0,0,0)',
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
        # CABEÇALHO DO CARD GLASSMORPHISM DO VÍDEO
        st.html("""
            <div class="video-card-container">
                <div class="video-card-header">
                    <div class="video-card-title">
                        <span>📺 Vídeo de Apresentação</span>
                    </div>
                    <span class="video-badge">Apresentação Executiva</span>
                </div>
            </div>
        """)
        # CARREGAMENTO SEGURO DO IFRAME STREAMLIT
        st.components.v1.iframe(video_url, height=330)

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

    # DESTRINCHAMENTO - CAUSA 1
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

    # DESTRINCHAMENTO - CAUSA 2
    elif selected_id == 2:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 2: Problema na Oficina")
        
        col_2_1, col_2_2 = st.columns(2)
        
        with col_2_1:
            st.markdown("### ⚠️ Como é feito hoje?")
            st.error("""
            * **Acontecimentos:** Ocorre em casos de problemas de atendimento, *no-show* (ausência), reclamação direta do cliente ou alta demanda da oficina.
            * **Canal de Comunicação:** Quem recebe a reclamação aciona diretamente o consultor via **WhatsApp, E-mail ou Slack**.
            """)
            
        with col_2_2:
            st.markdown("### 🎯 Impactos e Solução Proposta")
            st.warning("""
            **Impacto Atual:**
            * Gera **altas demandas e sobrecarga** constante para a equipe de consultores.
            """)
            st.success("""
            **Solução:**
            * O processo continuará da mesma maneira, **mantendo o acionamento ao consultor restrito para casos graves** de alta relevância ou risco comercial.
            """)

    # DESTRINCHAMENTO - CAUSA 3
    elif selected_id == 3:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 3: Cobrança pela Falta de Inventário")
        
        col_3_1, col_3_2 = st.columns(2)
        
        with col_3_1:
            st.markdown("### 📦 Como é feito hoje & Impactos")
            st.error("""
            **Como é feito hoje?**
            * Como as oficinas não realizam o inventário corretamente, não verificam previamente os itens no estoque.
            * A **Logística aciona os consultores** cobrando posicionamento sobre a falta de inventário dessas oficinas.
            """)
            st.warning("""
            **Impactos:**
            * Falta generalizada de inventário e de peças disponíveis na oficina.
            * **Incapacidade de execução de serviços** agendados por ausência de componentes no local.
            """)
            
        with col_3_2:
            st.markdown("### ⚙️ Solução Proposta")
            st.success("""
            **Gerenciamento Automatizado:**
            * O próprio **sistema assume o gerenciamento do estoque** através de uma plataforma web dedicada.
            * **Contagem e baixa automatizadas:** O saldo do estoque é atualizado instantaneamente conforme os equipamentos são baixados via sistema após cada serviço.
            """)

    # DESTRINCHAMENTO - CAUSA 4
    elif selected_id == 4:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 4: Avarias, Danos e Riscos")
        
        col_4_1, col_4_2 = st.columns(2)
        
        with col_4_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * O cliente necessita de vistoria no equipamento ou reporta qualquer dano referente à qualidade do serviço prestado.
            * Quem recebe a solicitação aciona **diretamente o consultor** via WhatsApp, E-mail ou Slack.
            """)
            st.warning("""
            **Impacto:**
            * Gera **altas demandas e interrupções** desnecessárias para o consultor.
            """)
            
        with col_4_2:
            st.markdown("### ⚙️ Solução Proposta (Filtro N1/N2)")
            st.success("""
            **Análise Técnica Especializada:**
            * Realização de análise com **conhecimento técnico prévio sobre a causa raiz** do problema diretamente pelas equipes de **N1 / N2**.
            * **Regra de Transbordo:** A intervenção do consultor será solicitada **exclusivamente caso o N1 ou N2 não consigam identificar ou resolver o problema**.
            """)

    # DESTRINCHAMENTO - CAUSA 5
    elif selected_id == 5:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 5: Acionamento Back Office Oficina")
        
        col_5_1, col_5_2 = st.columns(2)
        
        with col_5_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * Quem recebe solicitações destinadas à oficina aciona **diretamente o consultor** por WhatsApp, E-mail ou Slack (fazendo *bypass* do Back Office).
            """)
            st.warning("""
            **Impacto:**
            * **Altas demandas acumuladas** no consultor por tratativas operacionais que deveriam ser resolvidas na ponta.
            """)
            
        with col_5_2:
            st.markdown("### ⚙️ Solução Proposta (Acesso Direto / GR)")
            st.success("""
            **Fluxo Direto de Atendimento:**
            * Garantir **acesso direto às oficinas** ou direcionar solicitações pelo fluxo de **agendamento GR**.
            * **Regra de Escalonamento:** O consultor só deve ser acionado **caso não haja retorno ou resolução** após a tentativa direta com a oficina/agendamento.
            """)

    # DESTRINCHAMENTO - CAUSA 6
    elif selected_id == 6:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 6: Integração e Documentação")
        
        col_6_1, col_6_2 = st.columns(2)
        
        with col_6_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * O consultor é acionado diretamente quando a oficina demora para entregar os documentos requeridos.
            """)
            st.warning("""
            **Impacto:**
            * Gera **altas demandas operacionais e desvio de foco** do consultor com cobranças de rotina.
            """)
            
        with col_6_2:
            st.markdown("### ⚙️ Solução Proposta (Setor de Inteligência)")
            st.success("""
            **Redirecionamento para o Setor de Inteligência:**
            * Acionar o **Setor de Inteligência (Robson)** para conduzir todas as tratativas e cobranças de documentos diretamente com a oficina.
            * Desonerar o consultor desse acompanhamento burocrático diário.
            """)
