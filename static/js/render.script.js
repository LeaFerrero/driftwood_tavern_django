/**
 * A class for rendering data in an HTML container.
 */
export class Render {

    /**
     * Creates an instance of the Render class.
     *
     * @param {string} containerID - The ID of the HTML container where data will be rendered.
     */
    constructor(containerID) 
    {
        this.container = document.getElementById(containerID);
    }

    /**
     * Fetches data from a URL and renders it in the HTML container.
     *
     * @param {string} url - The URL from which data will be retrieved.
     * @param {function} callback - A function that processes the data and returns HTML elements.
     * @param {Object} options - Additional options for the fetch request (optional).
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
     * Renders HTML elements in the specified container.
     *
     * @private
     * @param {string} items - HTML elements to render in the container.
     */
    #renderInContainer(items) 
    {
        this.container.innerHTML = items;
    }
}
