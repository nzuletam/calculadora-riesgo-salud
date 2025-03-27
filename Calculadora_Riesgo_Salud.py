from flask import Flask, render_template, request, jsonify

def calcular_imc(peso, altura):
    if peso > 0 and altura > 0:
        return round(peso / (altura ** 2), 2)
    return None

def determinar_nivel_riesgo(imc, factores_riesgo):
    riesgo = "Bajo"
    
    if imc >= 30:
        riesgo = "Alto"
    elif imc >= 25:
        riesgo = "Moderado"
    
    if len(factores_riesgo) > 2:
        riesgo = "Alto"
    elif len(factores_riesgo) > 0:
        riesgo = "Moderado"
    
    return riesgo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    peso = float(data.get('peso', 0))
    altura = float(data.get('altura', 0))
    factores_riesgo = data.get('factores_riesgo', [])
    
    imc = calcular_imc(peso, altura)
    nivel_riesgo = determinar_nivel_riesgo(imc, factores_riesgo) if imc else "Datos inválidos"
    
    return jsonify({"imc": imc, "nivel_riesgo": nivel_riesgo})

if __name__ == '__main__':
    app.run(debug=True)
