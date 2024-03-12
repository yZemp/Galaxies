import pickle

def store(data, filename = "galaxies.pickle"):
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle, protocol = pickle.HIGHEST_PROTOCOL)

def load(filename = "galaxies.pickle"):
    with open(filename, 'rb') as handle:
        return pickle.load(handle)