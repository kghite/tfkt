import bcrypt


class Authenticator:

    @staticmethod
    def hash_password(pass_str) -> bytes:
        return bcrypt.hashpw(pass_str.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def verify_password(try_str, pass_hash) -> bool:
        return bcrypt.checkpw(try_str.encode('utf-8'), pass_hash)
