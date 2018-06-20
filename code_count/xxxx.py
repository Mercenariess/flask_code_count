import hashlib
from settings import Config


def md5(arg):
    hash = hashlib.md5(Config.SALT)
    hash.update(bytes(arg,encoding='utf-8'))
    print(hash.update(bytes(arg,encoding='utf-8')))
    return hash.hexdigest()


pwd_md5 = md5('123')

print(pwd_md5)