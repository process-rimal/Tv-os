import unittest

from tv_os import TVOS


class TestTVOS(unittest.TestCase):
    def test_boot(self):
        tv = TVOS()
        self.assertEqual(tv.boot(), "TV OS booted")
        self.assertTrue(tv.status()["powered_on"])

    def test_open_and_close_app(self):
        tv = TVOS()
        self.assertEqual(tv.open_app("YouTube"), "Opened YouTube")
        self.assertEqual(tv.close_app(), "Closed YouTube")
        self.assertEqual(tv.close_app(), "No app is currently open")

    def test_open_unknown_app_raises(self):
        tv = TVOS()
        with self.assertRaises(ValueError):
            tv.open_app("Unknown App")

    def test_change_channel_validation(self):
        tv = TVOS()
        self.assertEqual(tv.change_channel(101), "Changed to channel 101")
        with self.assertRaises(ValueError):
            tv.change_channel(0)
        with self.assertRaises(ValueError):
            tv.change_channel("10")


if __name__ == "__main__":
    unittest.main()
