import configparser
import os
from flickrapi import FlickrAPI
from urllib.request import urlretrieve

KEYWORDS = ['rose', 'sunflower', 'lilium']
DATASET_DIR = './dataset/'
IMAGE_COUNT = 20

class Downloader:
    def __init__(self, config):
        self.flickr = FlickrAPI(config['flickr']['key'], config['flickr']['secret'], format='parsed-json')

    def search_images(self, keyword):
        res = self.flickr.photos.search(
            text=keyword,
            media='photos',
            sort='relevance',
            safe_search=1,
            per_page=IMAGE_COUNT,
            extras='url_q,license'
        )
        return res['photos']

    def download_images(self, photos, directory):
        try:
            for i, photo in enumerate(photos['photo']):
                url_q = photo['url_q']
                filepath = os.path.join(directory, photo['id'] + '.jpg')
                print('{:3d}: download {}'.format(i + 1, url_q))
                urlretrieve(url_q, filepath)
        except:
            import traceback
            traceback.print_exc()

    def run(self):
        for keyword in KEYWORDS:
            directory = os.path.join(DATASET_DIR, keyword)
            if not os.path.exists(directory):
                os.mkdir(directory)
            photos = self.search_images(keyword)
            self.download_images(photos, directory)


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    Downloader(config).run()


if __name__ == '__main__':
    main()
