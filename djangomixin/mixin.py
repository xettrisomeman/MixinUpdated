from django.core.exceptions import PermissionDenied


class OneRequired:

    def dispatch(self, request,*args,**kwargs):
        if kwargs['id'] != 1:
            raise PermissionDenied

        return super(OneRequired ,self).dispatch(request,*args,**kwargs)

