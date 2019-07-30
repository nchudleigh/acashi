class BaseEntity:
    def __init__(self, *arg, **kw):
        for attribute in self.__attributes__:
            setattr(self, attribute, kw[attribute])
