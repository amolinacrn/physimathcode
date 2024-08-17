from io import BytesIO  # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.conf import settings
from weasyprint import HTML, CSS
from xhtml2pdf import pisa
import os


# def render_pdf_view(template_path, context_dict={}):
#     # Crear un objeto de respuesta Django, y especificar content_type como pdf
#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context_dict)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     # si error entonces mostrar alguna vista divertida
#     if pisa_status.err:
#         return HttpResponse("We had some errors <pre>" + html + "</pre>")
#     return response


def render_pdf_view(template_path, context_dict={}):
    template = get_template(template_path)
    html = template.render(context_dict)

    css_url = os.path.join(settings.BASE_DIR, "static/bs532/css/bootstrap.min.css")

    HTML(string=html).write_pdf(target="ajdcvas.pdf", stylesheets=[CSS(css_url)])
