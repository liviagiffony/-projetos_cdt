from flask import Flask, request, redirect, url_for, render_template_string, session

app = Flask(__name__)
app.secret_key = "power_up_sophia"


# =========================================================
# BASE DE EXERCÍCIOS
# =========================================================

exercicios = {
    "gluteos": [
        "Agachamento",
        "Elevação de quadril",
        "Abdução de quadril",
        "Extensão de quadril"
    ],

    "pernas": [
        "Agachamento",
        "Leg press",
        "Cadeira extensora",
        "Mesa flexora"
    ],

    "costas": [
        "Puxada frontal",
        "Remada baixa",
        "Remada unilateral",
        "Pulldown"
    ],

    "bracos": [
        "Rosca direta",
        "Tríceps na polia",
        "Elevação lateral",
        "Rosca martelo"
    ],

    "corpo_todo": [
        "Agachamento",
        "Remada baixa",
        "Elevação de quadril",
        "Elevação lateral"
    ]
}


# =========================================================
# LOGIN
# =========================================================

LOGIN = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Power Up - Login</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #eee7ff, #ffffff);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.login-box {
    background: white;
    width: 390px;
    padding: 45px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 10px 35px rgba(0,0,0,0.12);
}

.logo {
    color: #7046d8;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 8px;
}

.subtitulo {
    color: #777;
    margin-bottom: 30px;
}

input {
    width: 100%;
    padding: 14px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 12px;
    font-size: 15px;
}

button {
    width: 100%;
    padding: 14px;
    border: none;
    border-radius: 12px;
    background: #7046d8;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

button:hover {
    background: #5d35c1;
}
</style>
</head>

<body>

<div class="login-box">

    <div class="logo">POWER UP</div>

    <div class="subtitulo">
        Seu treino personalizado começa aqui 💜
    </div>

    <form method="POST">

        <input
            type="text"
            name="nome"
            placeholder="Digite seu nome"
            required
        >

        <input
            type="email"
            name="email"
            placeholder="Digite seu e-mail"
            required
        >

        <button type="submit">
            Entrar
        </button>

    </form>

</div>

</body>
</html>
"""


# =========================================================
# PÁGINA INICIAL
# =========================================================

HOME = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
<meta charset="UTF-8">
<title>Power Up</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f5ff;
    color: #292333;
}

header {
    height: 75px;
    background: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 60px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
}

.logo {
    color: #7046d8;
    font-size: 27px;
    font-weight: bold;
}

nav a {
    color: #555;
    text-decoration: none;
    margin-left: 25px;
}

.principal {
    text-align: center;
    padding: 80px 20px 50px;
}

.principal h1 {
    font-size: 43px;
    margin-bottom: 15px;
    color: #7046d8;
}

.principal p {
    color: #666;
    font-size: 18px;
}

.botao {
    display: inline-block;
    margin-top: 25px;
    padding: 17px 40px;
    background: #7046d8;
    color: white;
    text-decoration: none;
    border-radius: 13px;
    font-weight: bold;
    font-size: 17px;
}

.botao:hover {
    background: #5d35c1;
}

.cards {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 50px;
    flex-wrap: wrap;
}

.card {
    background: white;
    width: 230px;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.07);
}

.card h2 {
    color: #7046d8;
    font-size: 20px;
}

/* Wendy */

.wendy {
    position: fixed;
    right: 25px;
    bottom: 25px;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background: #7046d8;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 38px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}

.wendy-mensagem {
    position: fixed;
    right: 25px;
    bottom: 115px;
    background: white;
    padding: 14px 18px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.12);
    font-size: 14px;
}

</style>
</head>

<body>

<header>

    <div class="logo">POWER UP</div>

    <nav>
        <a href="/home">Início</a>
        <a href="/treino">Meu treino</a>
    </nav>

</header>


<section class="principal">

    <h1>Olá, {{ nome }}! 👋</h1>

    <p>
        Crie uma sugestão de treino de acordo com seus
        objetivos e sua disponibilidade.
    </p>

    <a class="botao" href="/treino">
        🏋️ Montar meu treino
    </a>


    <div class="cards">

        <div class="card">
            <h2>🎯 Seus objetivos</h2>
            <p>
                Informe o que você deseja alcançar
                com seus treinos.
            </p>
        </div>

        <div class="card">
            <h2>⏱️ Seu tempo</h2>
            <p>
                Escolha quanto tempo você possui
                para cada treino.
            </p>
        </div>

        <div class="card">
            <h2>💪 Seu treino</h2>
            <p>
                Receba uma sugestão criada
                automaticamente.
            </p>
        </div>

    </div>

</section>


<div class="wendy-mensagem">
    🤖 Oi! Vamos montar seu treino?
</div>

<div class="wendy">
    🤖
</div>

</body>
</html>
"""


# =========================================================
# FORMULÁRIO DO TREINO
# =========================================================

TREINO = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
<meta charset="UTF-8">
<title>Montar treino - Power Up</title>

<style>

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f5ff;
}

header {
    background: white;
    padding: 22px 60px;
    color: #7046d8;
    font-size: 27px;
    font-weight: bold;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
}

.formulario {
    background: white;
    width: 550px;
    max-width: 90%;
    margin: 45px auto;
    padding: 35px;
    border-radius: 22px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

h1 {
    color: #7046d8;
}

.descricao {
    color: #666;
}

label {
    display: block;
    margin-top: 22px;
    margin-bottom: 7px;
    font-weight: bold;
}

select {
    width: 100%;
    padding: 13px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background: white;
    font-size: 15px;
}

button {
    width: 100%;
    margin-top: 30px;
    padding: 15px;
    border: none;
    border-radius: 12px;
    background: #7046d8;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

</style>
</head>

<body>

<header>
    POWER UP
</header>


<div class="formulario">

    <h1>Vamos montar seu treino 🏋️</h1>

    <p class="descricao">
        Responda algumas perguntas para que o sistema
        possa gerar uma sugestão de treino.
    </p>


    <form method="POST">

        <label>Qual é o seu objetivo?</label>

        <select name="objetivo" required>

            <option value="">Selecione</option>
            <option value="massa">Ganhar massa muscular</option>
            <option value="forca">Aumentar força</option>
            <option value="condicionamento">
                Melhorar condicionamento
            </option>
            <option value="saude">
                Melhorar saúde e disposição
            </option>

        </select>


        <label>Qual grupo muscular você quer priorizar?</label>

        <select name="grupo" required>

            <option value="">Selecione</option>
            <option value="gluteos">Glúteos</option>
            <option value="pernas">Pernas</option>
            <option value="costas">Costas</option>
            <option value="bracos">Braços</option>
            <option value="corpo_todo">Corpo todo</option>

        </select>


        <label>Qual é o seu nível de experiência?</label>

        <select name="experiencia" required>

            <option value="">Selecione</option>
            <option value="iniciante">Iniciante</option>
            <option value="intermediario">Intermediário</option>
            <option value="avancado">Avançado</option>

        </select>


        <label>Quanto tempo você tem por treino?</label>

        <select name="tempo" required>

            <option value="">Selecione</option>
            <option value="30">30 minutos</option>
            <option value="60">1 hora</option>
            <option value="90">1 hora e 30 minutos</option>

        </select>


        <label>Quantos dias por semana você pode treinar?</label>

        <select name="dias" required>

            <option value="">Selecione</option>
            <option value="2">2 dias</option>
            <option value="3">3 dias</option>
            <option value="4">4 dias</option>
            <option value="5">5 dias</option>

        </select>


        <button type="submit">
            🤖 Gerar meu treino
        </button>

    </form>

</div>

</body>
</html>
"""


# =========================================================
# RESULTADO DO TREINO
# =========================================================

RESULTADO = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
<meta charset="UTF-8">
<title>Seu treino - Power Up</title>

<style>

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f5ff;
}

.resultado {
    background: white;
    width: 650px;
    max-width: 90%;
    margin: 50px auto;
    padding: 40px;
    border-radius: 22px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

h1 {
    color: #7046d8;
}

.info {
    background: #f0ebff;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
}

.exercicio {
    background: #f7f5ff;
    padding: 17px;
    margin: 10px 0;
    border-radius: 12px;
    border-left: 5px solid #7046d8;
}

.voltar {
    display: inline-block;
    margin-top: 25px;
    padding: 13px 25px;
    background: #7046d8;
    color: white;
    text-decoration: none;
    border-radius: 10px;
}

.aviso {
    margin-top: 25px;
    color: #777;
    font-size: 13px;
}

</style>
</head>

<body>

<div class="resultado">

    <h1>Seu treino está pronto! 🎉</h1>

    <p>
        Com base nas informações fornecidas,
        o Power Up gerou esta sugestão:
    </p>


    <div class="info">
        <strong>Objetivo:</strong> {{ objetivo }}
    </div>

    <div class="info">
        <strong>Tempo:</strong> {{ tempo }}
    </div>

    <div class="info">
        <strong>Frequência:</strong> {{ dias }} dias por semana
    </div>


    <h2>🏋️ Exercícios sugeridos</h2>


    {% for exercicio in treino %}

        <div class="exercicio">
            💪 {{ exercicio }}
        </div>

    {% endfor %}


    <div class="aviso">
        Esta é uma sugestão educativa gerada automaticamente
        pelo sistema e não substitui a orientação de um
        profissional de Educação Física.
    </div>


    <a class="voltar" href="/treino">
        Criar outro treino
    </a>

</div>

</body>
</html>
"""


# =========================================================
# ROTAS DO SITE
# =========================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nome = request.form["nome"]

        session["nome"] = nome

        return redirect(url_for("home"))

    return render_template_string(LOGIN)


@app.route("/home")
def home():

    nome = session.get("nome", "Usuário")

    return render_template_string(
        HOME,
        nome=nome
    )


@app.route("/treino", methods=["GET", "POST"])
def treino():

    if request.method == "POST":

        objetivo = request.form["objetivo"]
        grupo = request.form["grupo"]
        experiencia = request.form["experiencia"]
        tempo = request.form["tempo"]
        dias = request.form["dias"]


        # =================================================
        # AUTOMAÇÃO
        # =================================================

        treino_gerado = exercicios.get(
            grupo,
            exercicios["corpo_todo"]
        )

        # Se tiver apenas 30 minutos,
        # reduz a quantidade de exercícios.

        if tempo == "30":
            treino_gerado = treino_gerado[:3]

        # Para usuários com mais experiência,
        # mantém até 4 exercícios.

        elif experiencia in ["intermediario", "avancado"]:
            treino_gerado = treino_gerado[:4]

        else:
            treino_gerado = treino_gerado[:3]


        nomes_objetivos = {
            "massa": "Ganhar massa muscular",
            "forca": "Aumentar força",
            "condicionamento": "Melhorar condicionamento",
            "saude": "Melhorar saúde e disposição"
        }

        objetivo_formatado = nomes_objetivos.get(
            objetivo,
            objetivo
        )


        return render_template_string(
            RESULTADO,
            treino=treino_gerado,
            objetivo=objetivo_formatado,
            tempo=tempo + " minutos",
            dias=dias
        )


    return render_template_string(TREINO)


# =========================================================
# INICIAR O SITE
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)