# DE_Project
DE Project for Monthly average ratings and top products

## Steps to run 

You can just navigate to Source package where all the Python modules are.

Step 1 - Clone the repository in your local machine and install the dependencies using poetry 

``` poetry install ```

Step 2 - We must create a Ratings Database where our Tables will reside.Run data_gen.py in poetry which creates a Database if it does not exists and Ratings table if not exists

```poetry run python data_gen.py```

The data_gen.py will also add the required saample/randm data into the Ratings table.

Step 3 - Run compute_aggregates.py using poetry that will contain monthly average ratings for products and stores it in a table RatingsMonthlyAggregates.

```poetry run python compute_aggregates.py```

Step 4 - Run top_products.py which will list three top-rated products for every month of 2024 in RatingsMonthlyAggregates table created in previous step.

```poetry run python top_products.py```

Step 5 - After executing all the development modules it is time to run the unit tests.

```poetry run python -m unittest unit_tests/unit_tests.py```
