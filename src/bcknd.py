import urllib3 as url3
import json
import shutil


class Loader:
    def __init__(self, url):
        self.url = url

    site_data = dict()
    manager = url3.PoolManager()

    # url = 'https://moodup.team/test/info.php'

    def load_data(self):
        resp = self.manager.request('GET', self.url)
        buf = resp.data.decode('utf-8')
        self.site_data = json.loads(buf)

    # TODO
    def show_picture(self, nr):
        picture_data = self.site_data['imgs'][nr]
        return picture_data

    # TODO
    def save_picture(self):
        return
