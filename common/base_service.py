from rest_framework.exceptions import NotFound


class ServicesManager:
    model = None

    @classmethod
    def get(cls, data, prefetch_=None, select_=None):
        try:
            return cls.model.objects.prefetch_related(*prefetch_ if prefetch_ else []).select_related(
                *select_ if select_ else []).get(**data)
        except cls.model.DoesNotExist:
            raise NotFound(f'{cls.model.__name__} not found')

    @classmethod
    def filter(cls, prefetch_=None, select_=None):
        return cls.model.objects.prefetch_related(*prefetch_ if prefetch_ else []).select_related(
            *select_ if select_ else [])