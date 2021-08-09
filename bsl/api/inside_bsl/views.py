from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Abonents
from django.core.exceptions import ObjectDoesNotExist


class Ping_View(APIView):
    @staticmethod
    def get(request):
        return Response({"status": Response.status_code,
                         "result": True,
                         "addition": {f"Сервис работает"},
                         "description": {}
                         })


class Add_View(APIView):
    @staticmethod
    def get(request):
        ids = request.query_params.get('id')
        amount = float(request.query_params.get('amount'))
        try:
            user = Abonents.objects.get(id=ids)
            status_user = user.status
            if status_user == 1:
                Abonents.objects.filter(id=ids).update(balance=user.balance + amount)
                operation_status = True
                return Response({"status": Response.status_code,
                                 "result": operation_status,
                                 "addition": {f"Баланс пользователя {user.name}, увеличен на {amount}"},
                                 "description": {}
                                 })
            elif status_user == 0:
                operation_status = False
                return Response({"status": Response.status_code,
                                 "result": operation_status,
                                 "addition": {f"Операции с пользователем запрещены"},
                                 "description": {}
                                 })
        except ObjectDoesNotExist:
            operation_status = False
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {f"Пользователь не найден"},
                             "description": {}
                             })
        except Exception as exp:
            print(f"Исключение {exp}")
            operation_status = False
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {f"Ошибка вызова запроса"},
                             "description": {}
                             })


class Substract_View(APIView):
    @staticmethod
    def get(request):
        ids = request.query_params.get('id')
        amount = float(request.query_params.get('amount'))
        try:
            user = Abonents.objects.get(id=ids)
            status_user = user.status
            if status_user == 1:
                if user.balance - amount - user.hold > 0:
                    Abonents.objects.filter(id=ids).update(balance=user.balance - amount - user.hold,
                                                           hold=0)
                    operation_status = True
                    return Response({"status": Response.status_code,
                                     "result": operation_status,
                                     "addition": {f"Баланс пользователя {user.name}, уменьшен на {amount + user.hold} "
                                                  f"в том числе hold {user.hold}"},
                                     "description": {}
                                     })
                else:
                    operation_status = False
                    return Response({"status": Response.status_code,
                                     "result": operation_status,
                                     "addition": {f"Недостаточсно баланса для совершения операции"},
                                     "description": {}
                                     })
            elif status_user == 0:
                operation_status = False
                return Response({"status": Response.status_code,
                                 "result": operation_status,
                                 "addition": {f"Операции с пользователем запрещены"},
                                 "description": {}
                                 })
        except ObjectDoesNotExist:
            operation_status = False
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {f"Пользователь не найден"},
                             "description": {}
                             })
        except Exception as exp:
            print(f"Исключение {exp}")
            operation_status = False
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {f"Ошибка вызова запроса"},
                             "description": {}
                             })


class Status_View(APIView):
    @staticmethod
    def get(request):
        ids = request.query_params.get('id')
        try:
            user = Abonents.objects.get(id=ids)
            status_user = user.status
            if status_user == 1:
                status_user = "Открыт"
            elif status_user == 0:
                status_user = "Закрыт"
            operation_status = True
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {'user': user.name,
                                          'uuid': user.uuid,
                                          'balance': user.balance,
                                          'hold': user.hold,
                                          'status_user': status_user
                                          },
                             "description": {}
                             })
        except ObjectDoesNotExist:
            operation_status = False
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {f"Пользователь не найден"},
                             "description": {}
                             })
        except Exception as exp:
            print(f"Исключение {exp}")
            operation_status = False
            return Response({"status": Response.status_code,
                             "result": operation_status,
                             "addition": {f"Ошибка вызова запроса"},
                             "description": {}
                             })
