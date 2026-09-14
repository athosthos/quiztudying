import streamlit as st
import json
import os


# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Quiz",
    page_icon="🧠",
    layout="centered"
)


# ==========================================
# CONFIGURAÇÃO DA PASTA DOS JSONS
# ==========================================

PASTA_QUESTOES = "questoes"


# ==========================================
# FUNÇÃO PARA ENCONTRAR OS JSONS
# ==========================================

def carregar_quizzes():

    arquivos = []

    if os.path.exists(PASTA_QUESTOES):

        for arquivo in os.listdir(PASTA_QUESTOES):

            if arquivo.endswith(".json"):
                arquivos.append(arquivo)

    return sorted(arquivos)


# ==========================================
# FUNÇÃO PARA CARREGAR UM JSON
# ==========================================

def carregar_questoes(nome_arquivo):

    caminho = os.path.join(
        PASTA_QUESTOES,
        nome_arquivo
    )

    with open(caminho, "r", encoding="utf-8") as arquivo:

        return json.load(arquivo)


# ==========================================
# FUNÇÃO PARA VOLTAR PARA HOME
# ==========================================

def voltar_home():

    st.session_state.tela = "home"

    st.session_state.quiz_atual = None

    st.session_state.questao_atual = 0

    st.session_state.respostas = []

    st.session_state.respondida = False

    st.session_state.questoes = []

    st.rerun()


# ==========================================
# INICIALIZAÇÃO DO SESSION STATE
# ==========================================

if "tela" not in st.session_state:
    st.session_state.tela = "home"

if "quiz_atual" not in st.session_state:
    st.session_state.quiz_atual = None

if "questao_atual" not in st.session_state:
    st.session_state.questao_atual = 0

if "respostas" not in st.session_state:
    st.session_state.respostas = []

if "respondida" not in st.session_state:
    st.session_state.respondida = False

if "questoes" not in st.session_state:
    st.session_state.questoes = []


# ==========================================
# HOME
# ==========================================

if st.session_state.tela == "home":

    st.title("🧠 Quiz")

    st.write(
        "Escolha um assunto para começar:"
    )

    st.divider()

    quizzes = carregar_quizzes()


    # --------------------------------------
    # VERIFICAR SE EXISTEM JSONS
    # --------------------------------------

    if not quizzes:

        st.warning(
            "Nenhum arquivo JSON foi encontrado."
        )

        st.info(
            "Coloque seus arquivos .json dentro da pasta 'questoes'."
        )


    # --------------------------------------
    # MOSTRAR OS QUIZZES
    # --------------------------------------

    else:

        for arquivo in quizzes:

            # Remove .json
            nome = arquivo.replace(".json", "")

            # Deixa o nome mais bonito
            nome_exibicao = nome.replace("_", " ").title()


            if st.button(
                f"📚 {nome_exibicao}",
                use_container_width=True
            ):

                # Carrega as questões
                questoes = carregar_questoes(arquivo)

                # Guarda informações do quiz
                st.session_state.quiz_atual = nome_exibicao

                st.session_state.questoes = questoes

                st.session_state.questao_atual = 0

                st.session_state.respostas = []

                st.session_state.respondida = False

                st.session_state.tela = "quiz"

                st.rerun()


# ==========================================
# QUIZ
# ==========================================

elif st.session_state.tela == "quiz":

    questoes = st.session_state.questoes

    indice = st.session_state.questao_atual

    total = len(questoes)

    questao = questoes[indice]


    # ======================================
    # CABEÇALHO
    # ======================================

    st.title(
        f"🧠 {st.session_state.quiz_atual}"
    )

    st.write(
        f"### Questão {indice + 1} de {total}"
    )

    st.progress(
        (indice + 1) / total
    )

    st.divider()


    # ======================================
    # BOTÃO VOLTAR PARA HOME
    # ======================================

    if st.button("🏠 Voltar para Home"):

        voltar_home()


    st.divider()


    # ======================================
    # PERGUNTA
    # ======================================

    st.subheader(
        questao["question"]
    )


    resposta = st.radio(
        "Selecione uma alternativa:",
        questao["options"],
        key=f"resposta_{indice}"
    )


    # ======================================
    # RESPONDER
    # ======================================

    if not st.session_state.respondida:

        if st.button(
            "Responder",
            use_container_width=True
        ):

            indice_resposta = (
                questao["options"].index(resposta)
            )

            correta = (
                indice_resposta == questao["correct"]
            )


            # Guarda resposta
            st.session_state.respostas.append({

                "resposta_usuario": indice_resposta,

                "correta": correta

            })


            # Marca como respondida
            st.session_state.respondida = True

            st.rerun()


    # ======================================
    # RESULTADO DA QUESTÃO
    # ======================================

    else:

        ultima_resposta = (
            st.session_state.respostas[-1]
        )


        # ----------------------------------
        # RESPOSTA CORRETA
        # ----------------------------------

        if ultima_resposta["correta"]:

            st.success(
                "✅ Resposta correta!"
            )


        # ----------------------------------
        # RESPOSTA ERRADA
        # ----------------------------------

        else:

            st.error(
                "❌ Resposta incorreta!"
            )

            st.write(
                f"**Resposta correta:** "
                f"{questao['options'][questao['correct']]}"
            )


        # ----------------------------------
        # EXPLICAÇÃO
        # ----------------------------------

        st.info(
            f"**Explicação:** "
            f"{questao['explanation']}"
        )


        st.divider()


        # ==================================
        # PRÓXIMA QUESTÃO
        # ==================================

        if indice + 1 < total:

            if st.button(
                "➡️ Próxima questão",
                use_container_width=True
            ):

                st.session_state.questao_atual += 1

                st.session_state.respondida = False

                st.rerun()


        # ==================================
        # FINAL DO QUIZ
        # ==================================

        else:

            if st.button(
                "🏆 Ver resultado",
                use_container_width=True
            ):

                st.session_state.tela = "resultado"

                st.rerun()


# ==========================================
# RESULTADO
# ==========================================

elif st.session_state.tela == "resultado":

    questoes = st.session_state.questoes

    total = len(questoes)


    # ======================================
    # CALCULAR ACERTOS
    # ======================================

    acertos = sum(
        resposta["correta"]
        for resposta in st.session_state.respostas
    )


    percentual = (
        acertos / total
    ) * 100


    # ======================================
    # TÍTULO
    # ======================================

    st.title("🎉 Quiz finalizado!")

    st.subheader(
        st.session_state.quiz_atual
    )


    # ======================================
    # RESULTADO
    # ======================================

    st.metric(
        "Resultado",
        f"{acertos}/{total}"
    )


    st.write(
        f"Você acertou **{percentual:.1f}%** das questões."
    )


    # ======================================
    # MENSAGEM
    # ======================================

    if percentual >= 90:

        st.success(
            "🏆 Excelente! Você domina muito bem o conteúdo."
        )

    elif percentual >= 70:

        st.success(
            "👏 Muito bom! Você tem um bom domínio do conteúdo."
        )

    elif percentual >= 50:

        st.warning(
            "📚 Bom começo! Vale revisar alguns assuntos."
        )

    else:

        st.error(
            "📖 Vale a pena revisar o conteúdo e tentar novamente."
        )


    st.divider()


    # ======================================
    # BOTÕES
    # ======================================

    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "🔄 Refazer quiz",
            use_container_width=True
        ):

            st.session_state.questao_atual = 0

            st.session_state.respostas = []

            st.session_state.respondida = False

            st.session_state.tela = "quiz"

            st.rerun()


    with col2:

        if st.button(
            "🏠 Voltar para Home",
            use_container_width=True
        ):

            voltar_home()


    st.divider()


    # ======================================
    # REVISÃO
    # ======================================

    st.subheader(
        "📋 Revisão das questões"
    )


    for i, resposta in enumerate(
        st.session_state.respostas
    ):

        questao = questoes[i]


        st.write(
            f"### Questão {i + 1}"
        )


        st.write(
            questao["question"]
        )


        st.write(
            f"**Sua resposta:** "
            f"{questao['options'][resposta['resposta_usuario']]}"
        )


        st.write(
            f"**Resposta correta:** "
            f"{questao['options'][questao['correct']]}"
        )


        st.info(
            questao["explanation"]
        )


        st.divider()