from radicale.auth import BaseAuth
import hashlib
import sqlite3
import base64


class Auth(BaseAuth):
    def is_authenticated(self, user, password):
        if self.configuration.has_option("auth", "django_sqlite3_path"):
            path = self.configuration.get("auth", "django_sqlite3_path")
            self.logger.info(f"Using sqllite3: {path}")
            try:
                with sqlite3.connect(path) as conn:
                    cursor = conn.execute(f'SELECT * from auth_user where username=?', (user,))
                    rows = cursor.fetchall()
                    if len(rows) > 1:
                        # shouldn't happened
                        raise ValueError(f"Too much users for {user}")
                    elif len(rows) == 0:
                        raise ValueError(f'No such user {user}')
                    else:
                        cipher, iterations, salt, hash_orig = rows[0][1].split('$', 4)
            except Exception as e:
                self.logger.warning(e)
                return False
            else:
                hash_new = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), int(iterations))
                hash_new = base64.b64encode(hash_new).decode('ascii').strip()
                return hash_new == hash_orig
        else:
            self.logger.error('No sufficient configuration')
        return False
