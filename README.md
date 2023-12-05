<h1>Documentacion de TIF Backend CaC - Stio Web Driftwood Tavern - Tavern & inn -</h1>

<h2>1 - Titulo y descripción del proyecto</h2>
<ul>
  <li>
    <b>Titulo:</b> Driftwood Tavern - Tavern & inn.
  </li>
  <li>
    <b>Descripcion:</b> El sitio es en sí, es un sitio web de un bar, pero para hacer algo distinto se optó por darle otra temática y surgió la idea "¿y si este bar       está ubicado en el mundo de Dungeons & Dragons (el juego de rol)?" "¿Cómo sería que la tabernera nos encargue un sitio para promocionar una taberna en un mundo        sí?". Bajo esta línea de pensamiento se desarrolló el sitio. Es un sitio web para promocionar una taberna en un mundo de fantasía. Aunque con ligeros cambios          puede adaptarse a cualquier bar del mundo real. </br>
    Aclarado esto, Driftwood Tavern existe dentro del mundo de Dungeons & Dragons y para armar el sitio se saco informacion  de
    <a href="https://forgottenrealms.fandom.com/wiki/Driftwood_Tavern">Forgotten Realms Wiki</a> y de <a     
    href="https://neverwinter.fandom.com/wiki/Driftwood_Tavern">Neverwinter Wiki</a>, aunque la informacion no es igual en los dos sitios, si es la misma taberna.  
  </li>
</ul>


<h2>2 - Publico objetivo</h2>
<ul>
  <li>
    <b>Publico:</b> Aventureros que se encuentren en busca de un buen lugar donde comer, descansar o reabastecer su inventario de pociones.
  </li>
</ul>

<h2>3 - Tecnologias utilizadas</h2>
<ul>
  <li><strong>Frontend</strong>:
    <ul>
      <li>Lenguajes: HTML, CSS, JavaScript</li>
    </ul>
  </li>
  <li><strong>Backend</strong>:
    <ul>
      <li>Lenguaje de programación: Python</li>
      <li>Frameworks o librerías: Django</li>
      <li>Base de datos: MySQL</li>
    </ul>
  </li>
  <li><strong>Deploy</strong>:
    <ul>
      <li>Plataforma de deploy: PythonAnywhere</li>
    </ul>
  </li>
</ul>

<h2>4 - Estructura de archivos y carpetas del proyecto.</h2>
  
  ```
  .
  ├── README.md
  ├── app_menu
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations
  │   │   ├── 0001_initial.py
  │   │   ├── 0002_alter_menu_table.py
  │   │   ├── 0003_alter_menu_options.py
  │   │   ├── 0004_remove_menu_price_menu_currency_menu_price_amount.py
  │   │   ├── 0005_alter_menu_currency_alter_menu_description_and_more.py
  │   │   ├── 0006_alter_menu_item_type.py
  │   │   └── __init__.py
  │   ├── models.py
  │   ├── router.py
  │   ├── serializers.py
  │   ├── static
  │   │   ├── css
  │   │   │   ├── app.general.style.css
  │   │   │   ├── app.keyframe.style.css
  │   │   │   └── app.style.css
  │   │   └── media
  │   │       └── fonts
  │   │           ├── Bookinsanity.otf
  │   │           ├── Mr-Eaves-Small-Caps.otf
  │   │           ├── Scaly-Sans-Bold.otf
  │   │           ├── Scaly-Sans-Caps.otf
  │   │           └── Scaly-Sans.otf
  │   ├── templates
  │   │   ├── menu.html
  │   │   ├── menu_create.html
  │   │   ├── menu_delete.html
  │   │   └── menu_detail.html
  │   ├── tests.py
  │   ├── urls.py
  │   ├── views.py
  │   └── viewsets.py
  ├── driftwood_tavern_django
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   ├── views.py
  │   └── wsgi.py
  ├── manage.py
  ├── requirements.txt
  ├── static
  │   ├── css
  │   │   ├── footer.style.css
  │   │   ├── general.style.css
  │   │   ├── header.style.css
  │   │   ├── keyframe.style.css
  │   │   └── main.style.css
  │   ├── js
  │   │   ├── menu.script.js
  │   │   ├── potions-catalog.script.js
  │   │   ├── render.script.js
  │   │   ├── renderData.script.js
  │   │   └── validations.script.js
  │   └── media
  │       ├── fonts
  │       │   ├── Bookinsanity.otf
  │       │   ├── Mr-Eaves-Small-Caps.otf
  │       │   ├── Scaly-Sans-Bold.otf
  │       │   ├── Scaly-Sans-Caps.otf
  │       │   └── Scaly-Sans.otf
  │       ├── icons
  │       │   ├── facebook.png
  │       │   ├── galeon.png
  │       │   ├── gorjeo.png
  │       │   └── instagram.png
  │       └── images
  │           ├── background.jpg
  │           ├── bardic-inspiration.png
  │           ├── bedroom.png
  │           ├── driftwoodtavern.png
  │           ├── madam-rosene.png
  │           ├── note-border.png
  │           ├── party-eating.png
  │           ├── potions-catalog.png
  │           ├── scroll-of-sending.png
  │           ├── stable.png
  │           └── tavern-image.png
  └── templates
      ├── base.html
      ├── contact_form.html
      ├── index.html
      ├── location.html
      ├── our_history.html
      └── potions_catalog.html
  ```

<h2>5 - Estructura del sitio</h2>
<ul>
  <li><b>Estructura:</b><br>

    ```
      Home
      ├── Our History
      ├── Location
      ├── Menu
      │   ├── Create
      │   ├── Read
      │   ├── Update
      │   └── Delete
      ├── Potions Catalog
      ├── Contact Us
      └── Social Media
    
    ```

  </li>
  <br>
  <li><b>Maquetado:</b>
    <p> El maquetado incluido corresponde a la ultima iteracion del diseño.
    <ul>
      <li>
        <b>Maquetado para pantallas inferiores a 1080:</b>
        <img src="https://raw.githubusercontent.com/LeaFerrero/images/main/inferior1080.png?token=GHSAT0AAAAAACKTNZ3MHIJK5PD2LY26JSVWZLPUREA" alt="imagen pantallas                 inferiores a 1080">
      </li>
      <li>
        <b>Maquetado para pantallass superiores a 1080:</b>
        <img src="https://raw.githubusercontent.com/LeaFerrero/images/main/sueperior1080.png?token=GHSAT0AAAAAACKTNZ3NBO5M5O7FLDLUWWOGZLPURSQ" alt="imagen pantallas     
        superiores a 1080">
      </li>
      <li>
        <b>Maquetado de cómo se deberían representar las secciones:</b> 
        <img src="https://raw.githubusercontent.com/LeaFerrero/tpo-driftwood-tavern/main/layout/section.png" alt="seccion">
      </li>
      <li>
        <b>Maquetado de cómo se deberían representar la seccion de Menu (app del sitio):</b> 
        <img src="https://raw.githubusercontent.com/LeaFerrero/images/main/menu-section.png?token=GHSAT0AAAAAACKTNZ3NIKKTB6FZ4PH5NUGMZLPUTJQ" alt="seccion menu">
      </li>
    </ul>
  </li>
</ul>

<h2>6 - Diseño y Estilo:</h2>
<p>
  Teniendo en cuenta que el sitio web está creado para una taberna dentro del juego de rol de Dungeons & Dragons, se buscó darle la estética del manual de dicho 
  juego, tanto fuentes como paleta de colores se <i><b>sacaron del manual</b></i>. Tambien ciertas decisiones funcionales se basaron en dicha estetica, por ejemplo,     el formulario de contacto dice que "no pueden enviarse mas de 25 palabras", esta decicion no es abritraria, ya que, dento del juego hay un hechizo, <a               
  href="https://roll20.net/compendium/dnd5e/Sending#content">Sending</a>, que permite enviar un mensaje a distancia de no mas de 25 palabras, y el "scroll of sending" 
  mencionado, es un item consumible que proporciona dicho hehizo.<br>
  Lo unico un tanto mas diferente es que las imagenes estan dentro de los recuadros adornados, que en el manual contiene texto (como se muestra mas abajo en la 
  imagenes del manual, concretamente en la segunda pagina de la segunda imagen en el recuadro de "Draconidos"), se opto por hacerlo asi porque para 
  incluir las imagenes como en el manual se hubiese necesitado edición, y no alcanzaba el tiempo, hecho de esta forma se pudo incluir imagenes que acomañen al texto     sin perder la referencia pero tambien sin que el contenido sea todo texto.<br>
  Para la forma en la que se muestran las imagenes y los textos en pantalla se uso este sitio como referencia: <a href="https://www.quay.com.au">Quay</a>. Si bien       Driftwood Tavern no es un calco, y no busca serlo, si presenta algunas similitudes, fue en un principio un punto importante por donde arrancar el proyecto, porque     no habia mucha idea de diseño ni maquetado, asi que es importante dejarlo documentado.
</p>

<p>A continuación unas imagenes de las páginas del manual:</p>
<img src="https://tothetablereviews.files.wordpress.com/2014/09/img_3155.jpg" alt="imagen de manual DnD">
<img src="https://github.com/LeaFerrero/images/blob/main/sample-design.jpg" alt="imagen de manual DnD">
<br>

<ul>
  <li>
    <b>Diseño y estilo:</b> Medieval fantástico, intentando imitar el manual del jugador de Dungeons & Dragons.
  </li>
  <li>
    <b>Colores:</b> Tonos marrones y amarillos, verde claro para las tablas.
  </li>
  <li><b>Tipografía:</b> Fue conseguida del repositorio https://github.com/jonathonf/solbera-dnd-fonts/tree/master.</br> 
  A continuación una lista de qué tipografía se usa y dónde:
    <ul>
      <li>Mr Eaves Small Caps: encabezados.</li>
      <li>Booksanity: párrafos.</li>
      <li>Scaly Sans: formularios, mensaje de error de los formularios, texto de botones, footer, tbody de las tablas de menu y de pociones.</li>
      <li>Scaly Sans Bold: thead de las tablas de menu y de pociones.</li>
      <li>Scaly Sans Caps: menú desplegable.</li>
    </ul>
  </li>
</ul>

<h2>7 - Contenido y Funcionalidades</h2>
<ul>
  <li>
    <b>Contenido:</b>
    <ul>
      <li>Información detallada sobre los servicios del lugar: taberna, posada, shows, catálogo de pociones y establos.</li>
      <li>Información detallada de la historia del lugar.</li>
      <li>Información sobre cómo llegar.</li>
      <li>Información del menú de la taberna, y CRUD para crear, ver detalles, actualizar o borrar los productos del menú .</li>
      <li>Imágenes que acompañan el texto y al formulario:
        <ul>
          <li>Imagen de bardo: Extraída del manual del jugador de Dungeons & Dragons 5ta edición.</li>
          <li>Imagen de dormitorio: Ephellem, <a href="https://ar.pinterest.com/ephellem/">Pinterest</a>.</li>
          <li>Imagen de establo: Extraída de <a href="https://ar.pinterest.com/pin/857654322810939138/">Pinterest</a>.</li>
          <li>Imagen de estante de pociones: Extraída de <a href="https://www.pinterest.es/pin/21814379439074113/">Pinterest</a>.</li>
          <li>Imagen de fondo de la taberna: Yami-Yami, <a href="https://www.artstation.com/artwork/QXW90d">ArtStation</a>.</li>
          <li>Imagen de gente comiendo en la taberna: Extraída de <a href="https://www.diceanddragons.com/post/a-feast-for-adventurers-the-100-                   
          fantastical-foods-you-can-order-from-a-tavern">Dice and Dragons</a>.</li>
          <li>Imagen de logo: Creada para el proyecto por Agustina Zappia.</li>
          <li>Imagen de Madam Rosene: Creada con IA en <a href="https://stablediffusionweb.com">Stable Diffusion Web</a>.</li>
          <li>Imagen de scroll: Konstantin Roshchin, <a href="https://www.artstation.com/artwork/VxvLR">ArtStation</a>.</li>
        </ul>
      </li>
      <li>Iconos utilizados en la página:
        <ul>
          <li><b>Icono de barco (favicon):</b> <a href="https://www.flaticon.es/icono-gratis/galeon_210587">Flaticon</a>.</li>
          <li><b>Icono de Twitter:</b> <a href="https://www.flaticon.es/icono-gratis/gorjeo_1384049">Flaticon</a>.</li>
          <li><b>Icono de Facebook:</b> <a href="https://www.flaticon.es/icono-gratis/facebook_1384021?                                      
          related_id=1384005&origin=search">Flaticon</a>.</li>
          <li><b>Icono de Instagram:</b> <a href="https://www.flaticon.es/icono-gratis/instagram_1384047?related_id=1384015&origin=search">Flaticon</a>.</li>
        </ul>
        <p>
          Aclaración importante: como la taberna no existe en el mundo real, hacer clic sobre los iconos de Facebook, Twitter o Instagram redirigirá a la página oficial de Dungeons & Dragons en la red social                correspondiente.
        </p>
      </li>
    </ul>
  </li>
  <li>
     <b>Funcionalidades:</b>
    <ul>
      <li>Menu desplegable.</li>
      <li>Formulario de contacto funcional con <a href="https://getform.io">Getform</a>.</li>
      <li>CRUD en la la seccion "MENU": crear, leer, actualizar o eliminar los productos del menu de la taberna.</li>
    </ul>  
  </li>
</ul>

<h2>8 - Integrantes del equipo y representante:</h2>
<ul>
  <li><b>Equipo:</b> 
    <ul>
      <li>Leandro Raúl Ferrero: representante, coordinador, maquetacion, diseño, desarrollo, contenido, deploy</li>
      <li>Janni Granados: desarrollo, formulario, validaciones del formulario, correccion de estilos</li>
    </ul>
  </li>
</ul>

<h2>10 - Recursos Externos:</h2>
<ul>
  <li>Consumo de la API <a href="https://open5e.com">Open5e</a> para cargar la lista de pociones que se muestra en la pagina "Potions Catalog".</li>
  <li>Implementación del mapa interactivo de <a href="https://neverwinteractive.com">Neverwinter Interactive Maps</a> en la sección "Location" a través de un iframe.    </li>
  <li>Integración de <a href="https://getform.io">Getform</a> para la funcionalidad del formulario contacto.</li>
</ul>

<h2>11 - Desarrollos Futuros y Mejoras Potenciales:</h2>
<ul>
  <li>Cerear una animacion de rueda de carga para mostrar antes de que carge la tabla de pociones.</li>
</ul>

<h2>12 - Contacto:</h2>
<ul>
  <li><b>Email de representante: </b><a href="mailto:learferrero@gmail.com" target="_blank" rel="noopener noreferrer                                    nofollow">learferrero@gmail.com</a></li>
</ul>

<h2>13 - Fecha de entrega:</h2>
<ul>
  <li><b>5 de Diciembre de 2023</b></li>
</ul>

<h2>14 - Acreditaciones adicionales:</h2>
<p>
  El proyecto se sometio a testeos y se itero varias veces para mejorar tanto el contenido como la experiencia de usuario. Fue una parte importante para el proyecto asi que considero importante dejarlo asentado.<br>
  Los testeos fueron realizados por gente tanto agena al pryecto como Codo a Codo. Se incluye la lista a continuacion, con nombre, 
  dispositivo y navegador utilizados para el testeo.
</p>
<ul>
  <li>Agustina Zappia: PC - Firefox.
  <li>Mariano Gonzalez Walsh: PC - Opera GX, PC - Google Chrome, Android - Navegador de Samsung.</li>
  <li>Patricia Gonzalez Walsh: PC Opera GX, Android - Google Chrome.</li>
</ul>

<p>
  Si bien durante el desarrollo se tuvo en cuenta que tambien el diseño sea adaptable a pantallas de tablet, nadie tenia una tablet para el testeo. No descarto   que    pueda haber algun problema, pero sin ninguna tablet en que probar el sitio es imposible estar seguro.
  Ademas, la página fue pensada en español en un principio, pero como la API consumida está en inglés, y en base a testeos de usuarios que les chocaba que haya dos      idiomas distintos, se optó por cambiar todo a inglés.
</p>
