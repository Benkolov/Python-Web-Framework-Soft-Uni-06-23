from rest_framework import generics as rest_generics_views, permissions, exceptions as rest_exceptions


from todo_app.api_todos.models import Todo, Category
from todo_app.api_todos.serializers import CategorySerializer, TodoForListSerializer, TodoForCreateSerializers, \
    TodoForDetailsSerializers


class ListCreateTodoApiView(rest_generics_views.ListCreateAPIView):
    queryset = Todo.objects.all()

    list_serializer_class = TodoForListSerializer
    create_serializer_class = TodoForCreateSerializers

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        else:
            return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset =  queryset.filter(user=self.request.user)
        category_id = self.request.query_params.get('category', None)
        if category_id :
            queryset = queryset.filter(category=category_id)

        return queryset


class DetailsTodoApiView(rest_generics_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoForDetailsSerializers
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        todo = super().get_object()

        if todo.user != self.request.user:
            raise rest_exceptions.PermissionDenied

        return todo


class ListCategoriesApiView(rest_generics_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return self.queryset.filter(todo__user_id=self.request.user.id).distinct()
