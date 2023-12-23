import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Generate text from a prompt using a language model.")
parser.add_argument('prompt', type=str, help='The prompt to feed to the language model')

# Parse the arguments
args = parser.parse_args()

# CUDA 사용 가능 여부 확인
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/polyglot-ko-5.8b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/polyglot-ko-5.8b").to(device)

# Use the provided prompt
prompt = args.prompt

# Encode the prompt into tokens and convert to a PyTorch tensor
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

# Generate text using the model
output = model.generate(input_ids, max_length=256, num_return_sequences=1, temperature=0.7, do_sample=True)

# Decode the generated tokens back to text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated text
print(generated_text)
