from django.views.generic import TemplateView

class BaseTemplateView(TemplateView):
    """
    Clase de vista base para proporcionar plantillas con datos de contexto dinámicos.

    Atributos:
        page_names (dict): Un diccionario que asigna nombres de vista a nombres de visualización personalizados.

    Métodos:
        get_context_data(**kwargs): Anula el método get_context_data para incluir datos de contexto personalizados.

    """

    page_names = {
        'index': 'Home',
        'our_history': 'Our History',
        'location': 'Location',
        'potions_catalog': 'Potions Catalog',
        'contact_form': 'Contact Us',
    }

    def get_context_data(self, **kwargs):
        """
        Anula el método get_context_data para incluir datos de contexto personalizados.

        Returns:
            dict: Un diccionario que contiene los datos de contexto base junto con el nombre de la página actual.

        """
        context = super().get_context_data(**kwargs)
        view_name = self.request.resolver_match.url_name
        context["current_page"] = self.page_names.get(view_name, view_name.capitalize())
        return context


class IndexTemplate(BaseTemplateView):
    """
    Clase de vista para la página de inicio.

    Atributos:
        template_name (str): El nombre de la plantilla asociada a esta vista.

    """

    template_name = "index.html"


class LocationTemplate(BaseTemplateView):
    """
    Clase de vista para la página de ubicación.

    Atributos:
        template_name (str): El nombre de la plantilla asociada a esta vista.

    """

    template_name = "location.html"


class ContactFormTemplate(BaseTemplateView):
    """
    Clase de vista para la página de formulario de contacto.

    Atributos:
        template_name (str): El nombre de la plantilla asociada a esta vista.

    """

    template_name = "contact_form.html"


class OutHistoryTemplate(BaseTemplateView):
    """
    Clase de vista para la página de historia.

    Atributos:
        template_name (str): El nombre de la plantilla asociada a esta vista.

    """

    template_name = "our_history.html"


class PotionsCatalogTemplate(BaseTemplateView):
    """
    Clase de vista para la página del catálogo de pociones.

    Atributos:
        template_name (str): El nombre de la plantilla asociada a esta vista.

    """

    template_name = "potions_catalog.html"
