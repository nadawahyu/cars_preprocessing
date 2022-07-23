import pandas as pd
import numpy as np
from helper.preprocessing import CategoricalFeatures
from sklearn import preprocessing
from sklearn.preprocessing import normalize

def feature_engineering(df):
    col_names = {"dateCreated": "ad_created",
                 "dateCrawled": "date_crawled",
                 "fuelType": "fuel_type",
                 "lastSeen": "last_seen",
                 "monthOfRegistration": "registration_month",
                 "notRepairedDamage": "unrepaired_damage",
                 "nrOfPictures": "num_of_pictures",
                 "offerType": "offer_type",
                 "postalCode": "postal_code",
                 "powerPS": "power_ps",
                 "vehicleType": "vehicle_type",
                 "yearOfRegistration": "registration_year"}
    df.rename(columns=col_names, inplace=True)

    # convert to datetime
    df[["ad_created", "date_crawled", "last_seen"]] = df[["ad_created", "date_crawled", "last_seen"]].astype('datetime64')

    pattern = r'\D' # anything non-digit

    # replace anything that matches the pattern and convert to integer
    df['price'] = df['price'].str.replace(pattern,'', regex=True).astype('int')

    # replace anything that matches the pattern and convert to integer
    df['odometer'] = df['odometer'].str.replace(pattern,'', regex=True).astype('int')

    # drop seller and offer type because the unique data comparison is too big
    df_transformed = df.drop(columns=['seller', 'offer_type'])
    df_transformed.head()

    # drop num of pics because it only contains 0
    df_transformed = df_transformed.drop(columns='num_of_pictures')
    df_transformed.head()

    # dropping name & postal code
    df_transformed = df_transformed.drop(columns=['name', 'postal_code'])
    df_transformed.head()

    # remove outliers
    df_transformed = df_transformed[(df_transformed['price'] >= 500) & (df_transformed['price'] <= 40000)]

    # fill null values in columns with categorical data with its mode
    contains_null = [i for i in df_transformed.columns if (df_transformed[i].isnull().sum()/df_transformed[i].isnull().count()*100 > 0)]
    for i in contains_null:
        df_transformed[i] = df_transformed[i].fillna(df_transformed[i].mode()[0])

    # normalize data
    col_num = ['power_ps', 'odometer']
    normalized_col = [preprocessing.normalize([df_transformed[i]]) for i in col_num]
    for i,j in enumerate(col_num):
        df_transformed[j] = normalized_col[i][0]
    
    # apply CategoricalFeatures() for categorical data
    cols = [c for c in df_transformed.columns if (df_transformed[c].dtype == "object")]
    cat_feats = CategoricalFeatures(df_transformed, categorical_features=cols, 
                                    encoding_type="one_hot", 
                                    handle_na=True)
    df_transformed = cat_feats.fit_transform()

    # apply CategoricalFeatures() for ordinal data
    ordinal_data = ['registration_year', 'registration_month', 'date_crawled', 'ad_created', 'last_seen']
    cat_feats = CategoricalFeatures(df_transformed,
                     ordinal_data,
                     'label',
                     handle_na=False)
    df_transformed = cat_feats.fit_transform()

    return df_transformed