from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    if peso > 0 and altura > 0:
        return round(peso / (altura ** 2), 2)
    return None

def clasificar_imc(imc):
    """Clasifica el IMC en una categoría de peso."""
    if imc is None:
        return "Dato no válido"
    elif imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def determinar_nivel_riesgo(imc, factores_riesgo):
    """Determina el nivel de riesgo basado en el IMC y factores de riesgo."""
    if imc is None:
        return "Error"

    riesgo = "Bajo"
    if imc >= 30 or len(factores_riesgo) > 2:
        riesgo = "Alto"
    elif imc >= 25 or len(factores_riesgo) > 0:
        riesgo = "Moderado"

    return riesgo

@app.route("/", methods=["GET", "POST"])
def formulario():
    imc = None
    nivel_riesgo = ""
    clasificacion_imc = ""
    peso = altura = ""
    factores_seleccionados = []

    factores_riesgo = [
        "Fumador", "Hipertensión", "Diabetes", "Antecedentes familiares de enfermedad cardiovascular",
        "Sedentarismo", "Colesterol alto", "Enfermedad renal crónica", "EPOC",
        "Artritis reumatoide", "Enfermedad hepática crónica", "Insuficiencia cardíaca"
    ]

    if request.method == "POST":
        try:
            peso = float(request.form.get("peso", 0))
            altura = float(request.form.get("altura", 0))
            factores_seleccionados = request.form.getlist("factores_riesgo")

            imc = calcular_imc(peso, altura)
            clasificacion_imc = clasificar_imc(imc)
            nivel_riesgo = determinar_nivel_riesgo(imc, factores_seleccionados)
        except ValueError:
            nivel_riesgo = "Error en los datos"

    return render_template("index.html", imc=imc, clasificacion_imc=clasificacion_imc,
                           nivel_riesgo=nivel_riesgo, factores_riesgo=factores_riesgo, 
                           factores_seleccionados=factores_seleccionados, peso=peso, altura=altura)

if __name__ == "__main__":
    app.run(debug=True)
