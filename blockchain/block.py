import datetime
import hashlib


class Block:

    def __init__(self, data, previous_hash=0):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):

        sha = hashlib.sha256()
        data_string = str(self.data)

        hash_string = data_string.encode('utf-8')
        sha.update(hash_string)

        return sha.hexdigest()
