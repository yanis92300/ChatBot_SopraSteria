import pickle

# Creation of pickle file to store all python objects which we'll use in the predictions process

def create_pickle(list, pkl_url):
    return pickle.dump(list, open(pkl_url, 'wb'))

def load_pickle(pkl_url):
    return pickle.load(open(pkl_url,'rb'))