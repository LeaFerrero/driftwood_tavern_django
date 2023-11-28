// Importa la clase Render desde el archivo "render.script.js"
import { Render } from "./render.script.js"

// Importa la función renderData desde el archivo "renderData.script.js"
import { renderData } from "./renderData.script.js"

// Crea una instancia de la clase Render y especifica el ID del contenedor como "app"
const app = new Render("app");

// Utiliza la instancia de Render para recuperar datos de la API y renderizarlos en el contenedor "app"
// La URL especificada busca elementos mágicos relacionados con "Potion of"
// La función renderData procesa los datos y devuelve elementos HTML
app.fetchData("https://api.open5e.com/v1/magicitems/?search=Potion of", renderData);
