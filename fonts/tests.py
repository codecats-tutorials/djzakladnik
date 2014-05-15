from django.test import TestCase
from os.path import join, isfile
from zakladnik import settings

# Create your tests here.
class FontsTestCase(TestCase):
    def testFileExists(self):
        names = [
            'glyphicons-halflings-regular.ttf',
            'glyphicons-halflings-regular.svg',
            'glyphicons-halflings-regular.eot',
            'glyphicons-halflings-regular.woff'
        ]
        fontDir = join(settings.BASE_DIR ,'fonts' , settings.STATIC_URL[1:], 'fonts')

        for name in names:
            path = join(fontDir, name)
            self.assertGreater(len(open(path).read()), 1)

    def testFileNotExists(self):
        names = [
            'Glyphicons-halflings-regular.ttf',
            'Glyphicons-halflings-regular.svg'
        ]
        fontDir = join(settings.BASE_DIR ,'fonts' , settings.STATIC_URL[1:], 'fonts')

        for name in names:
            path = join(fontDir, name)
            self.assertFalse(isfile(path))
