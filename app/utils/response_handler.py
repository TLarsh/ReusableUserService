from rest_framework.response import Response
from rest_framework import status

class ResponseHandler:
    @staticmethod
    def success(message='', data=None, status_code=status.HTTP_200_OK):
        return Response({
            'message': message,
            'status': True,
            'data': data or {},
            'errors': None,
        }, status=status_code)
    
    @staticmethod
    def error(message='', errors=None, status_code=status.HTTP_400_BAD_REQUEST):
        return Response({
            'message': message,
            'status': False,
            'data': None,
            'errors': errors or None
        })