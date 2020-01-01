#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from dokumen.models import Dokumen,TujuanDokumen,Fungsi,JenisDokumen,Klasifikasi

class DokumenType(DjangoObjectType):
    class Meta:
        model = Dokumen

class TujuanDokumenType(DjangoObjectType):
    class Meta:
        model = TujuanDokumen

class FungsiType(DjangoObjectType):
    class Meta:
        model = Fungsi

class JenisDokumenType(DjangoObjectType):
    class Meta:
        model = JenisDokumen

class KlasifikasiType(DjangoObjectType):
    class Meta:
        model = Klasifikasi


# class Query(ObjectType):
