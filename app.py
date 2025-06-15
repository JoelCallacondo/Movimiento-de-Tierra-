from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    tipo = data["tipo"]
    resultado = None

    try:
        if tipo == "RESPUESTA1":
            largo_banco = float(data["largo_banco"])
            ancho_banco = float(data["ancho_banco"])
            densidad = float(data["densidad"])
            altura_banco = (largo_banco - 46.5) * (2/3)
            resultado = altura_banco * ancho_banco * densidad * largo_banco

        elif tipo == "RESPUESTA2":
            densidad_explosivo = float(data["densidad_explosivo"])
            diametro_pozo = float(data["diametro_pozo"])
            resultado = densidad_explosivo * (diametro_pozo ** 2) * 0.507

        elif tipo == "RESPUESTA3":
            altura = float(data["altura"])
            pasadura = float(data["pasadura"])
            taco = float(data["taco"])
            resultado = altura + pasadura - taco

        elif tipo == "RESPUESTA4":
            tonelaje = float(data["tonelaje"])
            altura_carga = float(data["altura_carga"])
            resultado = tonelaje * altura_carga

        return jsonify({
            "resultado": round(resultado, 2),
            "altura_banco": round((float(data["largo_banco"]) - 46.5) * (2/3), 2) if tipo == "RESPUESTA1" else None
        })

    except ValueError:
        return jsonify({"error": "Datos inválidos"}), 400

if __name__ == "__main__":
    app.run(debug=True)