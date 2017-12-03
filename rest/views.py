from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework import generics
from user.models import CustomUser
from .serializers import UserSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import TokenAuthentication
from .authentication import ExpiringTokenAuthentication
import datetime

from rest_framework import status
from rest.serializers import ChecklistSerializer, ChecklistAnswerSerializer

from homepage.models import CheckList, ChecklistAnswer
# Create your views here.

class ChecklistList(APIView):

    def get(self, request, format=None):
        checklists = CheckList.objects.all()
        serializer = ChecklistSerializer(checklists, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class CheckListDetail(APIView):

    def getChecklist(self, pk):

        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def get(self, request, pk, format=None):

        print(pk)
        checklist = self.getChecklist(pk)

        serializer = ChecklistSerializer(checklist, many=False)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, pk):

        checklist = self.getChecklist(pk)
        serializer = ChecklistSerializer(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checklist = self.getChecklist(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ChecklistAnswerList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request, format=None):
        checklist_answers = ChecklistAnswer.objects.filter(answer_email=request.user.email)
        serializer = ChecklistAnswerSerializer(checklist_answers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = ChecklistAnswerSerializer(data=request.data)
        email = request.data['answer_email']
        checklist_pk = request.data['checklist']

        if serializer.is_valid():

            if ChecklistAnswer.objects.filter(answer_email=email, checklist=CheckList.objects.get(pk=str(checklist_pk))).count() > 0:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChecklistAnswersUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @csrf_exempt
    def get(self, request, email, format=None):
        checklist_answers = ChecklistAnswer.objects.filter(answer_email=email)
        serializer = ChecklistAnswerSerializer(checklist_answers, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ChecklistAnswerDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @csrf_exempt
    def getChAnswer(self, pk):  

        try:
            return ChecklistAnswer.objects.get(pk=pk)
        except ChecklistAnswer.DoesNotExist:
            return None

    @csrf_exempt
    def delete(self, request, pk, format=None):

        checklist_answer = self.getChAnswer(pk)
        if not checklist_answer:
            return Response({"error": "Not found"},status=status.HTTP_404_NOT_FOUND)
        if (checklist_answer.owner and checklist_answer.owner.auth_token != request.user.auth_token) or (request.user.email != checklist_answer.answer_email):
            return Response({"error": "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        checklist_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @csrf_exempt
    def get(self, request, pk, format=None):

        #if request.data['email']
        checklist_answer = self.getChAnswer(pk)
        serializer = ChecklistAnswerSerializer(checklist_answer, many=False)

        if not checklist_answer:
            return Response({"error": "Not found"},status=status.HTTP_404_NOT_FOUND)

        if (checklist_answer.owner and checklist_answer.owner.auth_token != request.user.auth_token) or (request.user.email != serializer.data['answer_email']):
            return Response({"error": "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data)



    @csrf_exempt
    def post(self, request, pk, format=None):

        ch_answer = self.getChAnswer(pk)
        serializer = ChecklistAnswerSerializer(ch_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserAuth(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            return Response({"error": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)

        Token.objects.filter(user=user).delete()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class UserAuthToken(ObtainAuthToken):

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            user = serializer.validated_data['user']
            Token.objects.filter(user=user).delete()
            token, created = Token.objects.get_or_create(user=user)

            #if not created:
                # update the created time of the token to keep it valid
             #   token.created = datetime.datetime.utcnow()
              #  token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



