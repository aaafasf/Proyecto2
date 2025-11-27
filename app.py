from flask import Flask, request, redirect, url_for, render_template_string, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "clave_ultra_secreta_123"

PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Panel Neon Flask</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap" rel="stylesheet">

<style>
:root{
    --bg: #0a0f1f;
    --panel: rgba(255,255,255,0.04);
    --neon: #00eaff;
    --neon2: #14f7a3;
    --text: #d9e6ff;
    --muted: #7b8ca6;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins', sans-serif;
}

body{
    background:radial-gradient(circle at 20% 20%, rgba(0,234,255,0.14), transparent 60%),
               linear-gradient(180deg, #04070f, #0a0f1f);
    color:var(--text);
    display:flex;
    height:100vh;
    overflow:hidden;
}

/* ---- Sidebar ---- */
.sidebar{
    width:240px;
    background:rgba(255,255,255,0.03);
    border-right:1px solid rgba(255,255,255,0.06);
    padding:24px;
    display:flex;
    flex-direction:column;
    gap:26px;
    backdrop-filter:blur(16px);
}

.logo{
    display:flex;
    align-items:center;
    gap:10px;
    font-size:20px;
    font-weight:800;
    color:var(--neon);
    text-shadow:0 0 8px var(--neon);
}

.logo span{
    width:32px;
    height:32px;
    background:var(--neon);
    color:black;
    border-radius:6px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:800;
    filter:drop-shadow(0 0 8px var(--neon));
}

.nav a{
    color:var(--muted);
    text-decoration:none;
    padding:10px 0;
    display:block;
    transition:0.2s;
}

.nav a:hover{
    color:var(--neon2);
    text-shadow:0 0 8px var(--neon2);
}

/* ---- Main ---- */
.main{
    flex:1;
    padding:40px;
    overflow-y:auto;
}

h1{
    font-size:32px;
    margin-bottom:8px;
}
.lead{
    color:var(--muted);
    margin-bottom:24px;
}

/* ---- Grid ---- */
.grid{
    display:grid;
    grid-template-columns: 1fr 360px;
    gap:28px;
}

/* ---- Cards ---- */
.card{
    background:var(--panel);
    border:1px solid rgba(255,255,255,0.05);
    padding:22px;
    border-radius:14px;
    backdrop-filter:blur(16px);
    box-shadow:0 4px 18px rgba(0,0,0,0.4);
}

.stat{
    background:rgba(0,234,255,0.06);
    border:1px solid rgba(0,234,255,0.12);
    padding:16px;
    border-radius:12px;
    text-align:center;
}
.stat span{
    display:block;
    font-size:32px;
    margin-top:6px;
    color:var(--neon);
    text-shadow:0 0 8px var(--neon);
}

/* ---- Form ---- */
label{
    font-size:14px;
    color:var(--muted);
    margin-bottom:4px;
    display:block;
}
input, textarea{
    width:100%;
    padding:10px;
    border-radius:8px;
    border:1px solid rgba(255,255,255,0.04);
    background:rgba(255,255,255,0.03);
    color:var(--text);
    margin-bottom:12px;
    outline:none;
    font-size:14px;
}
textarea{
    min-height:120px;
}

.btn{
    background:linear-gradient(90deg, var(--neon), var(--neon2));
    border:none;
    padding:12px 16px;
    border-radius:10px;
    color:black;
    cursor:pointer;
    font-weight:600;
    width:100%;
    box-shadow:0 0 12px rgba(0,234,255,0.4);
}

.flash{
    background:rgba(0,234,255,0.12);
    border:1px solid rgba(0,234,255,0.25);
    color:var(--neon);
    padding:10px 12px;
    border-radius:8px;
    margin-bottom:12px;
    text-shadow:0 0 4px var(--neon);
}

@media(max-width:900px){
    .grid{
        grid-template-columns:1fr;
    }
}
</style>
</head>

<body>

<div class="sidebar">
    <div class="logo"><span>N</span> NeonPanel</div>

    <div class="nav">
        <a href="/">Dashboard</a>
        <a href="#support">Soporte</a>
        <a href="#">Ajustes</a>
        <a href="#">Estadísticas</a>
    </div>
</div>

<div class="main">

    <h1>Dashboard principal</h1>
    <p class="lead">Panel estilo neon con Glass UI integrado. Todo embebido en Flask sin archivos externos.</p>

    <div class="grid">

        <div class="card">
            <h3>Estadísticas del sistema</h3>
            <div style="display:flex; gap:16px; margin-top:14px;">
                <div class="stat">
                    Usuarios
                    <span>124</span>
                </div>
                <div class="stat">
                    Servicios
                    <span>12</span>
                </div>
                <div class="stat">
                    Alertas
                    <span>3</span>
                </div>
            </div>
        </div>

        <div class="card" id="support">
            <h3>Soporte técnico</h3>

            {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="flash">{{ messages[0] }}</div>
            {% endif %}
            {% endwith %}

            <form method="post" action="{{ url_for('support') }}">
                <label>Nombre</label>
                <input type="text" name="name" required placeholder="Tu nombre">

                <label>Correo</label>
                <input type="email" name="email" required placeholder="correo@ejemplo.com">

                <label>Descripción del problema</label>
                <textarea name="message" placeholder="Cuéntanos qué sucede..."></textarea>

                <button class="btn">Enviar Ticket</button>
            </form>
        </div>

    </div>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(PAGE)

@app.route("/support", methods=["POST"])
def support():
    name = escape(request.form.get("name", "").strip())
    email = escape(request.form.get("email", "").strip())
    message = escape(request.form.get("message", "").strip())

    flash(f"Ticket recibido: {name}. Te contactaremos al correo: {email}")
    return redirect(url_for("index") + "#support")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1001, debug=False)