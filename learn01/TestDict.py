import unittest

from learn01.learnUnitTest import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='bb')
        self.assertEquals(d.a,1)
        self.assertEquals(d.b,'bb')
        self.assertTrue(isinstance(d,Dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEquals(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty

