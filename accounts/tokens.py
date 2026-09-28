from datetime import timedelta
from rest_framework_simplejwt.tokens import AccessToken

class PersistentAPIToken(AccessToken):
    # Override the default 30-minute lifetime to 1 year (or whatever you prefer)
    lifetime = timedelta(days=365)

    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        # Add a custom claim to distinguish this from regular login tokens
        token['token_type'] = 'access'
        return token
