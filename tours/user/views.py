from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     GenericAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     )
from rest_framework.response import Response
from .serializers import (UserSignUpSerializer,
                          UserLoginSerializer,
                          UserUpdateSerializer)
from .models import user
from rest_framework import status

class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj = user.objects.get(email=request.data["email"])

            response_data = {
                "id": obj.id,
                "fname": obj.fname,
                "lname": obj.lname,
                "email": obj.email,
                "username": obj.username
            }
            return Response(response_data)
        else:
            return Response(serializer.errors)


class GetUserListView(ListAPIView):
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        return user.objects.filter()

    def post(self, request,  *args, **kwargs):
        data = list()
        get_status = request.data["status"]
        user_data = user.objects.filter(status=get_status)
        serializer = self.get_serializer(user_data, many=True)


        for user in serializer.data:
            data.append({
                "id": user[0]["id"],
                "first_name": user[0]["first_name"],
                "last_name": user[0]["last_name"],
                "email": user[0]["email"],
                "description": user[0]["description"],
                "linkedin_url":user[0]["linkedin_url"],
                "contact_number":user[0]["contact_number"]
            })
        return Response(data, status.HTTP_200_OK)


class UserLoginAPIView(GenericAPIView):
        serializer_class = UserLoginSerializer

        def post(self, request, *args, **kwargs):
            print("REQUEST DATA", request.data)
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                obj=serializer.user

                response_data = {
                    "id": obj.id,
                    "first_name": obj.fname,
                    "lname": obj.lname,
                    "email": obj.email,
                    "username": obj.username
                }
                return Response(response_data)
            else:
                return Response(serializer.errors)


class DeleteUserView(DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = self.kwargs["pk"]
        user.objects.filter(id=user_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)


class UpdateUserAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return user.objects.filter(id=user_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fname = request.data["fname"]
        instance.lname = request.data["lname"]
        instance.contact = request.data["number"]
        instance.email = request.data["email"]

        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)