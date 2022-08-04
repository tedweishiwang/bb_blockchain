import hashlib


def double_hash(raw):
    return hashlib.sha256(hashlib.sha256(raw.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()