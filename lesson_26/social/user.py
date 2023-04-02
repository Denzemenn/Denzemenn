import requests

class User:
    def __init__(self, fn="", ln="", log="", pas=""):
        self.__data = None
        self.data = requests.get("https://api.randomdatatools.ru/").json()
        self.fname = self.__data["FirstName"] if not fn else fn
        self.lname = self.__data["LastName"] if not ln else ln
        self.login = self.__data["Login"] if not log else log
        self.__pass = self.__data["Password"] if not pas else pas

    def log_in(self):
        if self.login == l and self.__pass == p:
            return True
