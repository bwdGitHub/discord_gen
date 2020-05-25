from abc import ABC, abstractmethod
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class Transform(ABC):

    @abstractmethod
    def transform(self,str):
        pass

class Test_Transform(Transform):

    def transform(self,str):
        # simple transform - just reverse the input string.
        return str[::-1]

class GPT2_Transform(Transform):
    ''' Generates responses using the gpt2 language model.'''

    def __init__(self,
    max_length = 20,
    temperature = 1.0,
    top_k = 0,
    top_p = 0.9):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.max_length = max_length
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p

    def transform(self,str):
        enc = self.tokenizer.encode(str,add_special_tokens=False,return_tensors="pt")
        seq = self.model.generate(
            input_ids = enc,
            max_length = self.max_length+len(enc[0]),
            temperature = self.temperature,
            top_k = self.top_k,
            top_p = self.top_p,
            repetition_penalty = 1.0,
            do_sample = True,
            num_return_sequences = 1)

        if len(seq.shape)>2:
            seq.squeeze()
        gen = []
        for gen_seq in seq:
            gen_seq = gen_seq.tolist()
            text = self.tokenizer.decode(gen_seq,clean_up_tokenization_spaces = True)
            text = text[: None]
            tot_seq = (
                text[len(self.tokenizer.decode(enc[0],clean_up_tokenization_spaces=True)) :]
            )
            gen.append(tot_seq)
        return " ".join(gen)

class Compose_Transform(Transform):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def transform(self,str):
        return self.T2.transform(self.T1.transform(str))

class Postprocessor(Transform):
    def transform(self,str):
        lastperiod = str.rfind(".")
        end = len(str) if lastperiod==-1 else lastperiod+1
        return str[:end]