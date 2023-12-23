import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# CUDA 사용 가능 여부 확인
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/polyglot-ko-12.8b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/polyglot-ko-12.8b").to(device)

# Example text prompt
prompt = "{prompt: 너는 지금부터 인터넷 방송의 시청자의 역할이야. 이런 역할에 맞게 방송인의 이야기에 반응해줘.} {방송인: 오늘 날씨 좋다.} {시청자:}"

# Encode the prompt into tokens and convert to a PyTorch tensor
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

# Generate text using the model
output = model.generate(input_ids, max_length=256, num_return_sequences=1, temperature=0.7, do_sample=True)

# Decode the generated tokens back to text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated text
print(generated_text)
