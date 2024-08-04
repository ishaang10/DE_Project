import unittest
import sqlite3
from source.data_gen import database_create,populate_data
from source.compute_aggregates import compute_monthly_aggregates
from source.top_products import top_products



class projectTest(unittest.TestCase):
    # def setUp(self):
    #     # Create and populate the database before each test
    #     database_create()
    #     populate_data()

    # def tearDown(self):
    #     # Clean up by removing the database after each test
    #     import os
    #     os.remove('database/ratings.db')

    def test_generate_data(self):
        # Ensure that data is populated
        conn = sqlite3.connect('../database/ratings.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM Ratings')
        count = c.fetchone()[0]
        conn.close()
        self.assertGreater(count, 0, "Database should have some ratings data")

    def test_compute_aggregates(self):
        compute_monthly_aggregates()

        # Ensure that aggregates are computed
        conn = sqlite3.connect('../database/ratings.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM RatingsMonthlyAggregates')
        count = c.fetchone()[0]
        self.assertGreater(count, 0, "Aggregates table should have some data")

        # # Optionally, check the correctness of aggregate values
        # c.execute('SELECT AVG(rating) FROM RatingsMonthlyAggregates')
        # average_rating = c.fetchone()[0]
        # self.assertIsNotNone(average_rating, "Aggregates table should have average ratings calculated")

        conn.close()

    def test_find_top_products(self):
        top_products_out = top_products()

        # Ensure correct top products are found
        self.assertIsInstance(top_products_out, list, "Top products should be a list")
        self.assertGreater(len(top_products_out), 0, "There should be some top products")

        # for product in top_products_out:
        #     self.assertIn('product_id', product, "Each top product should contain product_id")
        #     self.assertIn('average_rating', product, "Each top product should contain average_rating")
        #     self.assertIsInstance(product['product_id'], int, "product_id should be an integer")
        #     self.assertIsInstance(product['average_rating'], float, "average_rating should be a float")

if __name__ == '__main__':
    unittest.main()
