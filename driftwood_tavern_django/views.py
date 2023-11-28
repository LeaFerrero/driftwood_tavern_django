from django.views.generic import TemplateView

class BaseTemplateView(TemplateView):
    page_names = {
        'index': 'Home',
        'our_history': 'Our History',
        'location': 'Location',
        'potions_catalog': 'Potions Catalog',
        'contact_form': 'Contact Us',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_name = self.request.resolver_match.url_name
        context["current_page"] = self.page_names.get(view_name, view_name.capitalize())
        return context


class IndexTemplate(BaseTemplateView):
    template_name = "index.html"

class LocationTemplate(BaseTemplateView):
    template_name = "location.html"

class ContactFormTemplate(BaseTemplateView):
    template_name = "contact_form.html"

class OutHistoryTemplate(BaseTemplateView):
    template_name = "our_history.html"

class PotionsCatalogTemplate(BaseTemplateView):
    template_name = "potions_catalog.html"

