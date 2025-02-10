#Language abbreviation - https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes

from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small", legacy=False)

class LoadModel:
    @staticmethod
    def base(request):
        text = f"translate {request.fromlang} to {request.tolang}: {request.content}"
        inputs = tokenizer(text, return_tensors="pt").input_ids

        output = model.generate(inputs, max_length=512)
        converted_output = tokenizer.decode(output[0], skip_special_tokens=True)

        return converted_output
    
    @staticmethod
    def engtohindi(request):
        return 'Helsinki-NLP/opus-mt-en-hi'