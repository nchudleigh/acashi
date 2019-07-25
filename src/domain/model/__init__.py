class Model:
    def __init__(self, **kw):
        self.validate()

    def to_dto(self):
        return self.DTO(*(getattr(self, field) for field in self._fields))
