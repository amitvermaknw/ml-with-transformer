from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained('vennify/t5-base-grammar-correction')
tokenizer = T5Tokenizer.from_pretrained('vennify/t5-base-grammar-correction')

class LoadModel:
    @staticmethod
    def correct(request):
        input = f'grammer: {request.content}'
        input_ids = tokenizer.encode(input, return_tensors='pt')

        output = model.generate(input_ids, max_length=512, early_stopping=True)
        correct_output = tokenizer.decode(output[0], skip_special_tokens=True)

        return correct_output