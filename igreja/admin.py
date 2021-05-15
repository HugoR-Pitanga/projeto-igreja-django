from django.contrib import admin
from .models import Ministerio, Agenda, MovimentoFinanceiro, TipoMovimentoFinanceiro, OrigemMovimentoFinanceiro

admin.site.register(Ministerio)
admin.site.register(Agenda)
admin.site.register(MovimentoFinanceiro)
admin.site.register(TipoMovimentoFinanceiro)
admin.site.register(OrigemMovimentoFinanceiro)