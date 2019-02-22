import socket


class Resolver:
    """
    This is just a normal class, nothing fancy
    """
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


# Create a new instance of Resolver class
r = Resolver()
# Directly call the instance, not its member functions
print("r('google.com)", r("google.com"))
