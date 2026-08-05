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

# Função para converter imagens locais em Base64
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

img_base64 = get_base64_of_bin_file("estradas.jpeg")

# Converte as logos e foto da equipe para Base64
logo_ps_b64 = get_base64_of_bin_file("logo.png")
logo_inno_b64 = get_base64_of_bin_file("logo_innovation2026.png")
foto_equipe_b64 = get_base64_of_bin_file("equipe_fluxo.jpg")

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

    /* Layout do Cabeçalho */
    .header-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        width: 100%;
        padding: 5px 0;
    }}

    /* Container Flex que força as logos a ficarem LADO A LADO */
    .header-logos-wrapper {{
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    .header-logo-left {{
        height: 60px;
        object-fit: contain;
    }}

    .header-logo-right {{
        height: 50px;
        object-fit: contain;
    }}

    /* Linha divisória vertical perfeita entre as logos */
    .header-logo-divider {{
        width: 1px !important;
        height: 45px !important;
        background: rgba(56, 189, 248, 0.5) !important;
        margin: 0 15px !important;
        display: block !important;
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

    /* CONTAINER FULL GLASSMORPHISM DE CARDS */
    .glass-card-full {{
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 16px;
        padding: 18px 20px 8px 20px;
        box-shadow: 0 12px 32px 0 rgba(0, 0, 0, 0.45);
        transition: all 0.3s ease-in-out;
        margin-bottom: 12px;
    }}

    .glass-card-full:hover {{
        border-color: rgba(56, 189, 248, 0.8) !important;
        box-shadow: 0 0 25px rgba(0, 153, 229, 0.4) !important;
        transform: translateY(-2px);
    }}

    .glass-card-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
    }}

    .glass-card-title {{
        color: #FFFFFF;
        font-size: 1.15rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    /* CARD EXCLUSIVO DA EQUIPE COM DESTAQUE EM FOTO */
    .team-card {{
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 16px;
        padding: 20px 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 25px;
        margin-bottom: 25px;
        transition: all 0.3s ease-in-out;
    }}

    .team-card:hover {{
        border-color: rgba(56, 189, 248, 0.85);
        box-shadow: 0 0 30px rgba(0, 153, 229, 0.35);
    }}

    .team-card-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid rgba(56, 189, 248, 0.25);
        padding-bottom: 12px;
        margin-bottom: 16px;
    }}

    .team-card-title {{
        color: #38BDF8;
        font-size: 1.25rem;
        font-weight: 800;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .team-leader-badge {{
        background: rgba(0, 153, 229, 0.2);
        color: #38BDF8;
        border: 1px solid rgba(0, 153, 229, 0.5);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
    }}

    /* ÁREA DA FOTO DA EQUIPE AJUSTADA PARA PROPORÇÃO 960x732 */
    .team-photo-container {{
        width: 100%;
        aspect-ratio: 960 / 732;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(56, 189, 248, 0.3);
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        background: rgba(15, 23, 42, 0.9);
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .team-photo {{
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 12px;
    }}

    /* CONTAINER E BADGES DOS NOMES DOS INTEGRANTES */
    .team-members-tags-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        margin-top: 16px;
        padding: 4px;
    }}

    .member-tag {{
        background: rgba(30, 41, 59, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.3);
        color: #F8FAFC;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.88rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 6px;
        backdrop-filter: blur(4px);
    }}

    .member-tag span {{
        color: #38BDF8;
        font-weight: 700;
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
            flex-direction: column !important;
            justify-content: center !important;
            align-items: center !important;
        }}

        .header-logos-wrapper {{
            margin-bottom: 10px !important;
        }}

        .header-logo-left {{
            height: 35px !important;
        }}

        .header-logo-right {{
            height: 30px !important;
        }}

        .header-logo-divider {{
            height: 28px !important;
            margin: 0 10px !important;
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

        button[data-baseweb="tab"] {{
            font-size: 12px !important;
            padding: 4px 6px !important;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO HTML NATIVO COM LOGOS LADO A LADO
src_logo_ps = f"data:image/png;base64,{logo_ps_b64}" if logo_ps_b64 else "logo.png"
src_logo_inno = f"data:image/png;base64,{logo_inno_b64}" if logo_inno_b64 else "logo_innovation2026.png"

st.html(f"""
    <div class="header-container">
        <div class="header-logos-wrapper">
            <img src="{src_logo_ps}" class="header-logo-left" alt="Platform Science">
            <div class="header-logo-divider"></div>
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
        "detalhamento": "A oficina pede apoio ao consultor por travamentos no cliente (ex: falta de equipamento, problema no aplicativo).",
        "canal_atual": "WhatsApp / Campo",
        "acionado_atual": "Consultor",
        "destino_correto": "Ponto Focal / Filtro de Demandas",
        "impacto": "Alto",
        "acao_recomendada": "Designar uma pessoa para filtrar as demandas de campo e compreender a situação antes de escalar ao consultor."
    },
    {
        "id": 8,
        "problema_atual": "Falta de Dados na OS",
        "detalhamento": "Falta de endereço na OS (endereço do cliente ou localização de onde a frota se encontra na hora do serviço).",
        "canal_atual": "WhatsApp / Chamado",
        "acionado_atual": "Consultor",
        "destino_correto": "Agendamento GR",
        "impacto": "Alto",
        "acao_recomendada": "Acionar o time de agendamento GR para validação e inclusão de dados de localização da frota."
    },
    {
        "id": 9,
        "problema_atual": "Encaixe de Agendamento",
        "detalhamento": "Acionamento do consultor para encaixe de agendamento, quando o contato poderia ser direto com o Back Office da oficina.",
        "canal_atual": "WhatsApp / E-mail / Slack",
        "acionado_atual": "Consultor",
        "destino_correto": "Oficinas / Agendamento GR",
        "impacto": "Alto",
        "acao_recomendada": "Acesso direto às oficinas ou agendamento GR. Acionar o consultor apenas caso não obtenha retorno."
    },
    {
        "id": 10,
        "problema_atual": "Acionamento sobre Tecnologia",
        "detalhamento": "Módulo sem atualização de firmware, falha no aplicativo móvel, módulo desatualizado e erro de integração de OS.",
        "canal_atual": "WhatsApp / Direto",
        "acionado_atual": "Consultor -> Apoio (Edson)",
        "destino_correto": "Filtro de Demandas Dedicado",
        "impacto": "Alto",
        "acao_recomendada": "Designar uma pessoa para filtrar as demandas técnicas e entender a situação antes de acionar a equipe de apoio."
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

# Navegação por Abas
aba1, aba2 = st.tabs(["📊 Visão Geral Atual", "🔄 Detalhamento - Como Resolver?"])

# ABA 1: VISÃO GERAL ATUAL
with aba1:
    # ENCAPSULAMENTO GLASSMORPHISM DO BLOCO COMPLETO DO GRÁFICO
    with st.container():
        st.html("""
            <div class="glass-card-full">
                <div class="glass-card-header">
                    <div class="glass-card-title">
                        <span>📊 Distribuição por Nível de Impacto</span>
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
        
        # Efeito visual de destaque nas fatias
        pull_effect = [0.06 if l in ['Muito Alto', 'Alto'] else 0.02 for l in labels]

        fig_pizza = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.6,
            pull=pull_effect,
            direction='clockwise',
            sort=False,
            marker=dict(
                colors=colors, 
                line=dict(color='#0A141D', width=2)
            ),
            hovertemplate="<b>Impacto %{label}</b><br>Casos: <b>%{value}</b><br>Proporção: <b>%{percent}</b><extra></extra>",
            textinfo="label+value",
            texttemplate="<b>%{label}</b><br>%{value}",
            textposition="outside",
            textfont=dict(color='#E2E8F0', size=12, family="sans-serif")
        )])

        fig_pizza.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                font=dict(color="#CBD5E1", size=11)
            ),
            margin=dict(t=15, b=25, l=30, r=30),
            height=260,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            annotations=[dict(
                text=f'<span style="font-size:22px;font-weight:800;color:#FFFFFF">{total_situacoes}</span><br><span style="font-size:10px;color:#38BDF8;font-weight:700">TOTAL</span>',
                x=0.5, y=0.5, font_size=14, showarrow=False
            )]
        )

        st.plotly_chart(fig_pizza, use_container_width=True, config={'displayModeBar': False})
        st.html("</div>")
    
    # BARRA DE PROGRESSO DO GARGALO OPERACIONAL
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

    st.markdown("---")
    st.markdown("### Resumo das Situações Atuais")

    # CONSTRUÇÃO DO HTML DA TABELA CUSTOMIZADA
    rows_html = ""
    for _, row in df.iterrows():
        badge = get_impact_badge(row["impacto"])
        rows_html += f"<tr><td><strong>{row['id']}. {row['problema_atual']}</strong></td><td>{row['canal_atual']}</td><td>{row['acionado_atual']}</td><td>{row['destino_correto']}</td><td>{badge}</td></tr>"

    table_html = f"""<div class="table-container"><table class="custom-table"><thead><tr><th>Problema Atual</th><th>Canal Atual</th><th>Quem é Acionado Hoje</th><th>Destino Correto</th><th>Nível de Impacto</th></tr></thead><tbody>{rows_html}</tbody></table></div>"""
    
    st.html(table_html)

    # CARD DA EQUIPE REESTRUTURADO PARA RECEBER A FOTO
    src_foto_equipe = f"data:image/jpeg;base64,{foto_equipe_b64}" if foto_equipe_b64 else ""

    if src_foto_equipe:
        foto_html = f'<img src="{src_foto_equipe}" class="team-photo" alt="Equipe do Projeto">'
    else:
        foto_html = '''
            <div style="color: #94A3B8; text-align: center; padding: 40px 20px;">
                <span style="font-size: 2rem;">📷</span><br>
                <strong style="color: #E2E8F0;">Espaço Reservado para a Foto da Equipe</strong><br>
                <small style="color: #64748B;">Adicione o arquivo 'equipe_fluxo.jpg' na pasta do projeto.</small>
            </div>
        '''

    st.html(f"""
        <div class="team-card">
            <div class="team-card-header">
                <div class="team-card-title">
                    <span>👥 Equipe do Projeto</span>
                </div>
                <span class="team-leader-badge">Líder: Paulo Terra</span>
            </div>
            
            <!-- ÁREA DA FOTO DA EQUIPE -->
            <div class="team-photo-container">
                {foto_html}
            </div>

            <!-- TAGS DOS INTEGRANTES (NOMES ELEGANTES) -->
            <div class="team-members-tags-container">
                <div class="member-tag"><span>•</span> Fabio Silva</div>
                <div class="member-tag"><span>•</span> Lucas Ribeiro</div>
                <div class="member-tag"><span>•</span> Maria Eduarda Barbosa</div>
                <div class="member-tag"><span>•</span> Verusca Cristina</div>
                <div class="member-tag"><span>•</span> Karilene Esteves</div>
                <div class="member-tag"><span>•</span> Higor Souza</div>
                <div class="member-tag"><span>•</span> Caio Monteiro</div>
            </div>
        </div>
    """)

# ABA 2: DETALHAMENTO - COMO RESOLVER?
with aba2:
    st.subheader("Detalhamento Ponto a Ponto: Como Resolver")
    
    opcoes_select = [f"{row['id']}. {row['problema_atual']}" for _, row in df.iterrows()]
    
    item_selecionado_str = st.selectbox(
        "Selecione o Problema Atual para Analisar a Solução:",
        options=opcoes_select
    )
    
    selected_id = int(item_selecionado_str.split(".")[0])

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

    # DESTRINCHAMENTO - CAUSA 7
    elif selected_id == 7:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 7: Trava no Cliente (Acionamento Oficina)")
        
        col_7_1, col_7_2 = st.columns(2)
        
        with col_7_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * A oficina entra em contato buscando apoio quando identifica travamentos no cliente (ex: falta de equipamento, falhas no aplicativo).
            * O técnico aciona **diretamente o consultor** para qualquer pendência ocorrida em campo.
            """)
            st.warning("""
            **Impacto:**
            * Gera **altas demandas e sobrecarga** frequente de chamados operacionais no consultor.
            """)
            
        with col_7_2:
            st.markdown("### ⚙️ Solução Proposta (Triagem / Ponto Focal)")
            st.success("""
            **Designação de Ponto Focal para Triagem:**
            * Definição de **uma pessoa responsável por filtrar as demandas** e compreender a situação técnica/operacional.
            * **Fluxo de Escalonamento:** Apenas casos que exijam atuação comercial ou negociação direta com a liderança do cliente serão repassados ao consultor.
            """)

    # DESTRINCHAMENTO - CAUSA 8
    elif selected_id == 8:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 8: Falta de Dados na OS")
        
        col_8_1, col_8_2 = st.columns(2)
        
        with col_8_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * Falta de dados essenciais na Ordem de Serviço, especificamente o endereço do cliente ou a localização exata de onde a frota se encontra no momento do atendimento.
            * O técnico aciona **diretamente o consultor** quando identifica qualquer pendência de falta de informações na OS.
            """)
            st.warning("""
            **Impacto:**
            * Gera **altas demandas e sobrecarga** operacional constante no consultor para resolução de inconsistências cadastrais.
            """)
            
        with col_8_2:
            st.markdown("### ⚙️ Solução Proposta (Agendamento GR)")
            st.success("""
            **Direcionamento para Agendamento GR:**
            * Redirecionar os acionamentos por falta de dados de localização diretamente para o **time de agendamento GR**.
            * Cabe a essa equipe realizar a validação prévia e inclusão dos dados de endereço antes de enviar a OS para atendimento em campo.
            """)

    # DESTRINCHAMENTO - CAUSA 9
    elif selected_id == 9:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 9: Encaixe de Agendamento")
        
        col_9_1, col_9_2 = st.columns(2)
        
        with col_9_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * Acionamento do consultor para realizar encaixes de agendamento na grade de atendimento.
            * Quem recebe a solicitação entra em contato diretamente com o consultor via **WhatsApp, E-mail ou Slack**.
            """)
            st.warning("""
            **Impacto:**
            * Gera **altas demandas e interrupções rotineiras** no trabalho estratégico do consultor.
            """)
            
        with col_9_2:
            st.markdown("### ⚙️ Solução Proposta (Atendimento Direto / GR)")
            st.success("""
            **Acesso Direto às Oficinas ou Agendamento GR:**
            * Permitir o **acesso direto às oficinas** ou canalizar as solicitações via fluxo de **agendamento GR**.
            * **Regra de Escalonamento:** O consultor só deverá ser acionado **caso não haja retorno ou posicionamento** por parte da oficina ou da equipe de agendamento.
            """)

    # DESTRINCHAMENTO - CAUSA 10
    elif selected_id == 10:
        st.markdown("---")
        st.markdown("## 🔍 Destrinchamento da Causa 10: Acionamento sobre Tecnologia")
        
        col_10_1, col_10_2 = st.columns(2)
        
        with col_10_1:
            st.markdown("### ⚠️ Como é feito hoje & Impacto")
            st.error("""
            **Como é feito hoje?**
            * Ocorrem falhas como: **módulo sem atualização no firmware**, **falha no aplicativo móvel**, **módulo sem atualização** e **erro de integração de OS**.
            * O técnico faz o acionamento diretamente para o consultor.
            * O consultor precisa acionar o apoio ao técnico (**Edson**) para verificar a situação.
            """)
            st.warning("""
            **Impacto:**
            * **Altas demandas acentuadas** tanto para o consultor quanto para o time de apoio técnico.
            """)
            
        with col_10_2:
            st.markdown("### ⚙️ Solução Proposta (Triagem Técnica)")
            st.success("""
            **Designação de Ponto Focal para Filtro:**
            * Alocar **uma pessoa dedicada para filtrar as demandas** e compreender antecipadamente a situação técnica.
            * **Evitar o Triângulo de Acionamento:** Eliminar a intermédio do consultor, direcionando apenas chamados pré-validados para a equipe de apoio técnico.
            """)
