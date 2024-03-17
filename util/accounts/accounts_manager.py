import json


class AccountsManager:

    @staticmethod
    def get_conta(tipo_conta):
        with open('./util/accounts/common_accounts.json') as arquivo:
            return json.load(arquivo)[tipo_conta]
