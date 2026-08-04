import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Diagnóstico & Solução de Acionamentos",
    page_icon="🛠️",
    layout="wide"
)

# Título Principal
st.title("🛠️ Diagnóstico de Acionamentos & Matriz de Solução")
st.caption("Visão atual dos gargalos operacionais e proposta de reestruturação dos fluxos.")

st.divider()

# Dados dos 9 Pontos
dados_acionamentos = [
    {
        "id": 1,
        "causa": "Falta de Equipamento",
        "canal_atual": "WhatsApp / E-mail",
        "acionado_atual": "Consultor",
        "destino_correto": "Planejamento / Suprimentos",
        "impacto": "Alto",
        "acao_recomendada": "Criar fluxo direto para o time de Planejamento de estoque."
    },
    {
        "id": 2,
        "causa": "Problemas na Oficina",
        "canal_atual": "WhatsApp / Slack",
        "acionado_atual": "Consultor",
        "destino_correto": "Gestão de Oficinas",
        "impacto": "Alto",
        "acao_recomendada": "Painel de visibilidade de capacidade e fila de atendimento."
    },
    {
        "id": 3,
        "causa": "Falta de Inventário na Oficina",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Back Office / Sistema de Estoque",
        "impacto": "Muito Alto",
        "acao_recomendada": "Obrigatoriedade de checklist diário antes do acionamento."
    },
    {
        "id": 4,
        "causa": "Avarias, Danos e Riscos",
        "canal_atual": "E-mail / WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Setor de Qualidade / Vistoria",
        "impacto": "Médio",
        "acao_recomendada": "Formulário padronizado com upload obrigatório de foto."
    },
    {
        "id": 5,
        "causa": "Acionamento Back Office Oficina",
        "canal_atual": "Slack / WhatsApp",
        "acionado_atual": "Consultor (Bypass)",
        "destino_correto": "Back Office da Oficina",
        "impacto": "Médio",
        "acao_recomendada": "Trava de sistema: só liberar consultor se Back Office não atender."
    },
    {
        "id": 6,
        "causa": "Integração / Documentação",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Portal de Conhecimento / Self-Service",
        "impacto": "Baixo",
        "acao_recomendada": "Disponibilizar central de ajuda com download de documentos."
    },
    {
        "id": 7,
        "causa": "Trava no Cliente (Sem frota no local)",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Consultor (Válido)",
        "impacto": "Alto",
        "acao_recomendada": "Ficha de impeditivo rápida para atuação comercial do consultor."
    },
    {
        "id": 8,
        "causa": "Falta de Dados na OS",
        "canal_atual": "WhatsApp / E-mail",
        "acionado_atual": "Consultor",
        "destino_correto": "Emissor da OS / Validação Automática",
        "impacto": "Médio",
        "acao_recomendada": "Bloqueio de abertura de OS sem campos de endereço e frota."
    },
    {
        "id": 9,
        "causa": "Encaixe de Agendamento",
        "canal_atual": "WhatsApp",
        "acionado_atual": "Consultor",
        "destino_correto": "Back Office Oficina",
        "impacto": "Médio",
        "acao_recomendada": "Fila única de solicitações de encaixe no Back Office."
    }
]

df = pd.DataFrame(dados_acionamentos)

# Navegação por Abas
aba1, aba2 = st.tabs(["📊 Visão Geral & Diagnóstico", "🔄 Matriz de Redirecionamento"])

# ABA 1: VISÃO GERAL
with aba1:
    st.subheader("Métricas do Processo Atual")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Pontos Mapeados", len(df))
    col2.metric("Acionamentos Indevidos ao Consultor", "7 de 9", delta="-77%", delta_color="inverse")
    col3.metric("Canais Pulverizados", "3 (WhatsApp, E-mail, Slack)")
    
    st.markdown("### Tabela Resumo dos Gargalos Operacionais")
    st.dataframe(
        df[["id", "causa", "canal_atual", "acionado_atual", "destino_correto", "impacto"]],
        use_container_width=True,
        hide_index=True
    )

# ABA 2: DETALHAMENTO E RESOLUÇÃO DOS PONTOS
with aba2:
    st.subheader("Detalhamento Ponto a Ponto: Como Resolver")
    
    item_selecionado = st.selectbox(
        "Selecione o Acionamento para Analisar a Solução:",
        options=df["causa"].tolist()
    )
    
    detalhe = df[df["causa"] == item_selecionado].iloc[0]
    
    st.markdown("---")
    
    col_esquerda, col_direita = st.columns(2)
    
    with col_esquerda:
        st.markdown("### ❌ Como é feito hoje")
        st.warning(f"**Causa:** {detalhe['causa']}")
        st.write(f"**Canal de Entrada:** {detalhe['canal_atual']}")
        st.write(f"**Quem é acionado:** {detalhe['acionado_atual']}")
        st.write(f"**Impacto Operacional:** {detalhe['impacto']}")
        
    with col_direita:
        st.markdown("### ✅ Fluxo Proposto (Solução)")
        st.success(f"**Destino Correto:** {detalhe['destino_correto']}")
        st.info(f"**O que deve ser feito:** {detalhe['acao_recomendada']}")
