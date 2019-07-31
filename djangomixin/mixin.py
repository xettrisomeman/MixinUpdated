from django.core.exceptions import PermissionDenied


class OneRequired:
        #when class is fired , dispatch is the first method it calls
    def dispatch(self, request,*args,**kwargs):
        if kwargs['id'] == "hello-world": #if id provided in url is not equal to 1 then
            raise PermissionDenied #raise permissiondenied
        #else
        return super(OneRequired ,self).dispatch(request,*args,**kwargs)

