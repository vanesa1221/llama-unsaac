from datasets import load_dataset

dataset = load_dataset('text', data_files='data/datos_unsaac.txt')
dataset.push_to_hub('vanesa1221/llama-prueba-unsaac')
