from loader import dp
from .throttling import ThrottlingMiddleware
from .checker import Bro


if __name__ == 'middlewars':
    print("Throttling was set up : True")
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Bro())