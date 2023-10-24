import json
from gpt4all import GPT4All
with open('output.json', 'r') as json_file:
    data = json.load(json_file)
    data1 = data["Sub-Problem"]["question1"]
    data2 = data["Sub-Problem"]["answer1"]
    data3 = data["Sub-Problem"]["question2"]
    data4 = data["Sub-Problem"]["answer2"]

model = GPT4All(model_name='orca-mini-3b.ggmlv3.q4_0.bin')
prompt1 = f"""
        AI:{data1}
        Human:{data2}
        AI:{data3}
        Human:{data4}

        Summarize the text above in 50 words.

        
        Summarized Text:"""
output = model.generate(prompt=prompt1,temp=0, max_tokens=512)
print(output)


