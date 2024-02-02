* GitHub Codespace

```www.github.com/features/codespaces```

* Download data from url into the parquet directory

```wget -P /workspaces/Data_Engineering_Zoomcamp/week_1_basic_setup/parquet/ https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet```

* command to run pgcli

```pgcli -h localhost -p 5432 -u postgres -d new_york_taxi ```

* install sqlalchemy, psycopg2 and python-dotenv libraries for establishing connection to database, read data from database, and interacting with environment variables respectively.

```pip install sqlalchemy psycopg2 python-dotenv```


SQL QUERIES
* Query to obtain maximum and min pickup_time `tpep_pickup_datetime`, and also maximum amount spent by a passenger `total amount`.
```
SELECT max(tpep_pickup_datetime), min(tpep_pickup_datetime), max(total_amount) FROM yellow_taxi_data;

``` 

* Select all content on `zones` table
```
SELECT * FROM zones;
```

* Select particular columns from the `yellow_taxi_data` and `zones`table by joining the tables.

```
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    zpu."Borough" + ' / ' + zpu."Zone" As "pick_up_loc",
    zdo."Borough" + ' / ' + zdo."Zone" AS "dropoff_loc"
FROM yellow_taxi_data t,
     zones zpu,
     zones zdo
WHERE
    t."PULocationID" = zpu."LocationID" AND
    t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```
Alternative query showing join implicitly.
```
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' / ', zpu."Zone") As "pick_up_loc",
    CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_loc"
FROM 
    yellow_taxi_data t JOIN zones zpu
        ON t."PULocationID" = zpu."LocationID"
    JOIN zones zdo
        ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

* Check table for rows where `PULocationID` is `NULL`
```
SELECT
    t.tpep_pickup_datetime,
    t.tpep_dropoff_datetime,
    t.total_amount,
    t."PULocationID",
    t."DOLocationID"
FROM 
    yellow_taxi_data t
WHERE
    "PULocationID" is NULL
LIMIT 100;
```

* Check if all locations have a pickup location `POLocationID` and dropoff location `DOLocationID`.

```
SELECT
    t.tpep_pickup_datetime,
    t.tpep_dropoff_datetime,
    t.total_amount,
    t."PULocationID",
    t."DOLocationID"
FROM 
    yellow_taxi_data t
WHERE
    "PULocationID" NOT IN (SELECT "LocationID" FROM zones)
LIMIT 100;
```

* 

```
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    DATE_TRUNC('DAY', tpep_dropoff_datetime)
    total_amount,
FROM 
    yellow_taxi_data t
LIMIT 100;

```

* Another query
```
SELECT
    CAST(tpep_dropoff_datetime AS DATE) as "day",
    "DOLocationID",
	COUNT(1) AS "count",
	MAX(total_amount),
	MAX(passenger_count)
FROM 
    yellow_taxi_data t
GROUP BY
	 1, 2 
ORDER BY "day" ASC, "DOLocationID" ASC;
```
NB: The `GROUP BY` command precedes the `ORDER BY` command, the `GROUP BY` command sorts a column in groups and the `ORDER BY` sort the provided either in ascending or descending order using the `GROUP BY` column as a control.