import pandas as pd
import pickle

def get_predictions(params, model):
    # get distances from start_location
    distances = get_trip_distance(PULocation=params['PULocation'])

    # create a small dataframe using the parameters passed in
    X_test_small = pd.DataFrame({key:[value]*len(distances) for key, value in params.items()} )
    X_test_small['trip_distance'] = distances['trip_distance'].values
    X_test_small = X_test_small.drop(['DOLocation',"PULocation"], axis = 1) 
    X_test_small.index = distances["DOLocationID"].values
    X_test_small = pd.get_dummies(X_test_small)
    
    # ensure the same columns as the model training
    empty_df = pd.DataFrame(columns=model.feature_names_in_)
    X_test = pd.concat([empty_df, X_test_small]).fillna(0)

    # return predictions
    preds = model.predict(X_test)
    output = {int(distances['DOLocationID'].values[i]):float(preds[i]) for i in range(len(preds))}
    return output

def get_trip_distance(PULocation):
    ids_to_distance_mapping = pd.read_csv("../Modelling/ids_to_distance_mapping.csv")
    distances = ids_to_distance_mapping[ids_to_distance_mapping['PULocationID'] == PULocation].drop('PULocationID', axis = 1)

    return distances