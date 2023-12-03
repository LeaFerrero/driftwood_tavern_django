/**
 * Una clase para renderizar datos en un contenedor HTML.
 */
export class Render {

    /**
     * Crea una instancia de la clase Render.
     *
     * @param {string} containerID - El ID del contenedor HTML donde se renderizarán los datos.
     */
    constructor(containerID) 
    {
        this.container = document.getElementById(containerID);
    }

    /**
     * Recupera datos de una URL y los renderiza en el contenedor HTML.
     *
     * @param {string} url - La URL desde la cual se recuperarán los datos.
     * @param {function} callback - Una función que procesa los datos y devuelve elementos HTML.
     * @param {Object} options - Opciones adicionales para la solicitud fetch (opcional).
     */
    fetchData(url, callback, options = {}) 
    {
        if (!callback) 
        {
            console.error("Callback function is missing.");
        }
        else 
        {
            fetch(url, options)
                .then(response => response.json())
                .then(data => {
                    let items = callback(data);
                    this.#renderInContainer(items);
                })
                
                .catch(error => {
                    console.error("Error during fetch:", error);
                });
        }
    }

    /**
     * Renderiza elementos HTML en el contenedor especificado.
     *
     * @private
     * @param {string} items - Elementos HTML a renderizar en el contenedor.
     */
    #renderInContainer(items) 
    {
        this.container.innerHTML = items;
    }
}
