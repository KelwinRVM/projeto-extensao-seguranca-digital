import streamlit as st
import re
from datetime import datetime

st.set_page_config(
    page_title="Segurança Digital na Prática",
    page_icon="🔐",
    layout="wide"
)

# -----------------------------
# ESTILO
# -----------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #0f172a;
    }
    .subtitle {
        font-size: 20px;
        color: #334155;
    }
    .card {
        background-color: #f8fafc;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }
    .success-card {
        background-color: #ecfdf5;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #10b981;
    }
    .warning-card {
        background-color: #fffbeb;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #f59e0b;
    }
    .danger-card {
        background-color: #fef2f2;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #ef4444;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# FUNÇÕES
# -----------------------------
def avaliar_senha(senha):
    pontos = 0
    criterios = []

    if len(senha) >= 8:
        pontos += 1
        criterios.append("✅ Possui pelo menos 8 caracteres")
    else:
        criterios.append("❌ Possui menos de 8 caracteres")

    if re.search(r"[A-Z]", senha):
        pontos += 1
        criterios.append("✅ Possui letra maiúscula")
    else:
        criterios.append("❌ Não possui letra maiúscula")

    if re.search(r"[a-z]", senha):
        pontos += 1
        criterios.append("✅ Possui letra minúscula")
    else:
        criterios.append("❌ Não possui letra minúscula")

    if re.search(r"[0-9]", senha):
        pontos += 1
        criterios.append("✅ Possui número")
    else:
        criterios.append("❌ Não possui número")

    if re.search(r"[^A-Za-z0-9]", senha):
        pontos += 1
        criterios.append("✅ Possui caractere especial")
    else:
        criterios.append("❌ Não possui caractere especial")

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
        return "Baixo", "A mensagem possui poucos sinais de golpe, mas ainda assim é importante conferir remetente, link e contexto."
    elif risco <= 3:
        return "Médio", "A mensagem apresenta alguns sinais suspeitos. Evite clicar em links e confirme a informação por outro canal."
    else:
        return "Alto", "A mensagem possui vários sinais de golpe. Não clique em links, não envie dados e bloqueie/denuncie o contato."


# -----------------------------
# MENU LATERAL
# -----------------------------
st.sidebar.title("🔐 Menu")
pagina = st.sidebar.radio(
    "Escolha uma opção:",
    [
        "Início",
        "Checklist de Golpes",
        "Teste de Senha",
        "Quiz Educativo",
        "Dicas de Segurança",
        "Feedback da Comunidade",
        "Relatório do Projeto"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Projeto de Extensão - Segurança da Informação\n\n"
    "Tema: Conscientização sobre segurança digital."
)


# -----------------------------
# PÁGINA INÍCIO
# -----------------------------
if pagina == "Início":
    st.markdown('<div class="main-title">Segurança Digital na Prática</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Um aplicativo educativo para ajudar a comunidade a se proteger contra golpes virtuais.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎯 Objetivo</h3>
            <p>Orientar pessoas da comunidade sobre boas práticas de segurança digital, proteção de dados e prevenção contra golpes virtuais.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>👥 Público-alvo</h3>
            <p>Alunos, familiares, pequenos comerciantes, professores, funcionários e demais membros da comunidade local.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>💡 Proposta</h3>
            <p>Disponibilizar uma ferramenta simples, gratuita e educativa para identificar riscos digitais do dia a dia.</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Sobre o projeto")

    st.write("""
    Este projeto foi desenvolvido como uma atividade de extensão do curso de Segurança da Informação.
    A proposta é aproximar o conhecimento acadêmico da realidade da comunidade, levando orientações práticas
    sobre segurança digital, prevenção de golpes e proteção de dados pessoais.
    """)

    st.write("""
    O aplicativo apresenta conteúdos simples e interativos, permitindo que qualquer pessoa consiga aprender
    a identificar mensagens suspeitas, avaliar senhas e revisar boas práticas de uso seguro da internet.
    """)

    st.success("Use o menu lateral para acessar as ferramentas educativas.")


# -----------------------------
# CHECKLIST DE GOLPES
# -----------------------------
elif pagina == "Checklist de Golpes":
    st.title("🕵️ Checklist de Golpes Digitais")

    st.write("""
    Responda às perguntas abaixo para avaliar se uma mensagem, link ou contato recebido pode ser golpe.
    """)

    perguntas = [
        "A mensagem pede urgência, como 'clique agora', 'sua conta será bloqueada' ou 'última chance'?",
        "O remetente é desconhecido ou parece falso?",
        "O link está estranho, encurtado ou diferente do site oficial?",
        "A mensagem pede senha, código SMS, token ou dados bancários?",
        "A oferta parece boa demais para ser verdade?",
        "Há erros de português, logo distorcido ou aparência pouco profissional?"
    ]

    respostas = []

    for pergunta in perguntas:
        resposta = st.checkbox(pergunta)
        respostas.append(1 if resposta else 0)

    if st.button("Analisar risco"):
        nivel, orientacao = analisar_golpe(respostas)

        if nivel == "Baixo":
            st.markdown(f"""
            <div class="success-card">
                <h3>Risco: {nivel}</h3>
                <p>{orientacao}</p>
            </div>
            """, unsafe_allow_html=True)

        elif nivel == "Médio":
            st.markdown(f"""
            <div class="warning-card">
                <h3>Risco: {nivel}</h3>
                <p>{orientacao}</p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="danger-card">
                <h3>Risco: {nivel}</h3>
                <p>{orientacao}</p>
            </div>
            """, unsafe_allow_html=True)

        st.write("### Recomendações")
        st.write("""
        - Não clique em links suspeitos;
        - Não envie senhas, códigos ou dados bancários;
        - Confirme a informação pelo canal oficial;
        - Desconfie de mensagens com urgência exagerada;
        - Bloqueie e denuncie contatos suspeitos.
        """)


# -----------------------------
# TESTE DE SENHA
# -----------------------------
elif pagina == "Teste de Senha":
    st.title("🔑 Teste Educativo de Senha")

    st.warning("Atenção: não digite sua senha real. Use apenas uma senha de exemplo para fins educativos.")

    senha = st.text_input("Digite uma senha de exemplo:", type="password")

    if senha:
        nivel, pontos, criterios = avaliar_senha(senha)

        st.write(f"### Resultado: {nivel}")
        st.progress(pontos / 5)

        for criterio in criterios:
            st.write(criterio)

        st.write("### Boas práticas")
        st.write("""
        - Use senhas com pelo menos 12 caracteres quando possível;
        - Misture letras maiúsculas, minúsculas, números e símbolos;
        - Não use nome, data de nascimento ou informações pessoais;
        - Não reutilize a mesma senha em vários serviços;
        - Ative autenticação em dois fatores.
        """)


# -----------------------------
# QUIZ
# -----------------------------
elif pagina == "Quiz Educativo":
    st.title("🧠 Quiz de Segurança Digital")

    st.write("Responda às perguntas e veja sua pontuação ao final.")

    pontos = 0

    q1 = st.radio(
        "1. O que é phishing?",
        [
            "Um tipo de antivírus",
            "Uma tentativa de enganar pessoas para roubar dados",
            "Um método seguro de login",
            "Um programa de backup"
        ]
    )

    if q1 == "Uma tentativa de enganar pessoas para roubar dados":
        pontos += 1

    q2 = st.radio(
        "2. Qual é uma boa prática de segurança?",
        [
            "Usar a mesma senha em todos os sites",
            "Compartilhar código SMS com atendente",
            "Ativar autenticação em dois fatores",
            "Clicar em links recebidos de desconhecidos"
        ]
    )

    if q2 == "Ativar autenticação em dois fatores":
        pontos += 1

    q3 = st.radio(
        "3. O que fazer ao receber um link suspeito?",
        [
            "Clicar rapidamente",
            "Enviar para todos os contatos",
            "Ignorar a aparência do link",
            "Verificar o remetente e acessar o site oficial manualmente"
        ]
    )

    if q3 == "Verificar o remetente e acessar o site oficial manualmente":
        pontos += 1

    q4 = st.radio(
        "4. Qual senha é mais segura?",
        [
            "123456",
            "senha123",
            "NomeDataNascimento",
            "F!lme#Casa2026"
        ]
    )

    if q4 == "F!lme#Casa2026":
        pontos += 1

    q5 = st.radio(
        "5. O que nunca deve ser compartilhado por WhatsApp?",
        [
            "Figurinhas",
            "Código de verificação, senha ou token bancário",
            "Mensagem de bom dia",
            "Link de site oficial conferido"
        ]
    )

    if q5 == "Código de verificação, senha ou token bancário":
        pontos += 1

    if st.button("Ver resultado"):
        st.write(f"### Você acertou {pontos} de 5 perguntas.")

        if pontos <= 2:
            st.error("É importante revisar as dicas de segurança digital.")
        elif pontos <= 4:
            st.warning("Bom resultado! Mas ainda há pontos para melhorar.")
        else:
            st.success("Excelente! Você demonstrou boa noção de segurança digital.")


# -----------------------------
# DICAS
# -----------------------------
elif pagina == "Dicas de Segurança":
    st.title("🛡️ Dicas Rápidas de Segurança Digital")

    st.subheader("1. Cuidado com mensagens urgentes")
    st.write("Golpistas costumam usar medo e pressa para fazer a vítima clicar em links ou enviar dados.")

    st.subheader("2. Nunca compartilhe códigos de verificação")
    st.write("Códigos recebidos por SMS, e-mail ou aplicativo são pessoais e não devem ser enviados para ninguém.")

    st.subheader("3. Use autenticação em dois fatores")
    st.write("Esse recurso adiciona uma camada extra de proteção em contas importantes.")

    st.subheader("4. Confira links antes de clicar")
    st.write("Sempre verifique se o endereço do site é oficial. Na dúvida, digite o endereço manualmente no navegador.")

    st.subheader("5. Atualize aplicativos e sistemas")
    st.write("Atualizações corrigem falhas de segurança e ajudam a proteger seus dispositivos.")

    st.subheader("6. Desconfie de promoções exageradas")
    st.write("Ofertas muito abaixo do preço normal podem ser tentativa de golpe.")

    st.subheader("7. Proteja seus dados pessoais")
    st.write("Evite publicar documentos, endereço, telefone e informações sensíveis em redes sociais.")


# -----------------------------
# FEEDBACK
# -----------------------------
elif pagina == "Feedback da Comunidade":
    st.title("📝 Feedback da Comunidade")

    st.write("""
    Este formulário pode ser usado para coletar evidências da participação da comunidade.
    Para um projeto real, você pode substituir essa parte por um Google Forms.
    """)

    nome = st.text_input("Nome ou identificação do participante:")
    perfil = st.selectbox(
        "Perfil:",
        [
            "Aluno",
            "Professor",
            "Familiar",
            "Funcionário",
            "Pequeno comerciante",
            "Morador da comunidade",
            "Outro"
        ]
    )

    avaliacao = st.slider("De 0 a 10, quanto este conteúdo foi útil?", 0, 10, 8)

    aprendeu = st.radio(
        "Você aprendeu algo novo sobre segurança digital?",
        ["Sim", "Parcialmente", "Não"]
    )

    comentario = st.text_area("Comentário ou sugestão:")

    if st.button("Enviar feedback"):
        if nome.strip() == "":
            st.error("Informe ao menos um nome ou identificação.")
        else:
            st.success("Feedback registrado com sucesso!")

            st.write("### Registro gerado")
            st.write(f"**Participante:** {nome}")
            st.write(f"**Perfil:** {perfil}")
            st.write(f"**Avaliação:** {avaliacao}/10")
            st.write(f"**Aprendizado:** {aprendeu}")
            st.write(f"**Comentário:** {comentario}")
            st.write(f"**Data/Hora:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

            st.info("Tire um print desta tela para usar como evidência no relatório.")


# -----------------------------
# RELATÓRIO
# -----------------------------
elif pagina == "Relatório do Projeto":
    st.title("📄 Relatório do Projeto de Extensão")

    st.write("""
    Esta página serve como base para documentar a entrega do projeto.
    Você pode tirar prints dela e anexar no relatório final.
    """)

    st.subheader("Título")
    st.write("Segurança Digital na Prática: prevenção contra golpes virtuais e proteção de dados pessoais.")

    st.subheader("Problema identificado")
    st.write("""
    Parte da comunidade possui dificuldade para identificar golpes digitais, mensagens falsas, links suspeitos
    e riscos relacionados ao compartilhamento de dados pessoais.
    """)

    st.subheader("Solução desenvolvida")
    st.write("""
    Foi desenvolvido um aplicativo web educativo com informações, checklist, teste de senha, quiz e dicas práticas
    sobre segurança digital.
    """)

    st.subheader("Público beneficiado")
    st.write("""
    Comunidade local, incluindo alunos, familiares, pequenos comerciantes, professores, funcionários e demais interessados.
    """)

    st.subheader("Evidências sugeridas")
    st.write("""
    - Print da tela inicial do aplicativo;
    - Print do checklist de golpes;
    - Print do teste de senha;
    - Print do quiz educativo;
    - Print da divulgação do link para a comunidade;
    - Print ou exportação dos feedbacks recebidos;
    - Declaração da instituição, se aplicável;
    - Relatório final descrevendo os resultados.
    """)

    st.subheader("Conclusão")
    st.write("""
    O projeto contribui para a conscientização da comunidade sobre riscos digitais e apresenta orientações práticas
    de prevenção, aproximando os conhecimentos do curso de Segurança da Informação das necessidades reais da sociedade.
    """)