from src.db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))  # 80 characters limit
    price = db.Column(db.Float(precision=2))  # numbers after the comma

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  # Foreign key to link items & stores
    store = db.relationship('StoreModel')  # Now no joins necessary

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self) -> dict:
        """
        Returns the name & price as .json string.

        :return: {'name': String, 'price': Int}
        """
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name: str) -> object:
        """
        Find an object by its name.

        :param name: Item name to find.
        :return: Object of Item-class.
        """
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self) -> None:
        """
        Insert new or update existing object in data base.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        """
        Delete object from the data base.
        """
        db.session.delete(self)
        db.session.commit()
