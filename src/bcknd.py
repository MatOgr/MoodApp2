import urllib3 as url3
import json
import shutil


class Loader:
    site_data = dict()
    manager = url3.PoolManager()
    # url = 'https://moodup.team/test/info.php'

    def __init__(self, url):
        self.url = url
        self.load_data()

    def load_data(self):
        resp = self.manager.request('GET', self.url)
        buf = resp.data.decode('utf-8')
        self.site_data = json.loads(buf)

    def get_data_content(self, data):
        return self.site_data[data]

    def get_data_key(self, nr):
        return self.site_data.keys()[nr]

    def get_from_list(self, what, point=None):
        s = self.site_data[what]
        if point is None:
            return ''.join(['%s ' % x for x in s])
        return '\n'.join(['%s %s' % (point, x) for x in s])

    # TODO
    def show_picture(self, nr):
        picture_data = self.site_data['imgs'][nr]
        return picture_data

    # TODO
    def save_picture(self):
        return
