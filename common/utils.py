def get_object(obj, request, id, prefetch_=None, select_=None):
    return obj.service_class.get(
        {'id': id}, prefetch_, select_
    )
