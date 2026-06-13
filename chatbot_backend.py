# NEW
from langchain.chains import ConversationChain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_aws import ChatBedrockConverse
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import PromptTemplate
import streamlit as st

def demo_chatbot():
    demo_llm = ChatBedrockConverse(
        model="amazon.nova-pro-v1:0",
        temperature=0.7,
        max_tokens=1000,
        region_name=st.secrets.get("AWS_DEFAULT_REGION", "ap-south-1"),
        aws_access_key_id=st.secrets.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=st.secrets.get("AWS_SECRET_ACCESS_KEY")
    )
    return demo_llm
    

def demo_memory():
    llm_data = demo_chatbot()
    memory = ConversationSummaryBufferMemory(llm=llm_data,max_token_limit=2000)
    return memory

def demo_conversation(input_text, memory, demo_llm, report_summary=None):
    # with open("debug.txt", "w") as f:
    #     f.write(f"report_summary: {report_summary}")
    prompt_template = """You are an expert Wind Turbine SME Assistant.

You can:
1. Answer general wind turbine related questions from your knowledge
2. Answer specific questions based on the uploaded report if provided
3. Politely decline non-wind turbine questions

If the user asks anything NOT related to wind turbines,
politely say: I am designed only for wind turbine related questions.

Current conversation:
{history}
Human: {input}
Assistant:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=prompt_template
    )

    if report_summary:
        full_input = f"""A wind turbine report has been uploaded. 
    Answer the following question using ONLY the report data below.
    Do NOT give generic answers. Be specific and concise.

    REPORT:
    {report_summary}

    QUESTION: {input_text}"""
    else:
        full_input = input_text

    chat = ConversationChain(
        llm=demo_llm,
        memory=memory,
        prompt=prompt,
        verbose=True
    )
    chat_reply = chat.invoke({
        "input": full_input,
        
    })
    return chat_reply['response']


# print("starting test..")
# memory = demo_memory()
# llm = demo_chatbot()
# response = demo_conversation("what is a large language model in ai", memory, llm)
# print(response)

# response2 = demo_conversation("what i asked you now", memory, llm)
# print(response2)