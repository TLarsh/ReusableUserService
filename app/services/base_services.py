from django.core.exceptions import ValidationError

class BaseService:
    def execute(self, func, *args, **kwargs):

        try:
            result = func(*args, **kwargs)
            return result, None
        except ValidationError as e:
            return None, {'detail':str(e)}
        except Exception as e:
            return None, {'detail':str(e)}