/**
 * Valida que el nombre tenga mas de 2 letras y no sea numerico
 * @param {string} name Nombre a validar
 * @returns {boolean} True si el nombre es valido, false si no lo es
 */
const validateName = (name) => {
  return name.trim().length > 2 && isNaN(Number(name));
};

/**
 * Valida que el mensaje 1 o mas palabras y menos o igual a 25
 * @param {string} message Mensaje a validar
 * @returns {boolean} True si el mensaje es valido, false si no lo es
 */
const validateTextArea = (message) => {
  const words = message.split(/\s+/).filter((word) => word.length > 0);
  return words.length > 0 && words.length <= 25;
};

/**
 * Valida que el mail sea valido
 * @param {string} email Email a validar 
 * @returns {boolean} True si el emal es valido, false si no lo es
 */
const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

/**
 * Cuenta la cantidad de palabas ingresadas en el textarea
 */
const wordsCounter = () => {
  const textarea = document.getElementById("message");
  const wordCount = document.getElementById("wordCount");
  
  textarea.addEventListener("input", () => {
    const words = textarea.value.split(/\b\S+\b/g).length - 1;
    wordCount.innerText = words;
  });
};

/**
 * Valida un formulario y muestra mensajes de error en campos inválidos.
 *
 * @param {FormData} formData Los datos del formulario a validar.
 * @returns {boolean} True si el formulario es válido, de lo contrario, false.
 */
const validateForm = (formData) => {
  const name = formData.get("name");
  const email = formData.get("email");
  const message = formData.get("message");

  const errorName = document.getElementById("error-name");
  const errorEmail = document.getElementById("error-email");
  const errorMessage = document.getElementById("error-message");

  errorName.textContent = !validateName(name) ? "Name needs 3+ letters." : "";
  errorEmail.textContent = !validateEmail(email) ? "Enter a valid email." : "";
  errorMessage.textContent = !validateTextArea(message) ? "Message limited to 25 words." : "";

  return !(errorName.textContent || errorEmail.textContent || errorMessage.textContent);
};


/**
 * Limpia los campos del formulario
 */
const clearValues = () => {
  document.getElementById("name").textContent = "";
  document.getElementById("email").textContent = "";
  document.getElementById("message").textContent = "";
};


/**
 * Escucha el evento de envío del formulario y realiza la validación del formulario antes de su envío.
 * Si la validación falla, evita que el formulario se envíe y muestra un mensaje de error. Si la validación es exitosa,
 * muestra una alerta indicando que el formulario fue enviado.
 *
 */
const formSubmit = () => {
  document.getElementById("contact-form").addEventListener("submit", (event) => {
    // Obtiene los datos del formulario
    const formData = new FormData(event.target);
    
    // Valida el formulario
    if (!validateForm(formData)) 
    {
      event.preventDefault(); // Evitar que el formulario se envíe si la validación falla
    }
  });
}

// Inicialización
formSubmit();
wordsCounter();
clearValues();


