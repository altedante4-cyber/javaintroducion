const citas = [
    { texto: "El único modo de hacer un gran trabajo es amar lo que haces", autor: "Steve Jobs" },
    { texto: "La vida es lo que pasa cuando estás ocupado haciendo otros planes", autor: "John Lennon" },
    { texto: "El éxito no es definitivo, el fracaso no es fatal", autor: "Winston Churchill" },
    { texto: "Programa siempre como si el tipo que va a mantener tu código fuera un psicópata violento que sabe dónde vives", autor: "Jeff Atwood" },
    { texto: "Primero resuelve el problema. Luego, escribe el código", autor: "John Johnson" },
    { texto: "El conocimiento es poder", autor: "Francis Bacon" },
    { texto: "Sueña en grande y audaz", autor: "Walt Disney" },
    { texto: "La innovación distingue al líder del seguidores", autor: "Steve Jobs" },
    { texto: "Nunca es troppo tarde para ser lo que podrías haber sido", autor: "George Eliot" },
    { texto: "El código es como el humor. Cuando tienes que explicarlo, es malo", autor: "Cory House" }
];

const citaTexto = document.getElementById('cita-texto');
const citaAutor = document.getElementById('cita-autor');
const btnNuevaCita = document.getElementById('btnNuevaCita');

function mostrarCitaAleatoria() {
    const indiceAleatorio = Math.floor(Math.random() * citas.length);
    const cita = citas[indiceAleatorio];
    citaTexto.textContent = `"${cita.texto}"`;
    citaAutor.textContent = `- ${cita.autor}`;
}

btnNuevaCita.addEventListener('click', mostrarCitaAleatoria);

mostrarCitaAleatoria();
