from DAOs.ClientDAO import ClientDAO


class ManageAccount:
    __client = None

    def __init__(self):
        self.__client = ClientDAO()

    def editPersonalInfo(self, client_id, new_info):
        self.__client.updatePersonalInfo(client_id, new_info)

    def requestPersonalInfo(self, client_id):
        return self.__client.getPersonalInfo(client_id)

    def deleteAccount(self, client_id):
        self.__client.removeClient(client_id)
