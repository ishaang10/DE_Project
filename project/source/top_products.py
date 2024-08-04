import sqlite3

def top_products():
    conn = sqlite3.connect('../database/ratings.db')
    c = conn.cursor()
    result = c.execute('''
        SELECT month, product_id, average_rating
        FROM (
            SELECT
                month,
                product_id,
                average_rating,
                ROW_NUMBER() OVER (PARTITION BY month ORDER BY average_rating DESC) as rank
            FROM
                RatingsMonthlyAggregates
        )
        WHERE rank <= 3
    ''').fetchall()
    conn.commit()
    conn.close()
    return result

if __name__ == '__main__':
    top_products = top_products()
    for out in top_products:
        print(out)
