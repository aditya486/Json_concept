from django.shortcuts import render
from django.http import HttpResponse
# from django.core.serializers import serialize
# from django.core import serializers
from django.views.generic import View
from rest_app.models import Employee
import json
from rest_app.mixins import SerializeMixin,HttpResponseMixins
from rest_app.utils import is_json
from rest_app.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




class EmployeeDetailCBV(SerializeMixin,HttpResponseMixins,View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'the requested resource not available'})
            return self.render_to_http_reponse(json_data,status=404)
        else:
            json_data=self.serialize([emp,])
            return self.render_to_http_reponse(json_data)
        # emp_data={

        # 'eno': emp.eno,
        # 'ename': emp.ename,
        # 'esal': emp.esal,
        # 'eaddr': emp.eaddr,
        # }
        # print(emp_data)
        # json_data=json.dumps(emp)
        # print(json_data)
        # xuv = json.loads(json_data)
        # print(xuv)
        # return HttpResponse(json_data, content_type='application/json')
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(SerializeMixin,HttpResponseMixins,View):
    def get(self, request,*args, **kwargs):
        ps = Employee.objects.all()
        # print(qs.json())
        # emp_data={
        # 'eno': ps.eno,
        # 'ename': ps.ename,
        # 'esal': ps.esal,
        # 'eaddr': ps.eaddr,
        # }
        json_data= self.serialize(ps)
        # print(data)
        # json_data=json.dumps(emp_data)
        # print(json_data)
        # xuv = json.loads(json_data)
        # # print(xuv)
        # final_list = []
        # for obj in xuv:
        #     emp_data = obj['fields']
        #     final_list.append(emp_data)
        #
        # data = json.dumps(final_list)
        # print(data)
        return HttpResponse(json_data, content_type='application/json')
        # return HttpResponse(json_data, content_type='application/json')
    def post(self, request,*args, **kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid data only'})
            return self.render_to_http_reponse(json_data, status=400)
        emp_data=json.loads(data)
        form= EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data= json.dumps({'msg':'resource created successfully'})
            return self.render_to_http_reponse(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_reponse(json_data,status=400)

# Create your views here.
