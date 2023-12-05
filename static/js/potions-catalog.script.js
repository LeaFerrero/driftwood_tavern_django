// Import the Render class from the "render.script.js" file
import { Render } from "./render.script.js"

// Import the renderData function from the "renderData.script.js" file
import { renderData } from "./renderData.script.js"

// Create an instance of the Render class and specify the container ID as "app"
const app = new Render("app");

// Use the Render instance to fetch data from the API and render it in the "app" container
// The specified URL searches for magical items related to "Potion of"
// The renderData function processes the data and returns HTML elements
app.fetchData("https://api.open5e.com/v1/magicitems/?search=Potion of", renderData);
