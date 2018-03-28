# -*-coding:utf-8-*-
import os
import shelve
import traceback


class DataStorage():

    def __init__(self):
        self.storage_file = "data/storage"
        # is_existed = os.path.exists(self.storage_file)
        # if (is_existed):
        #     os.mknod(self.storage_file)

    def store(self, data):
        dbase = None
        try :
            dbase = shelve.open(self.storage_file)
            list = dbase.get('list')
            if list is None:
                list = []
            list.append(data)
            dbase['list'] = list
        except Exception:
            str = traceback.format_exc()
            print(str)
        finally:
            if dbase is not None:
                dbase.close()

    def retrieve(self):
        dbase = shelve.open(self.storage_file)
        list = dbase.get('list')
        if list is None:
            return []
        return list

    def remove(self, index):
        dbase = shelve.open(self.storage_file)
        list = dbase['list']
        del list[index]
        dbase.close()

    def remove_by_obj(self, obj):
        dbase = shelve.open(self.storage_file)
        list = dbase['list']
        list.remove(obj)
        dbase.close()


if __name__ == "__main__":
    data_storage = DataStorage()
    data = {
        'url': 'https://item.jd.com/4749506.html',
        'target_price': 2000
    }
    data_storage.store(data)

    data = data_storage.retrieve()
    print("data: ", data)