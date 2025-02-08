
from src.config.transmodel import LoadModel


class Translator:
    def handle_request(self, request):
        loadmodel = LoadModel()
        return loadmodel.base(request)