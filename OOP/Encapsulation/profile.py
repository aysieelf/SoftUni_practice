class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        if 5 <= len(value) <= 15:
            self._username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        if (len(value) >= 8 and
                any(ch.isupper() for ch in value) and
                any(ch.isdigit() for ch in value)):
            self._password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'

