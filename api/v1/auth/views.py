from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.v1.auth.serializer import UserSerializer
from register.models import User


class AuthView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        method = data.get('method')
        params = data.get('params')

        if not method:
            return Response({
                "Error": "Method kiritilmagan"
            })

        if params is None:
            return Response({
                "Error": "Params kiritilmagan"
            })

        if method == "register":
            username = params.get("username")
            user = User.objects.filter(username=username)

            if user:
                return Response({
                    "Error": "Bunaqa user allaqachon bor"
                })

            serializer = self.get_serializer(data=params)
            serializer.is_valid(raise_exception=True)
            root = serializer.create(serializer.data)
            root.set_password(params["password"])
            root.save()

            token = Token()
            token.user = root
            token.save()
        elif method == "login":
            nott = "username" if "username" not in params else "password" if "password" not in params else None
            if nott:
                return Response({
                    "Error": f"params.{nott} shu polya to'ldirilmagan"
                })

            username = params.get("username")
            user = User.objects.filter(username=username).first()

            if not user:
                return Response({
                    "Error": "Bunaqa user topilmadi"
                })

            if not user.check_password(params['password']):
                return Response({
                    "Error": "Parol Xato"
                })
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token()
                token.user = user
                token.save()
        else:
            return Response({
                "Error": "Bunday method yo'q"
            })

        return Response({
            "token": f"{token.key}"
        })









