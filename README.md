# car_django_db_test

## Prerequisites
- Docker
- Python 3.12
- Pipenv

---

## Project Setup

1. **Clone the repository**  
    ```
    git clone https://github.com/NathanJMF/car_django_db_test.git
    cd car_django_db_test
    ```

2. **Create a `.env` file** in the root of the project directory with the following structure:  
    ```
    GLOBAL_TEST_FLAG=true
    DJANGO_SECRET=your_django_secret
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    ```

3. **Start the PostgreSQL database**  
    Make sure the Docker Engine is running, then use the provided `docker-compose.yml` file to spin up the database:  
    ```
    docker-compose up -d
    ```

4. **Set up the virtual environment using Pipenv**  
    ```
    pipenv shell
    pipenv install
    ```

5. **Run migrations to set up the database structure**
    ```
    python manage.py migrate
    ```
   
6. **Run dummy data generation to populate the database**
    ```
    python manage.py generate_dummy_data
    ```
   
7. **Run the test script**
    ```
    python query_execution_time_test_script.py
    ```


## Car Retrieval Results
### Introduction
In this exercise, we explored several ways to retrieve and return ```Car``` data along with its related ```Owner``` and 
```CarBrand``` entries. The goal was to find the most efficient approach to this function when operating with 1 million 
Car rows.
### Naive Approach
The original naive approach provided has some issues when it comes to performing well at scale.
When using ```.objects.all()``` we are running unnecessary queries each time we access the ```Owner``` or ```Brand``` 
objects. Ontop of this, Python/Django will create and load every Object into memory.

### Join Approach
Uses ```Car.objects.select_related('brand', 'owner')``` so that related objects are fetched in a single query.

### Join + Reduced Key
Uses ```select_related``` but the return data is keyed by ```car.id``` instead of the ```Car``` object, attempting to reduce 
overhead.

### Join + Reduced Values
Uses ```select_related``` plus ```.only(...)``` to retrieve a subset of columns, eliminating unnecessary fields from the
query.

### Join + Reduced Key + Reduced Values
Combines the two above tactics and returns data keyed by ```car.id```, while retrieving only the necessary columns.

### No ORM Objects
Uses ```Car.objects.select_related(...).values(...)``` so Django returns raw dictionaries only containing the columns we
require rather than full objects instances.

### Performance Results (Last Recorded Times)

| Approach                             | 10K Cars | 1M Cars |
|--------------------------------------|----------|---------|
| Naive                                | 14.36s   | N/A*    |
| Join                                 | 0.17s    | 16.41s  |
| Join + Reduced Keys                  | 0.14s    | 17.85s  |
| Join + Reduced Values                | 0.11s    | 14.61s  |
| Join + Reduced Keys + Reduced Values | 0.12s    | 16.72s  |
| No ORM objects                       | 0.02s    | 1.72s   |
```* For 1,000,000 cars, the naive approach was abandoned due to extremely long execution time.```

### Conclusion
Overall, the Naive approach is impractical at large scale due to excessive queries and object instantiation.
Simply adding ```select_related``` (```Join Approach```) provides a significant performance boost and looks to be a reasonable 
default for moderate dataset sizes.
This could be further refined by reducing the number of fetched columns (```Join + Reduced Values```) leading to 
additional minor gains when measuring execution time.
However, when trying to use the Car ID for the dictionary keys over Car objects (```Join + Reduced Keys``` or 
```Join + Reduced Keys + Reduced Values```) in an attempt to reduce overhead, we observe worse performance than using 
just ```Join + Reduced Values```, especially when attempting 1M entries.
For datasets in the millions of rows, the ```No ORM Objects``` approach, returning dictionaries via ```.values(...)```, 
outperforms all others because it bypasses model instantiation entirely and does not perform any unnecessary queries.

Ultimately, the best method depends on both the size of the dataset and whether access to Django model features are 
required. For situations where Django model objects aren't required, returning dictionaries is the most efficient 
strategy.
