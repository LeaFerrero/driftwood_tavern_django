/* Aca esta el codigo del menu desplegable */

const hamMenu = document.querySelector(".hamburger-menu");
const offScreenMenu = document.querySelector(".off-screen-menu");
const linksList = document.querySelectorAll(".navigation-links-list li");

//Agrega un evento de click al menu de hamburguesa
hamMenu.addEventListener("click", () => {
        //Alterna la clase "active" del menu hamburguesa y del menu fuera de pantalla
    hamMenu.classList.toggle("active");
    offScreenMenu.classList.toggle("active");
});

//Agrega un evento click a cada elemento <li> dentro de la lista de navegacion
linksList.forEach(link => {
    //Cuando se hace click en un enlace se cierra el menu desplegable
    //Esto es para que por ejemplo si se clickea "inicio" estando en la pagina de inicio, el menu se cierre y no moleste
    link.addEventListener("click", () => {
        hamMenu.classList.toggle("active");
        offScreenMenu.classList.toggle("active");
        
    });
});



