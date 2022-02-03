import streamlit as st
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


class StreamlitApp:
    VERSION = '0.1'
    TITLE = f"Ada Support Tool V{VERSION}"

    def __init__(self):
        st.set_page_config(
            **{
                "page_title": self.TITLE,
                "page_icon": ":robot:",
                "layout": "wide",
            }
        )

        model_name = 'tuner007/pegasus_paraphrase'
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        #self.tokenizer = PegasusTokenizer.from_pretrained(model_name)
        #self.model = PegasusForConditionalGeneration.from_pretrained(model_name).to(self.torch_device)

    def paraphrase_generator(self):
        num_beams = 10
        num_return_sequences = 10
        max_length = 60
        temperature= 1.5
        
        input_text = st.text_input("Sentence:", value="How do I make a deposit?")
        #batch = self.tokenizer([input_text], truncation=True, padding='longest', max_length=max_length, return_tensors="pt").to(self.torch_device)
        #translated = self.model.generate(**batch,max_length=max_length, num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=temperature)
        #tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        #st.write(tgt_text)

    def main(self):
        st.sidebar.title("Navigation")
        pages = {
            "Paraphrase Generator": self.paraphrase_generator
        }
        page = st.sidebar.radio("Go to", list(pages.keys()))
        pages[page]()


if __name__ == "__main__":
    app = StreamlitApp()
    app.main()
