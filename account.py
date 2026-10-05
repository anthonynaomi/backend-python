class Account:
    def __init__(self, account_id, account_name):
        self.account_id = account_id
        self.account_name = account_name

    def get_account_info(self):
        return {
            "account_id": self.account_id,
            "account_name": self.account_name
        }