import sqlite3

def compute_monthly_aggregates():
    conn = sqlite3.connect('../database/ratings.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS RatingsMonthlyAggregates AS
        SELECT
            strftime('%Y-%m', timestamp) as month,
            product_id,
            AVG(rating) as average_rating
        FROM
            Ratings
        GROUP BY
            month, product_id
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    compute_monthly_aggregates()
