import unittest
from youtube import get_response, create_database


result = {'etag': '9xaVx5adTqgdEictDGYXcArH2vc',
 'items': [{'etag': 'tpZvdube5QSsIEMAiEDyEwHNZxo',
            'id': 'UCSofXQEbBHn12ucB45iTD3g',
            'kind': 'youtube#channel',
            'statistics': {'hiddenSubscriberCount': False,
                           'subscriberCount': '3120',
                           'videoCount': '16',
                           'viewCount': '204499'}}],
 'kind': 'youtube#channelListResponse',
 'pageInfo': {'resultsPerPage': 5, 'totalResults': 1}}

class TestFileName(unittest.TestCase):
    def test_get_response(self):
        self.assertEqual(get_response('FelixTechTips'), result)
'''
    def test_create_database(self):
        self.assertEqual(create_database(''), None)
        self.assertEqual(create_database(''), None)
'''


if __name__ == '__main__':
    unittest.main()
    