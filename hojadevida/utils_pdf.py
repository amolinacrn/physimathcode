from io import BytesIO  # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings
from weasyprint import HTML, CSS
from xhtml2pdf import pisa
from django.template.loader import render_to_string
import os


pdf_settings = {
    "page-size": "Letter",
    "margin-top": "0.75in",
    "margin-right": "0.75in",
    "margin-bottom": "0.75in",
    "margin-left": "0.75in",
    "encoding": "UTF-8",
    "no-outline": None,
}


def render_pdf_view(template_path, context_dict={}):

    html = render_to_string(template_path, context_dict)

    respuesta_pdf = HttpResponse(content_type="application/pdf")
    respuesta_pdf["Content-Disposition"] = "inline; report.pdf"

    css_url = os.path.join(settings.BASE_DIR, "static/bs532/css/bootstrap.min.css")

    HTML(string=html).write_pdf(respuesta_pdf, stylesheets=[CSS(css_url)])

    return respuesta_pdf
