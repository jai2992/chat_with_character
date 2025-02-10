import streamlit as st
import os
import json
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage


os.environ['GROQ_API_KEY']=st.secrets["GROQ_API_KEY"]

llm = ChatGroq(model="llama-3.3-70b-versatile")




def load_char():
    with open('characters.json','r') as json_file:
        data=json.load(json_file)
    return data
def save_char(new_data):
    with open('characters.json','r+') as json_file:
        data=json.load(json_file)
        data.insert(0,new_data)
        json_file.seek(0)
        json.dump(data,json_file)
with st.sidebar:
    new_char_name = st.text_input("enter the character name")
    new_char_des = st.text_area("enter the character description")


    if st.button("save"):
        new_char = {"name":new_char_name,"desc":new_char_des}
        save_char(new_char)


data = load_char()
char_name = st.selectbox(label="character", options=[x['name'] for x in data])
char_desc=[x['desc'] for x in data if x['name']==char_name][0]



history=[]
history.append(HumanMessage(content=f"""You are about to take on the role of a specific character. Your responses should be consistent with the characteristics, skills, personality traits, and behaviors of the character as described below. You should use the information to accurately represent the character’s style, tone, and responses in a way that aligns with the context provided.
                            Character name : {char_name}
                            Character description : {char_desc}
                            use only english
                            Always stay true to the character's traits, background, and motivations.
Do not break character or respond in a way that would be inconsistent with their personality.
Incorporate any relevant details about their abilities or past experiences into the conversation when needed.
If the conversation requires advice or a decision, consider how the character would act based on their worldview, skills, and goals.
If the character speaks in a specific tone or manner, mimic that speech style in every response.
                            """))


st.header(f"Chat with {char_name}")
st.write(f"Character description : {char_desc}")


user_input = st.chat_input("chat here")
if user_input:
    if user_input:
        history.append(HumanMessage(content=user_input))
        response = llm.invoke(history)
        history.append(AIMessage(content=response.content))

for message in history[1:]:
    if isinstance(message, HumanMessage):
        st.write(f"You: {message.content}")
    elif isinstance(message, AIMessage):
        st.write(f"Character: {message.content}")