/* Here is the code for the dropdown menu */

const hamMenu = document.querySelector(".hamburger-menu");
const offScreenMenu = document.querySelector(".off-screen-menu");
const linksList = document.querySelectorAll(".navigation-links-list li");

// Add a click event to the hamburger menu
hamMenu.addEventListener("click", () => {
        // Toggle the "active" class for the hamburger menu and off-screen menu
    hamMenu.classList.toggle("active");
    offScreenMenu.classList.toggle("active");
});

// Add a click event to each <li> element within the navigation list
linksList.forEach(link => {
    // When a link is clicked, close the dropdown menu
    // This is to ensure that if, for example, "home" is clicked while on the home page, the menu closes and doesn't interfere
    link.addEventListener("click", () => {
        hamMenu.classList.toggle("active");
        offScreenMenu.classList.toggle("active");
        
    });
});



