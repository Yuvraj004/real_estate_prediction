import json
import pickle
import numpy as np
locs = None
data_columns=None
model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)

def get_location_names():
    return locs

def get_data_columns():
    return data_columns

def load_saved_artifacts():
    global data_columns
    global locs
    global model
    with open('./artifacts/columns.json') as j_file:
        #data is a dictionary
        data_columns = json.load(j_file)['data_columns']
        #we only want the data columns from the 3 value
        locs = data_columns[3:]
    
    with open('./artifacts/bengaluru_prices_model.pickle','rb') as f:
        model = pickle.load(f)
    

if __name__=="__main__":
    # load_saved_artifacts()
    # print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
