class ProfileError(Exception):
    def __init__(self, code: str):
        self.code = code


class ProfileNotFoundError(ProfileError):
    def __init__(self, login: str):
        super().__init__(code)

    def __str__(self):
        return f"Profile {self.code} not found"


