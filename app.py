import streamlit as st
import re
from datetime import datetime

st.set_page_config(
    page_title="CyberSafe Community",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(circle at 15% 10%, rgba(34, 211, 238, 0.22) 0, transparent 28%),
            radial-gradient(circle at 85% 15%, rgba(16, 185, 129, 0.16) 0, transparent 30%),
            linear-gradient(135deg, #020617 0%, #07111f 45%, #020617 100%);
        color: #e5e7eb;
    }

    .stApp:before {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            linear-gradient(rgba(34, 211, 238, 0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(34, 211, 238, 0.04) 1px, transparent 1px);
        background-size: 42px 42px;
        pointer-events: none;
        z-index: 0;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1180px;
        position: relative;
        z-index: 1;
    }

    section[data-testid="stSidebar"] {
        background: rgba(2, 6, 23, 0.94);
        border-right: 1px solid rgba(34, 211, 238, 0.22);
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    .cyber-hero {
        background:
            linear-gradient(135deg, rgba(14, 165, 233, 0.24), rgba(16, 185, 129, 0.18)),
            rgba(2, 6, 23, 0.78);
        border: 1px solid rgba(34, 211, 238, 0.38);
        border-radius: 28px;
        padding: 44px;
        margin-bottom: 28px;
        box-shadow: 0 24px 70px rgba(0, 0, 0, 0.42), inset 0 0 32px rgba(34, 211, 238, 0.06);
        position: relative;
        overflow: hidden;
    }

    .cyber-hero:before {
        content: "01001001 101010 11001 001101";
        position: absolute;
        right: 28px;
        top: 22px;
        color: rgba(103, 232, 249, 0.13);
        font-size: 0.9rem;
        letter-spacing: 4px;
        font-weight: 800;
    }

    .hero-badge {
        display: inline-flex;
        background: rgba(34, 211, 238, 0.10);
        border: 1px solid rgba(34, 211, 238, 0.36);
        border-radius: 999px;
        padding: 8px 14px;
        font-size: 0.92rem;
        font-weight: 700;
        margin-bottom: 18px;
        color: #a5f3fc;
    }

    .hero-title {
        font-size: clamp(2.1rem, 4vw, 4.4rem);
        line-height: 1.02;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 14px;
        max-width: 900px;
        text-shadow: 0 0 24px rgba(34, 211, 238, 0.26);
    }

    .hero-subtitle {
        font-size: 1.15rem;
        line-height: 1.7;
        color: #cbd5e1;
        max-width: 820px;
        margin-bottom: 26px;
    }

    .hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }

    .pill {
        display: inline-flex;
        padding: 10px 14px;
        border-radius: 999px;
        background: rgba(15, 23, 42, 0.88);
        color: #e0f2fe;
        font-weight: 750;
        border: 1px solid rgba(34, 211, 238, 0.24);
    }

    .section-title {
        color: #f8fafc;
        font-size: 1.7rem;
        font-weight: 850;
        margin: 22px 0 14px 0;
    }

    .section-subtitle {
        color: #cbd5e1;
        font-size: 1rem;
        margin-bottom: 18px;
    }

    .cyber-card {
        background: rgba(2, 6, 23, 0.76);
        border: 1px solid rgba(34, 211, 238, 0.22);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 18px 48px rgba(0, 0, 0, 0.30), inset 0 0 24px rgba(34, 211, 238, 0.035);
        min-height: 185px;
        transition: 0.2s ease-in-out;
        margin-bottom: 14px;
    }

    .cyber-card:hover {
        transform: translateY(-3px);
        border-color: rgba(45, 212, 191, 0.60);
        box-shadow: 0 24px 55px rgba(0, 0, 0, 0.38), 0 0 22px rgba(34, 211, 238, 0.10);
    }

    .card-icon {
        width: 50px;
        height: 50px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.55rem;
        background: linear-gradient(135deg, rgba(34, 211, 238, 0.20), rgba(16, 185, 129, 0.18));
        border: 1px solid rgba(34, 211, 238, 0.18);
        margin-bottom: 16px;
    }

    .card-title {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .card-text {
        color: #cbd5e1;
        line-height: 1.65;
        font-size: 0.98rem;
    }

    .metric-card {
        background: rgba(2, 6, 23, 0.68);
        border: 1px solid rgba(34, 211, 238, 0.22);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: inset 0 0 22px rgba(34, 211, 238, 0.035);
        margin-bottom: 12px;
    }

    .metric-number {
        font-size: 2rem;
        color: #67e8f9;
        font-weight: 900;
    }

    .metric-label {
        color: #cbd5e1;
        font-weight: 650;
        margin-top: 4px;
    }

    .info-box, .success-box, .warning-box, .danger-box {
        border-radius: 18px;
        padding: 18px 20px;
        line-height: 1.65;
        margin: 14px 0;
    }

    .info-box {
        background: rgba(14, 165, 233, 0.11);
        border: 1px solid rgba(125, 211, 252, 0.32);
        color: #e0f2fe;
    }

    .success-box {
        background: rgba(16, 185, 129, 0.13);
        border: 1px solid rgba(52, 211, 153, 0.38);
        color: #dcfce7;
    }

    .warning-box {
        background: rgba(245, 158, 11, 0.13);
        border: 1px solid rgba(251, 191, 36, 0.38);
        color: #fef3c7;
    }

    .danger-box {
        background: rgba(239, 68, 68, 0.13);
        border: 1px solid rgba(248, 113, 113, 0.38);
        color: #fee2e2;
    }

    .timeline-item {
        background: rgba(2, 6, 23, 0.72);
        border-left: 4px solid #22d3ee;
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 12px;
        border-top: 1px solid rgba(34, 211, 238, 0.18);
        border-right: 1px solid rgba(34, 211, 238, 0.18);
        border-bottom: 1px solid rgba(34, 211, 238, 0.18);
    }

    .footer {
        margin-top: 36px;
        padding: 18px;
        text-align: center;
        color: #94a3b8;
        border-top: 1px solid rgba(34, 211, 238, 0.18);
    }

    .stButton > button {
        background: linear-gradient(135deg, #0891b2, #059669);
        color: white;
        border: 0;
        border-radius: 14px;
        padding: 0.7rem 1.1rem;
        font-weight: 800;
        box-shadow: 0 12px 28px rgba(8, 145, 178, 0.22);
    }

    .stButton > button:hover {
        border: 0;
        color: white;
        transform: translateY(-1px);
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        border-radius: 14px;
        background-color: rgba(15, 23, 42, 0.92);
        color: #e5e7eb;
        border: 1px solid rgba(34, 211, 238, 0.25);
    }

    h1, h2, h3, h4, p, li, span, label {
        color: inherit;
    }
</style>
""", unsafe_allow_html=True)


def avaliar_senha(senha):
    pontos = 0
    criterios = []

    regras = [
        (len(senha) >= 8, "Possui pelo menos 8 caracteres", "Possui menos de 8 caracteres"),
        (bool(re.search(r"[A-Z]", senha)), "Possui letra maiúscula", "Não possui letra maiúscula"),
        (bool(re.search(r"[a-z]", senha)), "Possui letra minúscula", "Não possui letra minúscula"),
        (bool(re.search(r"[0-9]", senha)), "Possui número", "Não possui número"),
        (bool(re.search(r"[^A-Za-z0-9]", senha)), "Possui caractere especial", "Não possui caractere especial"),
    ]

    for ok, positivo, negativo in regras:
        if ok:
            pontos += 1
            criterios.append(f"✅ {positivo}")
        else:
            criterios.append(f"❌ {negativo}")

    if pontos <= 2:
        nivel = "Fraca"
    elif pontos <= 4:
        nivel = "Média"
    else:
        nivel = "Forte"

    return nivel, pontos, criterios


def analisar_golpe(respostas):
    risco = sum(respostas)

    if risco <= 1:
        return "Baixo", "A mensagem possui poucos sinais de risco. Ainda assim, confira o remetente, o link e o contexto antes de seguir qualquer orientação."
    elif risco <= 3:
        return "Médio", "A mensagem apresenta sinais suspeitos. Evite clicar em links, não informe dados pessoais e confirme a informação por um canal oficial."
    else:
        return "Alto", "A mensagem apresenta vários sinais de golpe. Não clique em links, não envie dados, bloqueie o contato e denuncie quando possível."


def footer():
    st.markdown("""
    <div class="footer">
        🛡️ CyberSafe Community • Segurança Digital para Todos
    </div>
    """, unsafe_allow_html=True)


st.sidebar.markdown("## 🛡️ CyberSafe")
pagina = st.sidebar.radio(
    "Navegação",
    [
        "Início",
        "Checklist de Golpes",
        "Teste de Senha",
        "Quiz Educativo",
        "Dicas de Segurança",
        "Feedback da Comunidade",
        "Sobre o Projeto"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div class="info-box">
    <b>Segurança Digital para Todos</b><br><br>
    Aprenda a identificar ameaças comuns, proteger dados pessoais e navegar com mais segurança.
</div>
""", unsafe_allow_html=True)


if pagina == "Início":
    st.markdown("""
    <div class="cyber-hero">
        <div class="hero-badge">🛡️ CyberSafe Community</div>
        <div class="hero-title">Segurança Digital na Prática</div>
        <div class="hero-subtitle">
            Aprenda a reconhecer golpes virtuais, proteger suas contas, criar senhas mais seguras e cuidar melhor dos seus dados pessoais.
        </div>
        <div class="hero-actions">
            <div class="pill">🕵️ Análise de golpes</div>
            <div class="pill">🔑 Senhas seguras</div>
            <div class="pill">🧠 Quiz rápido</div>
            <div class="pill">🔐 Proteção de dados</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="cyber-card">
            <div class="card-icon">🎯</div>
            <div class="card-title">Aprendizado prático</div>
            <div class="card-text">
                Conteúdos simples e diretos para aplicar no dia a dia, mesmo sem conhecimento técnico.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="cyber-card">
            <div class="card-icon">⚠️</div>
            <div class="card-title">Prevenção de golpes</div>
            <div class="card-text">
                Identifique mensagens suspeitas, links falsos, falsas promoções e tentativas de roubo de dados.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="cyber-card">
            <div class="card-icon">🔐</div>
            <div class="card-title">Proteção de contas</div>
            <div class="card-text">
                Veja boas práticas para senhas, autenticação em dois fatores e cuidado com informações pessoais.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Ferramentas disponíveis</div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown('<div class="metric-card"><div class="metric-number">6</div><div class="metric-label">sinais de golpe</div></div>', unsafe_allow_html=True)

    with m2:
        st.markdown('<div class="metric-card"><div class="metric-number">5</div><div class="metric-label">critérios de senha</div></div>', unsafe_allow_html=True)

    with m3:
        st.markdown('<div class="metric-card"><div class="metric-number">5</div><div class="metric-label">perguntas rápidas</div></div>', unsafe_allow_html=True)

    with m4:
        st.markdown('<div class="metric-card"><div class="metric-number">24h</div><div class="metric-label">acesso online</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Como começar</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item"><b>1. Verifique mensagens suspeitas</b><br>Use o checklist para avaliar sinais de golpe em mensagens, links e contatos desconhecidos.</div>
    <div class="timeline-item"><b>2. Avalie uma senha de exemplo</b><br>Entenda quais elementos aumentam a segurança de uma senha.</div>
    <div class="timeline-item"><b>3. Teste seus conhecimentos</b><br>Responda ao quiz e veja seu desempenho em segurança digital.</div>
    <div class="timeline-item"><b>4. Compartilhe sua opinião</b><br>Envie um feedback sobre a experiência de uso da plataforma.</div>
    """, unsafe_allow_html=True)

    footer()


elif pagina == "Checklist de Golpes":
    st.markdown('<div class="section-title">🕵️ Checklist de Golpes Digitais</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Marque os sinais encontrados na mensagem, link, e-mail ou contato recebido.</div>', unsafe_allow_html=True)

    perguntas = [
        "A mensagem tenta criar urgência, como 'clique agora', 'última chance' ou 'sua conta será bloqueada'?",
        "O remetente é desconhecido ou parece se passar por uma empresa/pessoa conhecida?",
        "O link está estranho, encurtado ou diferente do endereço oficial?",
        "A mensagem pede senha, código SMS, token, PIX ou dados bancários?",
        "A oferta parece boa demais para ser verdade?",
        "A mensagem possui erros, logo distorcido ou aparência pouco confiável?"
    ]

    respostas = []

    for pergunta in perguntas:
        resposta = st.checkbox(pergunta)
        respostas.append(1 if resposta else 0)

    if st.button("Analisar risco"):
        nivel, orientacao = analisar_golpe(respostas)
        classe = "success-box" if nivel == "Baixo" else "warning-box" if nivel == "Médio" else "danger-box"

        st.markdown(f"""
        <div class="{classe}">
            <h3>Risco identificado: {nivel}</h3>
            <p>{orientacao}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="cyber-card">
            <div class="card-title">O que fazer agora?</div>
            <div class="card-text">
                • Não clique em links suspeitos;<br>
                • Não informe senhas, códigos ou dados bancários;<br>
                • Procure o canal oficial da empresa ou pessoa envolvida;<br>
                • Desconfie de mensagens com pressão ou promessa exagerada;<br>
                • Bloqueie e denuncie contatos suspeitos.
            </div>
        </div>
        """, unsafe_allow_html=True)

    footer()


elif pagina == "Teste de Senha":
    st.markdown('<div class="section-title">🔑 Teste Educativo de Senha</div>', unsafe_allow_html=True)
    st.markdown('<div class="warning-box">Digite apenas uma senha fictícia para teste. Não use senhas reais de contas pessoais.</div>', unsafe_allow_html=True)

    senha = st.text_input("Senha de exemplo:", type="password")

    if senha:
        nivel, pontos, criterios = avaliar_senha(senha)

        st.markdown(f'<div class="section-title">Resultado: {nivel}</div>', unsafe_allow_html=True)
        st.progress(pontos / 5)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown('<div class="cyber-card"><div class="card-title">Critérios avaliados</div>', unsafe_allow_html=True)
            for criterio in criterios:
                st.write(criterio)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="cyber-card">
                <div class="card-title">Boas práticas</div>
                <div class="card-text">
                    • Use senhas longas sempre que possível;<br>
                    • Misture letras, números e símbolos;<br>
                    • Evite nomes, datas e informações pessoais;<br>
                    • Não reutilize a mesma senha em vários serviços;<br>
                    • Ative autenticação em dois fatores.
                </div>
            </div>
            """, unsafe_allow_html=True)

    footer()


elif pagina == "Quiz Educativo":
    st.markdown('<div class="section-title">🧠 Quiz de Segurança Digital</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Responda às perguntas e veja sua pontuação ao final.</div>', unsafe_allow_html=True)

    pontos = 0

    q1 = st.radio(
        "1. O que é phishing?",
        ["Um tipo de antivírus", "Uma tentativa de enganar pessoas para roubar dados", "Um método seguro de login", "Um programa de backup"]
    )
    if q1 == "Uma tentativa de enganar pessoas para roubar dados":
        pontos += 1

    q2 = st.radio(
        "2. Qual é uma boa prática de segurança?",
        ["Usar a mesma senha em todos os sites", "Compartilhar código SMS com atendente", "Ativar autenticação em dois fatores", "Clicar em links recebidos de desconhecidos"]
    )
    if q2 == "Ativar autenticação em dois fatores":
        pontos += 1

    q3 = st.radio(
        "3. O que fazer ao receber um link suspeito?",
        ["Clicar rapidamente", "Enviar para todos os contatos", "Ignorar a aparência do link", "Verificar o remetente e acessar o site oficial manualmente"]
    )
    if q3 == "Verificar o remetente e acessar o site oficial manualmente":
        pontos += 1

    q4 = st.radio(
        "4. Qual senha é mais segura?",
        ["123456", "senha123", "NomeDataNascimento", "F!lme#Casa2026"]
    )
    if q4 == "F!lme#Casa2026":
        pontos += 1

    q5 = st.radio(
        "5. O que nunca deve ser compartilhado por WhatsApp?",
        ["Figurinhas", "Código de verificação, senha ou token bancário", "Mensagem de bom dia", "Link de site oficial conferido"]
    )
    if q5 == "Código de verificação, senha ou token bancário":
        pontos += 1

    if st.button("Ver resultado"):
        if pontos <= 2:
            st.markdown(f'<div class="danger-box"><h3>Você acertou {pontos} de 5 perguntas.</h3>Revise as dicas de segurança para se proteger melhor.</div>', unsafe_allow_html=True)
        elif pontos <= 4:
            st.markdown(f'<div class="warning-box"><h3>Você acertou {pontos} de 5 perguntas.</h3>Bom resultado. Continue praticando hábitos seguros.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="success-box"><h3>Você acertou {pontos} de 5 perguntas.</h3>Excelente resultado. Você demonstrou boa noção de segurança digital.</div>', unsafe_allow_html=True)

    footer()


elif pagina == "Dicas de Segurança":
    st.markdown('<div class="section-title">🛡️ Dicas Rápidas de Segurança Digital</div>', unsafe_allow_html=True)

    dicas = [
        ("🚨", "Cuidado com urgência", "Golpistas costumam usar medo e pressa para fazer a vítima clicar em links ou enviar dados."),
        ("🔢", "Proteja seus códigos", "Códigos recebidos por SMS, e-mail ou aplicativo são pessoais e não devem ser enviados para ninguém."),
        ("🔐", "Ative o 2FA", "A autenticação em dois fatores adiciona uma camada extra de proteção nas contas."),
        ("🔎", "Confira links", "Verifique se o endereço é oficial. Na dúvida, digite o site manualmente no navegador."),
        ("🔄", "Atualize sistemas", "Atualizações corrigem falhas de segurança e ajudam a proteger seus dispositivos."),
        ("🛍️", "Desconfie de promoções", "Ofertas muito abaixo do preço normal podem ser tentativa de golpe."),
    ]

    for i in range(0, len(dicas), 2):
        c1, c2 = st.columns(2)
        for col, dica in zip([c1, c2], dicas[i:i+2]):
            with col:
                icone, titulo, texto = dica
                st.markdown(f"""
                <div class="cyber-card">
                    <div class="card-icon">{icone}</div>
                    <div class="card-title">{titulo}</div>
                    <div class="card-text">{texto}</div>
                </div>
                """, unsafe_allow_html=True)

    footer()


elif pagina == "Feedback da Comunidade":
    st.markdown('<div class="section-title">📝 Feedback da Comunidade</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">Sua opinião ajuda a melhorar esta iniciativa e tornar o conteúdo mais claro, útil e acessível para outras pessoas.</div>', unsafe_allow_html=True)

    nome = st.text_input("Nome ou identificação:")
    perfil = st.selectbox("Perfil:", ["Aluno", "Professor", "Familiar", "Funcionário", "Pequeno comerciante", "Morador da comunidade", "Outro"])
    avaliacao = st.slider("De 0 a 10, quanto este conteúdo foi útil?", 0, 10, 8)
    aprendeu = st.radio("Você aprendeu algo novo sobre segurança digital?", ["Sim", "Parcialmente", "Não"])
    comentario = st.text_area("Comentário ou sugestão:")

    if st.button("Enviar feedback"):
        if nome.strip() == "":
            st.error("Informe um nome ou identificação para continuar.")
        else:
            st.markdown("""
            <div class="success-box">
                <h3>Feedback enviado com sucesso!</h3>
                Obrigado por contribuir com a melhoria da iniciativa CyberSafe Community.
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="cyber-card">
                <div class="card-title">Resumo do feedback</div>
                <div class="card-text">
                    <b>Participante:</b> {nome}<br>
                    <b>Perfil:</b> {perfil}<br>
                    <b>Avaliação:</b> {avaliacao}/10<br>
                    <b>Aprendizado:</b> {aprendeu}<br>
                    <b>Comentário:</b> {comentario}<br>
                    <b>Data/Hora:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
                </div>
            </div>
            """, unsafe_allow_html=True)

    footer()


elif pagina == "Sobre o Projeto":
    st.markdown('<div class="section-title">📄 Sobre o Projeto</div>', unsafe_allow_html=True)

    conteudos = [
        ("Título", "Segurança Digital na Prática: prevenção contra golpes virtuais e proteção de dados pessoais."),
        ("Objetivo", "Orientar a comunidade sobre riscos digitais comuns e boas práticas de proteção no uso da internet."),
        ("Problema abordado", "Muitas pessoas recebem mensagens falsas, links suspeitos e tentativas de golpe, mas nem sempre sabem como identificar os sinais de risco."),
        ("Solução", "Uma aplicação web educativa com checklist de golpes, teste de senha, quiz e dicas práticas de segurança digital."),
        ("Público", "Alunos, familiares, pequenos comerciantes, professores, funcionários e moradores da comunidade."),
        ("Resultado esperado", "Contribuir para que mais pessoas consigam reconhecer golpes virtuais e proteger melhor seus dados pessoais."),
    ]

    for titulo, texto in conteudos:
        st.markdown(f"""
        <div class="timeline-item">
            <b>{titulo}</b><br>{texto}
        </div>
        """, unsafe_allow_html=True)

    footer()
