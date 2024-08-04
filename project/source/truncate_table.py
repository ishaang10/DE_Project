import sqlite3

def truncate_Ratings():
    conn = sqlite3.connect('../database/ratings.db')
    c = conn.cursor()
    c.execute('''
        Delete From Ratings
    ''')
    conn.commit()
    conn.close()

def Drop_RatingsMonthlyAggregates():
    conn = sqlite3.connect('../database/ratings.db')
    c = conn.cursor()
    c.execute('''
        DROP Table if exists RatingsMonthlyAggregates
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    truncate_Ratings()
    print("Ratings Table Truncated successfully..!!")
    Drop_RatingsMonthlyAggregates()
    print("RatingsMonthlyAggregates Table Droped successfully..!!")

