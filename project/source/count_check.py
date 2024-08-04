import sqlite3

def count_checker():
    conn = sqlite3.connect('../database/ratings.db')
    c = conn.cursor()
    result = c.execute('''
        SELECT count(*) from Ratings
    ''').fetchall()
    conn.close()
    return result


# def count_checker2():
#     conn = sqlite3.connect('../database/ratings.db')
#     c = conn.cursor()
#     result = c.execute('''
#         SELECT count(*) from RatingsMonthlyAggregates
#     ''').fetchall()
#     conn.close()
#     return result


if __name__ == '__main__':
    table_count = count_checker()
    print(table_count)
    # table_count2 = count_checker2()
    # print(table_count2)
