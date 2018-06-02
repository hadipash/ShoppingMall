from DAOs.ClientDAO import ClientDAO


class ManageAccount:
    __client = None

    def __init__(self):
        self.__client = ClientDAO()

    def editPersonalInfo(self, client_id, new_info):
        ClientDAO().updatePersonalInfo(client_id, new_info)

    def requestPersonalInfo(self, client_id):
        return ClientDAO().getPersonalInfo(client_id)

    def deleteAccount(self, client_id):
        ClientDAO().removeClient(client_id)
