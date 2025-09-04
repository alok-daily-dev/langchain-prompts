from langchain_google_genai import ChatGoogleGenerativeAI as ChatG
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatG(model = 'gemini-2.5-flash')

st.header('Reasearch Tool')
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

if st.button('Generate Explanation'):
    st.write("Generating explanation...")
