/**
 * Validates that the name has more than 2 letters and is not numeric.
 * @param {string} name - Name to validate.
 * @returns {boolean} - True if the name is valid, false otherwise.
 */
const validateName = (name) => {
  return name.trim().length > 2 && isNaN(Number(name));
};

/**
 * Validates that the message has 1 or more words and is less than or equal to 25.
 * @param {string} message - Message to validate.
 * @returns {boolean} - True if the message is valid, false otherwise.
 */
const validateTextArea = (message) => {
  const words = message.split(/\s+/).filter((word) => word.length > 0);
  return words.length > 0 && words.length <= 25;
};

/**
 * Validates that the email is valid.
 * @param {string} email - Email to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

/**
 * Counts the number of words entered in the textarea.
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
 * Validates a form and displays error messages on invalid fields.
 *
 * @param {FormData} formData - The form data to validate.
 * @returns {boolean} - True if the form is valid, otherwise, false.
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
 * Clears the values of the form fields.
 */
const clearValues = () => {
  document.getElementById("name").textContent = "";
  document.getElementById("email").textContent = "";
  document.getElementById("message").textContent = "";
};


/**
 * Listens for the form submission event and performs form validation before submission.
 * If validation fails, prevents the form from submitting and displays an error message.
 * If validation is successful, shows an alert indicating that the form was submitted.
 */
const formSubmit = () => {
  document.getElementById("contact-form").addEventListener("submit", (event) => {
    // Gets the form data
    const formData = new FormData(event.target);
    
    // Validates the form
    if (!validateForm(formData)) 
    {
      event.preventDefault(); // Evitar que el formulario se envíe si la validación falla
    }
  });
}

// Initialization
formSubmit();
wordsCounter();
clearValues();


