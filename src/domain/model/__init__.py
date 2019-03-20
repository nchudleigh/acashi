class Model:
    def __init__(self, **kw):
        # TODO: Check for DTO
        self._fields = self.DTO._fields
        for field in self._fields:
            setattr(self, field, kw[field])

    def to_dto(self):
        return self.DTO(*(getattr(self, field) for field in self._fields))
