#!/usr/bin/env python3
import unittest
from zero import zero, set_output_immediately, set_trial_rename, clear_globals_for_unittests

version = "0.2.0"


# self.assertTrue(exp)
# self.assertEqual(a,b)
# self.assertContains(response, 'must supply test_name')
# self.assertRegex(response.content.decode('utf-8'), 'Test Passed: True')
# self.assertNotRegex(response.content.decode('utf-8'), 'delete id test')


def one_time_setup():
    set_output_immediately(False)
    set_trial_rename(True)


class Testzero(unittest.TestCase):
    def setUp(self):
        clear_globals_for_unittests()
        pass

    def tearDown(self):
        pass

    def test_initial_output(self):
        response = zero("test/set01")
        self.assertRegex(response, "Zero padding files")

    def test_files_in_correct_initial_state(self):
        response = zero("test/set01")
        self.assertRegex(response, "page1.pdf")
        self.assertRegex(response, "page2.pdf")
        response = zero("test/set02")
        self.assertRegex(response, "182_8a21_1")
        self.assertRegex(response, "id123_page1")
        self.assertRegex(response, "id532_page_1_1")
        response = zero("test/set03")
        self.assertRegex(response, r"set03/1")

    def test_page1(self):
        response = zero("test/set01")
        self.assertRegex(response, "page01.pdf")

    def test_page2(self):
        response = zero("test/set01")
        self.assertRegex(response, r"-> test/set01/page02.pdf")

    def test_page10(self):
        response = zero("test/set01")
        self.assertNotRegex(response, r"-> test/set01/page10.pdf")

    def test_files_scanned_count(self):
        response = zero("test/set01")
        self.assertRegex(response, r"3 files scanned")

    def test_files_zero_padded_count(self):
        response = zero("test/set01")
        self.assertRegex(response, r"2 files zero padded")

    def test_1_appears_twice(self):
        response = zero("test/set02")
        self.assertRegex(response, r"id123_page01")

    def test_number_in_middle_and_at_end(self):
        response = zero("test/set02")
        self.assertRegex(response, r"182_08a21_01")

    def test_two_page_numbers(self):
        response = zero("test/set02")
        self.assertRegex(response, r"id532_page_01_01")

    def test_single_digit_filename(self):
        response = zero("test/set03")
        self.assertRegex(response, r"set03/01")

    def test_print_summary(self):
        response = zero("test/set01")
        self.assertRegex(response, "files zero padded")


if __name__ == "__main__":
    one_time_setup()
    unittest.main()
