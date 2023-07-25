from rest_framework.renderers import BrowsableAPIRenderer
from django.conf import settings


class NoHTMLFormBrowsableAPIRenderer(BrowsableAPIRenderer):

    def get_rendered_html_form(self, *args, **kwargs):
        """
        We don't want the HTML forms to be rendered because it can be
        really slow with large datasets
        """
        return ""

    def get_raw_data_form(self, *args, **kwargs):
        """
        We don't want the HTML raw to be rendered because it can be
        really slow with large datasets
        """
        return ""
