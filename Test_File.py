#!/usr/bin/env python3
import unittest
from unittest.mock import patch
import ebayscraper
import datetime

"""
Create Test class that inheirits from unittest
"""


class TestScraper(unittest.TestCase):
    """
    create methon starting with word 'test_'
    """

    def test_average(self):
        # Test the calculateAverage function
        self.assertEqual(ebayscraper.calculateAverage([0, 10]), 5)

    def test_create_entry(self):
        # Test the create_entry function
        self.assertEqual(
            ebayscraper.create_entry(100),
            (["date", "price"], [str(datetime.date.today()), 100]),
        )
    def test_write(self):
        #Test the writeData function
        


#     def test_scrape(self):
#         with patch("ebayscraper.requests.get") as mocked_get:
#             mocked_get.return_value.ok = True
