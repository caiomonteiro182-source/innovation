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

# Dados das Causas / Problemas Atuais (sem coluna de ID)
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

# Renomeando as colunas para exibição amigável na tabela
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
aba1, aba2 = st.tabs(["📊 Visão Geral & Vídeo", "🔄 Matriz de Redirecionamento"])

# ABA 1: VISÃO GERAL + VÍDEO
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

# ABA 2: DETALHAMENTO E RESOLUÇÃO DOS PONTOS
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
