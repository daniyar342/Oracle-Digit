from rest_framework.response import Response
from rest_framework import status

from common.utils import get_object
from django.db import transaction


class ListModelMixin:
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            self.service_class.filter(prefetch_=self.prefetch_, select_=self.select_))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CreateModelMixin:
    """
    Create a model instance. 
    """

    def create(self, request, *args, **kwargs):
        serializer = self.validate_serializer_class(data=request.data,)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        obj = self.service_class.create(**serializer.validated_data)
        return Response(self.serializer_class(obj).data, status=status.HTTP_201_CREATED)


class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, **kwargs):
        instance = get_object(self, request, kwargs['id'], self.prefetch_, self.select_)
        serializer = self.serializer_class(
            instance)
        return Response(serializer.data)


class UpdateModelMixin:
    """
    Update a model instance.
    """

    def update(self, request, **kwargs):
        obj = get_object(self, request, kwargs['id'])
        serializer = self.validate_serializer_class(data=request.data,)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['obj'] = obj
        serializer.validated_data['user'] = request.user
        obj = self.service_class.update(**serializer.validated_data)

        return Response(data=self.serializer_class(obj).data, status=status.HTTP_200_OK)

    def partial_update(self, request, id):
        obj = get_object(self, request, id)
        serializer = self.validate_serializer_class(data=request.data,
                                                    partial=True)
        serializer.is_valid(raise_exception=True)
        obj = self.service_class.update(obj, fields=serializer.validated_data, user=request.user)

        return Response(data=self.serializer_class(obj).data, status=status.HTTP_200_OK)


class DestroyModelMixin:
    """
    Destroy a model instance.
    """

    def destroy(self, request, **kwargs):
        with transaction.atomic():
            instance = get_object(self, request, kwargs['id'])
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
