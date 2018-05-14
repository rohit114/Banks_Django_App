from django.http import HttpResponse, request
from banks.models import Banks ,Branches
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


class getByIFSC(APIView):
    def post(self,request , format=None):
        ifsc = request.data['ifsc']
        bank_details = Branches.objects.filter(ifsc=ifsc)
        return Response({'ifsc':ifsc,
                         'bank_id':bank_details[0].bank_id.name,
                         'branch': bank_details[0].branch,
                         'address':bank_details[0].address,
                         'city': bank_details[0].city,
                         'district':bank_details[0].district,
                         'state': bank_details[0].state
                         })


class get_by_BankName_City(APIView):
    def post(self,request , format=None):
        bank_name = Banks.objects.filter(name=request.data['name'])
        banks = Branches.objects.filter(bank_id=bank_name[0],city=request.data['city'])
        Banks_deatial = list()
        for each_bank in banks:
            Banks_deatial.append({'ifsc':each_bank.ifsc,
          'bank_id':request.data['name'],
          'branch': each_bank.branch,
          'address':each_bank.address,
          'city': each_bank.city,
          'district':each_bank.district,
          'state': each_bank.state})

        return Response(Banks_deatial)