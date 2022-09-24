class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)

        return self._instance

    def __instancecheck__(self, instance):
        return isinstance(instance, self._cls)
