# this is a simple repo for assignment in wrangling data

# objectives
- rename columns into snake_case
- change column type containing dates into `datetime64`
- change numerical column into `int`
- drop a few columns which have:
    - imbalanced ratio
    - empty numerical column
    - unique element in each row
- remove outliers in the column 'price' which values are below 500 or above 40000
- data imputation for rows with NaN:
    - columns with dtype('object') will be replaced with its mode
    - columns with dtype('int') or dtype('float') will be replaced with its median (side note: there's none)
- normalize to all numerical columns except 'price'
    - columns: power_ps, odometer
- encoding
    - for categorical data: with one hot encoding
    - for ordinal data: with label encoding