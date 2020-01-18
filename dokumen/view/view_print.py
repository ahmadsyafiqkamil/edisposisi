from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from ..models import Dokumen, ValidasiDokumen
from django.views import generic
from django.conf import settings
import os


def PrintDokumen(request,slug):
    tmp_pdf = os.path.join(settings.BASE_DIR, 'tes.pdf')
    print(tmp_pdf)
    print(settings.BASE_DIR)
    dokumen = Dokumen.objects.get(slug= slug)

    if dokumen.status == '1':
        ttd = ValidasiDokumen.objects.get(dokumen__slug=slug)
        qr = '{} / {}'.format(ttd.dokumen,ttd.penandatangan)
        html_string = render_to_string('laporan/laporan-nota-dinas.html',
                                       {
                                           'dokumen': dokumen,
                                           'ttd': ttd,
                                           'qr':qr
                                       })
    else:
        html_string = render_to_string('laporan/laporan-nota-dinas.html',
                                       {
                                           'dokumen': dokumen,
                                       })
    html = HTML(string=html_string)
    html.write_pdf(target=tmp_pdf);

    fs = FileSystemStorage(settings.BASE_DIR)
    with fs.open(tmp_pdf) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = ' filename="report.pdf"'
        return response

    return response
