from django.views.generic import TemplateView

class BaseTemplateView(TemplateView):
    """
    Base view class to provide templates with dynamic context data.

    Attributes:
        page_names (dict): A dictionary mapping view names to custom display names.

    Methods:
        get_context_data(**kwargs): Overrides the get_context_data method to include custom context data.

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
        Overrides the get_context_data method to include custom context data.

        Returns:
            dict: A dictionary containing base context data along with the name of the current page.

        """
        context = super().get_context_data(**kwargs)
        view_name = self.request.resolver_match.url_name
        context["current_page"] = self.page_names.get(view_name, view_name.capitalize())
        return context


class IndexTemplate(BaseTemplateView):
    """
    View class for the home page.

    Attributes:
        template_name (str): The name of the template associated with this view.

    """

    template_name = "index.html"


class LocationTemplate(BaseTemplateView):
    """
    View class for the location page.

    Attributes:
        template_name (str): The name of the template associated with this view.

    """

    template_name = "location.html"


class ContactFormTemplate(BaseTemplateView):
    """
    View class for the contact form page.

    Attributes:
        template_name (str): The name of the template associated with this view.

    """

    template_name = "contact_form.html"


class OutHistoryTemplate(BaseTemplateView):
    """
    View class for the history page.

    Attributes:
        template_name (str): The name of the template associated with this view.

    """

    template_name = "our_history.html"


class PotionsCatalogTemplate(BaseTemplateView):
    """
    View class for the potions catalog page.

    Attributes:
        template_name (str): The name of the template associated with this view.

    """

    template_name = "potions_catalog.html"
