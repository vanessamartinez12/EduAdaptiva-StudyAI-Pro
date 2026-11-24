console.log("script.js SI cargó ✅");

let nombre = "";
let materia = "quimica";
let indice = 0;
let puntos = 0;
let aciertos = 0;

const QUIZ = {
  quimica: [
    { q: "¿Qué es la masa molar?", op: ["Lo que pesa 1 mol en gramos", "El peso de un átomo", "La velocidad"], correcta: 0 },
    { q: "¿Cuánto pesa 1 mol de NaCl?", op: ["58.5 g", "10 g", "100 g"], correcta: 0 },
    { q: "Si tienes 2 moles de NaCl, ¿cuántos gramos son?", op: ["117 g", "58.5 g", "20 g"], correcta: 0 }
  ],
  mate: [
    { q: "¿Cuál es la derivada de x²?", op: ["2x", "x", "x³"], correcta: 0 },
    { q: "¿Cuánto es el límite de x+1 cuando x->2?", op: ["3", "2", "1"], correcta: 0 },
    { q: "¿Derivada de 5x?", op: ["5", "x", "0"], correcta: 0 }
  ],
  ingles: [
    { q: "¿Cómo se dice 'Yo soy'?", op: ["I am", "I is", "I are"], correcta: 0 },
    { q: "¿Cómo se dice 'Él es'?", op: ["He is", "He are", "He am"], correcta: 0 },
    { q: "¿Cómo se dice 'Ellos son'?", op: ["They are", "They is", "They am"], correcta: 0 }
  ],
  fisica: [
    { q: "¿Fórmula de velocidad?", op: ["distancia / tiempo", "tiempo / distancia", "masa x tiempo"], correcta: 0 },
    { q: "100m en 10s, ¿velocidad?", op: ["10 m/s", "100 m/s", "1 m/s"], correcta: 0 },
    { q: "¿Unidad de velocidad?", op: ["m/s", "kg", "litros"], correcta: 0 }
  ],
  biologia: [
    { q: "¿Qué es una célula?", op: ["Unidad básica de la vida", "Un virus", "Un mineral"], correcta: 0 },
    { q: "¿Dónde está el ADN?", op: ["En el núcleo", "En la piel", "En la sangre"], correcta: 0 },
    { q: "¿Qué hace la mitocondria?", op: ["Da energía", "Da color", "Da forma"], correcta: 0 }
  ],
  historia: [
    { q: "¿En qué año fue la Independencia de México?", op: ["1810", "1910", "1820"], correcta: 0 },
    { q: "¿Quién fue Miguel Hidalgo?", op: ["Padre de la Independencia", "Un presidente de USA", "Un científico"], correcta: 0 },
    { q: "¿Qué se celebra el 16 de septiembre?", op: ["Inicio de la Independencia", "Fin de la guerra", "Navidad"], correcta: 0 }
  ]
};

function mostrar(id){ document.getElementById(id).classList.remove("oculto"); }
function ocultar(id){ document.getElementById(id).classList.add("oculto"); }

function empezarQuiz(){
  console.log("Botón Empezar presionado");
  nombre = document.getElementById("nombre").value.trim();
  materia = document.getElementById("materia").value;
  if(!nombre){ alert("Escribe tu nombre primero 🙏"); return; }
  if(!QUIZ[materia]){ alert("Esa materia ya no existe, elige otra"); return; }
  indice = 0; puntos = 0; aciertos = 0;
  ocultar("p1"); mostrar("p2"); ocultar("p3"); ocultar("p4");
  mostrarPregunta();
}

function mostrarPregunta(){
  const lista = QUIZ[materia];
  const actual = lista[indice];
  document.getElementById("contador").textContent = `Pregunta ${indice+1} de ${lista.length}`;
  document.getElementById("puntos").textContent = `⭐ ${puntos} pts`;
  document.getElementById("pregunta-quiz").textContent = actual.q;
  document.getElementById("barra").style.width = `${(indice/lista.length)*100}%`;
  const cont = document.getElementById("opciones");
  cont.innerHTML = "";
  actual.op.forEach((texto, i) => {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "opcion";
    b.textContent = texto;
    b.addEventListener("click", () => responder(i));
    cont.appendChild(b);
  });
}

function responder(i){
  const lista = QUIZ[materia];
  if(i === lista[indice].correcta){ puntos += 100; aciertos++; }
  indice++;
  if(indice < lista.length){ mostrarPregunta(); }
  else { mostrarResultado(); }
}

function mostrarResultado(){
  ocultar("p2"); mostrar("p3");
  const total = QUIZ[materia].length;
  const porc = Math.round((aciertos/total)*100);
  document.getElementById("titulo-resultado").textContent = `¡Listo, ${nombre}! 🎉`;
  document.getElementById("resultado-texto").innerHTML = `<p style="font-size:18px">Sacaste <b>${aciertos} de ${total}</b></p><p style="color:#7c3aed;font-weight:700;margin-top:6px">${porc}% - ${porc>=70 ? "¡Ya le agarraste la onda!" : porc>=40 ? "Vas bien, te falta un empujoncito" : "Vamos desde cero, sin estrés"}</p><p style="margin-top:6px">Puntos: ⭐ ${puntos}</p>`;
  document.getElementById("barra-final").style.width = porc + "%";
}

function verPlan(){
  ocultar("p3"); mostrar("p4");
  const total = QUIZ[materia].length;
  const porc = Math.round((aciertos/total)*100);
  const nombreMateria = document.getElementById("materia").selectedOptions[0].text;
  let consejo = porc >= 70 ? "Ya dominas lo básico, ahora practicamos con ejemplos difíciles." : porc >= 40 ? "Vas a la mitad, repasamos lo básico con ejemplos fáciles." : "Empezamos desde cero, paso a paso, sin prisa.";
  document.getElementById("plan-texto").innerHTML = `<p><b>Hola ${nombre} 👋</b></p><p style="margin:8px 0">Materia: <b>${nombreMateria}</b> - Nivel: <b>${porc}%</b></p><p>${consejo}</p><p style="margin-top:8px"><b>Tu plan de hoy:</b><br>1️⃣ Repasar 1 concepto<br>2️⃣ Hacer 2 ejercicios juntos<br>3️⃣ Preguntarle a tu Tutor IA</p>`;
  document.getElementById("chat").innerHTML = "";
  agregarMensaje(`Hola ${nombre}, soy tu Tutor IA. Sacaste ${porc}% en ${nombreMateria}. ¿Empezamos con lo que más te costó?`, "bot");
}

function agregarMensaje(texto, tipo){
  const chat = document.getElementById("chat");
  const div = document.createElement("div");
  div.className = "msg " + tipo;
  div.textContent = texto;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function enviar(){
  const input = document.getElementById("pregunta");
  const texto = input.value.trim();
  if(!texto) return;
  agregarMensaje(texto, "user");
  input.value = "";
  try{
    const res = await fetch("/chat", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ mensaje: texto, materia: materia })
    });
    const data = await res.json();
    agregarMensaje(data.respuesta || data.reply || "Dime otra vez, ¿qué parte no entiendes?", "bot");
  } catch(e){
    agregarMensaje("Estoy aquí para ayudarte con " + materia + ". ¿Me pasas tu ejemplo de la tarea?", "bot");
  }
}

function hablar(){
  const texto = document.getElementById("pregunta").value || "Hola, explícame la masa molar";
  const u = new SpeechSynthesisUtterance(texto);
  u.lang = "es-MX";
  speechSynthesis.speak(u);
  agregarMensaje("🎤 Te escuché, ahora escríbeme tu duda y te la explico", "bot");
}

function volverInicio(){
  ocultar("p4"); mostrar("p1");
  document.getElementById("nombre").value = nombre;
}


function crearClave(texto){
  return texto.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9]+/g,"").slice(0,20) || "materia"+Date.now();
}

function agregarMateria(){
  const nombreMateria = prompt("¿Qué materia quieres agregar? Ej: Español");
  if(!nombreMateria || !nombreMateria.trim()) return;
  const tema = prompt("¿Qué tema? Ej: Verbos") || nombreMateria.trim();
  const clave = crearClave(nombreMateria);

  if(QUIZ[clave]){
    alert("Esa materia ya existe 👀 elígela del selector");
    document.getElementById("materia").value = clave;
    return;
  }


  QUIZ[clave] = [
    { q: `¿Cuál es el tema principal de ${tema}?`, op: [tema, "Otro tema", "Ninguno"], correcta: 0 },
    { q: `¿Qué quieres practicar de ${tema}?`, op: ["Lo básico", "Nada", "No sé"], correcta: 0 },
    { q: `¿Ya estudiaste ${tema} antes?`, op: ["Sí, un poco", "Nunca", "No recuerdo"], correcta: 0 }
  ];

  const sel = document.getElementById("materia");
  const opt = document.createElement("option");
  opt.value = clave;
  opt.textContent = `${nombreMateria.trim()} - ${tema.trim()}`;
  sel.appendChild(opt);
  sel.value = clave;
  alert("Materia agregada ✅ Ya la puedes usar");
}

function eliminarMateria(){
  const sel = document.getElementById("materia");
  const clave = sel.value;
  const texto = sel.selectedOptions[0] ? sel.selectedOptions[0].text : clave;
  if(!clave) return;
  if(sel.options.length <= 1){
    alert("No puedes borrar la última materia 😅");
    return;
  }
  if(!confirm(`¿Seguro que quieres eliminar "${texto}"?\nSe borrarán sus preguntas.`)) return;

  delete QUIZ[clave];
  sel.remove(sel.selectedIndex);
  materia = sel.value;
  alert("Materia eliminada 🗑️");
}


document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-empezar").addEventListener("click", empezarQuiz);
  document.getElementById("btn-plan").addEventListener("click", verPlan);
  document.getElementById("btn-enviar").addEventListener("click", enviar);
  document.getElementById("btn-voz").addEventListener("click", hablar);
  document.getElementById("btn-volver").addEventListener("click", volverInicio);

  document.getElementById("btn-agregar-materia").addEventListener("click", agregarMateria);
  document.getElementById("btn-eliminar-materia").addEventListener("click", eliminarMateria);
  const inp = document.getElementById("pregunta");
  inp.addEventListener("keydown", e => { if(e.key === "Enter") enviar(); });
  console.log("Botones conectados ✅");
}); 