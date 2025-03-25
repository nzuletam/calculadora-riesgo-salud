import React, { useState } from "react";

const calcularIMC = (peso, altura) => {
  if (peso > 0 && altura > 0) {
    const imc = peso / (altura * altura);
    return imc.toFixed(2);
  }
  return "";
};

const determinarNivelRiesgo = (imc, factoresRiesgo) => {
  let riesgo = "Bajo";
  
  if (imc >= 30) {
    riesgo = "Alto";
  } else if (imc >= 25) {
    riesgo = "Moderado";
  }
  
  if (factoresRiesgo.length > 2) {
    riesgo = "Alto";
  } else if (factoresRiesgo.length > 0) {
    riesgo = "Moderado";
  }

  return riesgo;
};

export default function FormularioRiesgoSalud() {
  const [peso, setPeso] = useState("");
  const [altura, setAltura] = useState("");
  const [factoresRiesgo, setFactoresRiesgo] = useState([]);

  const imc = calcularIMC(parseFloat(peso), parseFloat(altura));
  const nivelRiesgo = determinarNivelRiesgo(imc, factoresRiesgo);

  const toggleFactorRiesgo = (factor) => {
    setFactoresRiesgo((prev) =>
      prev.includes(factor)
        ? prev.filter((item) => item !== factor)
        : [...prev, factor]
    );
  };

  return (
    <div className="p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-xl font-bold mb-4">Evaluación de Riesgo en Salud</h2>
      <label className="block mb-2">Peso (kg):</label>
      <input
        type="number"
        className="w-full p-2 border rounded mb-4"
        value={peso}
        onChange={(e) => setPeso(e.target.value)}
        placeholder="Ingrese su peso"
      />

      <label className="block mb-2">Altura (m):</label>
      <input
        type="number"
        className="w-full p-2 border rounded mb-4"
        value={altura}
        onChange={(e) => setAltura(e.target.value)}
        placeholder="Ingrese su altura"
      />

      {imc && (
        <p className="mt-2 font-semibold">
          IMC: {imc} ({imc < 18.5 ? "Bajo peso" : imc < 25 ? "Normal" : imc < 30 ? "Sobrepeso" : "Obesidad"})
        </p>
      )}

      <h3 className="text-lg font-semibold mt-4">Factores de Riesgo</h3>
      {[
        "Fumador",
        "Hipertensión",
        "Diabetes",
        "Antecedentes familiares de enfermedad cardiovascular",
        "Sedentarismo",
        "Colesterol alto",
        "Enfermedad renal crónica",
        "Enfermedad pulmonar obstructiva crónica (EPOC)",
        "Artritis reumatoide",
        "Enfermedad hepática crónica",
        "Insuficiencia cardíaca"
      ].map((factor) => (
        <div key={factor} className="mb-2">
          <label className="inline-flex items-center">
            <input
              type="checkbox"
              checked={factoresRiesgo.includes(factor)}
              onChange={() => toggleFactorRiesgo(factor)}
            />
            <span className="ml-2">{factor}</span>
          </label>
        </div>
      ))}

      <p className="mt-4 font-bold text-lg">Nivel de Riesgo: {nivelRiesgo}</p>

      <p className="text-sm text-gray-600 mt-2">
        * El cálculo del riesgo en salud se basa en criterios de la Organización Mundial de la Salud (OMS) y guías clínicas establecidas.
      </p>
    </div>
  );
}
