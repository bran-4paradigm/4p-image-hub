# -*- coding:utf-8 -*-

import base64
import six
import hashlib
import os


def decode_auth(auth):
    if isinstance(auth, six.string_types):
        auth = auth.encode('ascii')
    s = base64.b64decode(auth)
    login, pwd = s.split(b':', 1)
    return login.decode('utf8'), pwd.decode('utf8')


def check_contain_zh(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def md5hex(word):
    # MD5加密算法，返回32位小写16进制符号
    if isinstance(word, unicode):
        word = word.encode("utf-8")
    elif not isinstance(word, str):
        word = str(word)
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()


def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
    return myhash.hexdigest()
