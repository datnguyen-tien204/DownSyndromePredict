import pickle
def load_model(model_name):
    with open(f'{model_name}.pkl', 'rb') as file:
        print("a",file)
        data = pickle.load(file)
    return data
load_model("KNN")