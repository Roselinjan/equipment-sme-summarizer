import streamlit as st
import requests
import json
from chatbot_backend import demo_chatbot, demo_memory, demo_conversation

# Initialize session state for chatbot

if 'memory' not in st.session_state:
    st.session_state['memory'] = demo_memory()

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

 
st.set_page_config(page_title="Wind Turbine SME Assistant | Enterprise", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {font-family: 'Inter', sans-serif;}
    .main {background-color: #f8fafc;}
    .stTextArea textarea {font-size: 15px; border-radius: 8px; border: 2px solid #e2e8f0; padding: 12px;}
    .stTextArea textarea:focus {border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,0.1);}
    .stButton button {background-color: #3b82f6; color: white; border-radius: 8px; 
                      padding: 10px 32px; font-weight: 600; border: none; 
                      transition: all 0.2s; font-size: 15px;}
    .stButton button:hover {background-color: #2563eb; box-shadow: 0 4px 12px rgba(59,130,246,0.3);}
    
    .header-container {background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
                       padding: 40px; border-radius: 12px; margin-bottom: 30px;
                       box-shadow: 0 4px 6px rgba(0,0,0,0.07);}
    .header-title {color: white; font-size: 2.5em; font-weight: 700; margin: 0; letter-spacing: -0.5px;}
    .header-subtitle {color: #dbeafe; font-size: 1.1em; margin-top: 8px; font-weight: 500;}
    
    .metric-card {background: white; padding: 24px; border-radius: 10px;
                  box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 4px solid;
                  transition: all 0.2s;}
    .metric-card:hover {box-shadow: 0 4px 12px rgba(0,0,0,0.15); transform: translateY(-2px);}
    .metric-icon {font-size: 2.5em; margin-bottom: 8px;}
    .metric-title {color: #1e293b; font-size: 1em; font-weight: 600; margin: 0;}
    .metric-desc {color: #64748b; font-size: 0.85em; margin-top: 4px;}
    .card1 {border-left-color: #3b82f6;}
    .card2 {border-left-color: #10b981;}
    .card3 {border-left-color: #8b5cf6;}
    
    .query-section {background: white; padding: 32px; border-radius: 10px;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin: 20px 0;}
    .section-label {color: #1e293b; font-size: 0.95em; font-weight: 600; margin-bottom: 8px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='header-container'>
    <div class='header-title'>⚡ Wind Turbine Equipment SME Assistant</div>
    <div class='header-subtitle'>Enterprise AI-Powered Expert System for Predictive Maintenance & Downtime Reduction</div>
</div>
""", unsafe_allow_html=True)

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.markdown("""
    <div class='metric-card card1'>
        <div class='metric-icon'>🔧</div>
        <div class='metric-title'>Equipment Diagnostics</div>
        <div class='metric-desc'>Real-time fault detection</div>
    </div>
    """, unsafe_allow_html=True)
with metric_col2:
    st.markdown("""
    <div class='metric-card card2'>
        <div class='metric-icon'>⏱️</div>
        <div class='metric-title'>Reduce Downtime</div>
        <div class='metric-desc'>Minimize operational losses</div>
    </div>
    """, unsafe_allow_html=True)
with metric_col3:
    st.markdown("""
    <div class='metric-card card3'>
        <div class='metric-icon'>🤖</div>
        <div class='metric-title'>AI-Powered Insights</div>
        <div class='metric-desc'>Predictive maintenance</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='query-section'>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📄 Summarize Report", "💬 Chat with SME"])
with tab1:
    st.markdown("<div class='section-label'>Equipment Query</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        prompt = st.text_area("Equipment Logs", height=120, placeholder="Paste the Equipment Logs...", label_visibility="collapsed")
        
        if st.button("Summarize"):
            if prompt:
                with st.spinner("Analyzing equipment data..."):
                    try:
                        response = requests.post(
                            "https://zz1qqaigii.execute-api.ap-south-1.amazonaws.com/prod/summarize",
                            json={"prompt": prompt}
                        )
                        
                        if response.status_code == 200:
                            response_data = response.json()
                            if isinstance(response_data, dict) and "body" in response_data:
                                result = json.loads(response_data["body"])
                            else:
                                result = response_data
                            
                            st.markdown("<div style='margin-top: 24px;'><div style='color: #1e293b; font-weight: 600; margin-bottom: 12px;'>Expert Analysis:</div></div>", unsafe_allow_html=True)
                            st.markdown(f"<div style='background: #f8fafc; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; color: #334155; line-height: 1.6;'>{result}</div>", unsafe_allow_html=True)
                            st.session_state['report_summary']=result
                            #st.write(f"Stored type: {type(st.session_state['report_summary'])}")
                        else:
                            st.error(f"System Error: Unable to process request (Status: {response.status_code})")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter an equipment query to proceed")

    st.markdown("</div>", unsafe_allow_html=True)
with tab2:

    st.markdown("<div class='query-section'>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Chat with SME Assistant</div>", unsafe_allow_html=True)

   

    # Display chat history

    for message in st.session_state['chat_history']:

        with st.chat_message(message['role']):

            st.write(message['content'])

    #st.write(st.session_state.get('report_summary', 'NO SUMMARY FOUND'))

    # Chat input

    user_input = st.chat_input("Ask a question about equipment...")

   

    if user_input:

        # Add user message to history

        st.session_state['chat_history'].append({

            'role': 'user',

            'content': user_input

        })

       

        # Get response from chatbot

        with st.spinner("Thinking..."):

            llm = demo_chatbot()

            response = demo_conversation(

                user_input,

                st.session_state['memory'],

                llm,
                st.session_state.get('report_summary','')

            )

       

        # Add AI response to history

        st.session_state['chat_history'].append({

            'role': 'assistant',

            'content': response

        })

       

        # Rerun to show new messages

        st.rerun()

   

    st.markdown("</div>", unsafe_allow_html=True)