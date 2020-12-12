from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.response import Response
from .models import package
from .serializers import PackageSerializer, UpdatePackageSerializer


class CreatePackageAPIView(CreateAPIView):
    serializer_class = PackageSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class PackageListView(ListAPIView):
    serializer_class = PackageSerializer

    def get_queryset(self):
        return package.objects.filter()

    def post(self, request,  *args, **kwargs):
        data = list()
        get_status = request.data["status"]
        package_data = package.objects.filter(status=get_status)
        serializer = self.get_serializer(package_data, many=True)


        for package in serializer.data:
            data.append({
                "id": package[0]["id"],
                "pname": package[0]["pname"],
                "ptype": package[0]["ptype"],
                "plocation": package[0]["plocation"],
                "price": package[0]["price"]
            })
        return Response(data, status.HTTP_200_OK)

class UpdatePackageAPIView(UpdateAPIView):
    serializer_class = UpdatePackageSerializer

    def get_queryset(self):
        package_id = self.kwargs['pk']
        return package.objects.filter(id=package_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.pname= request.data["pname"]
        instance.ptype=request.data["ptype"]
        instance.plocation=request.data["plocation"]
        instance.price=request.data["price"]

        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)

class DeletePackageView(DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        package_id = self.kwargs["pk"]
        package.objects.filter(id=package_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)
