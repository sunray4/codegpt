import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained('ibm-granite/granite-3.1-8b-instruct')
    model = AutoModelForCausalLM.from_pretrained('ibm-granite/granite-3.1-8b-instruct')
    model.eval()
    
    chat = [
        {
            'role': 'user',
            'content': 'Please list one common name for boys in 2020.'
        },
    ]
    
    chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    
    input_tokens = tokenizer(chat, return_tensors='pt')
    output = model.generate(**input_tokens, max_length=100)
    
    output = tokenizer.batch_decode(output)
    
    print(output)