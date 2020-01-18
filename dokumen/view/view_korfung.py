#  Copyright (c) 2020.
#  Ahmad Syafiq Kamil

from django.views import generic
from ..models import Dokumen, ValidasiDokumen
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse


class Dashboard(generic.TemplateView):
    template_name = 'dokumen/korfung/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data()
        context['verified'] = Dokumen.objects.filter(fungsi=self.request.session['KODE_FUNGSI'], status=1)
        context['not_verified'] = Dokumen.objects.filter(fungsi=self.request.session['KODE_FUNGSI'], status=0)
        return context


class DetailDokumen(generic.DetailView):
    template_name = 'dokumen/korfung/detail-dokumen.html'
    model = Dokumen


@method_decorator(login_required, name='dispatch')
class TandatanganDokumen(generic.View):
    def get(self, request):
        slug = request.GET.get('slug', None)
        b = Dokumen.objects.get(slug=slug)
        a = ValidasiDokumen(dokumen=b,penandatangan=self.request.user)
        a.save()
        b.status = 1
        b.save()
        data = {
            'read': True
        }
        return JsonResponse(data)
