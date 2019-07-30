class BaseRepo:
    def get_by_key(self, key):
        dao = session.query(self.dao).filter(self.dao.key == key).first()
        if dao is None:
            return None

        return self.to_entity(dao)

    def to_dao(self, entity):
        return self.dao(
            **{
                attribute: getattr(entity, attribute)
                for attribute in entity.__attributes__
            }
        )

    def to_entity(self, dao):
        return self.entity(
            **{
                attribute: getattr(dao, attribute)
                for attribute in self.entity.__attributes__
            }
        )

