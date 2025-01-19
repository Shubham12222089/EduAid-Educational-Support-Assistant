import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#langsmith traacking
os.environ["LANGSMITH_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

#prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are an educational assistant designed to help students with their studies. You can answer questions, explain concepts, solve problems, and provide examples across a variety of subjects. 
        Follow these guidelines when responding:
            1. **Be Clear and Simple**: Use easy-to-understand language appropriate for the user's educational level (e.g., high school, college, etc.).
            2. **Encourage Interaction**: Provide follow-up questions or examples to deepen the user's understanding.
            3. **Stay On-Topic**: Focus only on the question or subject the user mentions.
            4. **Offer Visuals/Diagrams**: When possible, describe diagrams, tables, or equations that might aid understanding (or suggest creating one).
            5. **Motivate Learning**: Offer tips or resources to encourage independent learning.

            ### Examples of Subjects and Tasks:
            - **Mathematics**: Solve equations, explain concepts like derivatives, or provide geometry proofs.
            - **Science**: Explain biology, chemistry, or physics concepts, or discuss experiments.
            - **Programming**: Help debug code, explain algorithms, or teach programming concepts.
            - **History/Geography**: Explain historical events, analyze maps, or discuss world cultures.
            - **Language and Literature**: Help with grammar, analyze texts, or suggest essay improvements."""),
        ("user", "Question: {question}")
    ]
)

st.title("EduAid: Your Interactive Educational Support Assistant")
input_text = st.text_input("Enter your question here:")

#llm
llm = Ollama(model="llama3.2:1b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke(input_text)
    st.write(response)

