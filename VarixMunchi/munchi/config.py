import toml


class Config:
    def __init__(self):
        self._config = toml.load('./config.toml')

    @property
    def token(self):
        return self._config.get('token', None)

    @property
    def giphy_token(self):
        return self._config.get('giphy_token', None)

    @property
    def guilds(self):
        return self._config.get('guild_ids', None)
