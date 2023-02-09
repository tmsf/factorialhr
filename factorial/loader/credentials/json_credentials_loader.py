import json

from .abstract_credentials import AbstractCredentials


class JsonCredentials(AbstractCredentials):

    def __init__(self, filename: str):
        super().__init__()

        self.filename = filename

        with open(filename, 'r') as f:
            settings = json.load(f)

            context = settings.get('user', {})
            self.email = context.get('email')
            self.password = context.get('password')

    def get_email(self) -> str:
        """Get email from json file to login to factorialhr

        :return: string
        """
        return self.email

    def get_password(self) -> str:
        """Get password from json file to login to factorialhr

        :return: string
        """
        return self.password
