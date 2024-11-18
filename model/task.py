class Task:
    def __init__(self, action, value=None, use_correction=True, **kwargs):
        self.action = action
        self.value = value
        self.use_correction = use_correction
        self.kwargs = kwargs
