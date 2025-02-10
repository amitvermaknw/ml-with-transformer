from src.model.grammodel import LoadModel

class Grammar:
    def handle_request(self, request):
        loadmodel = LoadModel()
        return loadmodel.correct(request)
        