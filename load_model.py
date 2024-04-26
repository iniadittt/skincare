import pickle

def load_data(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data