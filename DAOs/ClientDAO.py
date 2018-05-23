from DAOs import db


class ClientDAO:
    def __init__(self, client_id):
        self.db = db.get_db()
        self.id = client_id

    def __enter__(self):
        return self

    def getEmail(self):
        return self.db.execute('SELECT email FROM client WHERE id=?', (id,)).fetchone()
