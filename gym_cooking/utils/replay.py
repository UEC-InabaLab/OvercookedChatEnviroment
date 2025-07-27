import pickle
import time
import threading


class Replay:
    def __init__(self):
        self._d = {}
        self._d['dict'] = {} #注文や結果
        self._d['his'] = [] #作業ログ
        # his
        #  - 1
        #  - 2
        self._lock = threading.Lock()

    @classmethod
    def from_file(cls, filename):
        self = cls()
        self._d = pickle.load(open(filename, 'rb'))
        return self

    def save(self, filename):
        print(filename)
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self._d, f)
        except (OSError, pickle.PickleError) as e:
            print(f"エラー: ファイル '{filename}' に保存できませんでした: {e}")

    #self["key"] で辞書のデータを取得
    def __getitem__(self, item):
        return self._d['dict'][item]

    #self["key"] = value でデータを追加
    def __setitem__(self, key, value):
        with self._lock:
            self._d['dict'][key] = value

    def log(self, name: str, args: dict):
        with self._lock:
            self._d['his'].append(
                {'time': time.time(), 'name': name, 'args': args})

    def __iter__(self):
        return iter(self._d['his'])
    