from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from datetime import datetime, timedelta
import pytz




def creatUTC():
    utc = pytz.utc 
    current_utc_time = datetime.now(utc)
    time_window = timedelta(hours=2)

    utc_two_hours_forward = current_utc_time + time_window
    utc_two_hours_backward = current_utc_time - time_window

    current_utc_formatted = current_utc_time.strftime('utc: %Y-%m-%dT%H:%M:%SZ') 
    utc_two_hours_forward_formatted = utc_two_hours_forward.strftime('val2+: %Y-%m-%dT%H:%M:%SZ')
    utc_two_hours_backward_formatted = utc_two_hours_backward.strftime('val2-: %Y-%m-%dT%H:%M:%SZ')

    return current_utc_formatted


@api_view(['GET'])
# @renderer_classes([JSONRenderer])
def loadAPIView(request, format=None):
    if request.method == 'GET':
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        if slack_name and track:
            current_day = datetime.now()
            day = current_day.strftime('%A')
            github_file_url =  "https://github.com/lady-thee/django_api_get_endpoint/blob/main/api/views.py"
            github_url = "https://github.com/lady-thee/django_api_get_endpoint.git"
            utc = creatUTC()

            data = {
                'slack_name': slack_name,
                'current_day': day,
                'utc_time': utc,
                'track': track,
                'github_file_url': github_file_url,
                'github_repo_url': github_url,
                'status': status.HTTP_200_OK
            }
            return JsonResponse(data)
        else:
            safe = {
                'status': status.HTTP_200_OK
            }
            return Response(safe)

    safe = {
        'status': status.HTTP_200_OK
    }
    return Response(safe)