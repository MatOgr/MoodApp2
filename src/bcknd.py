import urllib3 as url3
import json
import shutil
from PIL import Image, ImageDraw
from io import BytesIO
import os
import numpy as np


class Loader:
    site_data = dict()
    manager = url3.PoolManager()
    SAVE_FOLDER = ''
    # url = 'https://moodup.team/test/info.php'

    def __init__(self, url):
        self.url = url
        self.load_data()
        for i in range(len(self.site_data['imgs'])):
            if self.find('%d.png' % i):
                self.get_image(i)
                #print('Pobiram')

    # ladowanie danych z podanego adresu - do slownika
    def load_data(self):
        resp = self.manager.request('GET', self.url)
        buf = resp.data.decode('utf-8')
        self.site_data = json.loads(buf)

    # pobranie zdjecia do uzytku w aplikacji / lub do pamieci
    def get_image(self, nr, save=False):
        address = self.site_data['imgs'][nr]
        resp = self.manager.request('GET', address)
        img = Image.open(BytesIO(resp.data))
        if save:
            try:
                img.save('%s/%s' % ('./res', address.split('/')[-1]))
                return 'Zapisano obraz'
            except:
                return 'Nie udalo sie zapisac obrazu'
        else:
            if nr == 0:
                img = self.cut_image(img)
            if not os.path.exists('./res'):
                os.makedirs('./res')
            img.save('./res/%d.png' % nr)

    # wytnij kolo ze zdjecia - do Circular button
    def cut_image(self, img):
        np_img = np.array(img)
        h, w = img.size
        dim = min(h, w)
        alpha = Image.new('L', (h, w), 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([(h-dim)/2, (w-dim)/2, (h+dim)/2, (w+dim)/2], 0, 360, fill=255)
        np_alpha = np.array(alpha)
        np_to_save = np.dstack((np_img, np_alpha))
        return Image.fromarray(np_to_save)

    # getter danych ze slownika
    def get_data_content(self, data):
        return self.site_data[data]

    # getter kluczy slownika
    def get_data_key(self, nr):
        return self.site_data.keys()[nr]

    #
    def get_from_list(self, what, point=None):
        s = self.site_data[what]
        if point is None:
            return ''.join(['%d. %s \n\n' % (i, x) for i, x in enumerate(s, 1)])
        return '\n'.join(['%s %s' % (point, x) for x in s])

    def find(self, name):
        for root, dirs, files in os.walk('./res'):
            if name not in files:
                return True
        return False

    # for tests
    def say_hello(self, nr):
        print('Hello %d' % nr)