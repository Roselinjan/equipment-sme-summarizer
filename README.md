# ⚡ Wind Turbine Equipment SME Assistant

An AI-powered Equipment SME Assistant that helps field 
technicians and equipment experts analyze wind turbine 
incident reports and get intelligent answers using 
Generative AI.

## 🔗 Live Demo
https://equipment-sme-summarizer.streamlit.app

## ✨ Features

### 📄 Report Summarization
- Paste wind turbine incident logs
- Get instant AI-powered summary
- Powered by Amazon Bedrock (Nova Pro)
- Serverless architecture using AWS Lambda

### 💬 Contextual AI Chatbot
- Ask questions about the summarized report
- Conversation memory across messages
- Restricted to wind turbine topics only
- Powered by LangChain + Amazon Bedrock

## 🛠️ Tech Stack

| Layer | Service |
|---|---|
| Frontend | Streamlit |
| API Layer | AWS API Gateway |
| Compute | AWS Lambda |
| AI Model | Amazon Bedrock (Nova Pro) |
| Chatbot Framework | LangChain |
| Conversation Memory | LangChain ConversationSummaryBufferMemory |
| Monitoring | AWS CloudWatch |
| IAM | AWS IAM Roles |

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/roselinjan/equipment-sme-summarizer

# Navigate to project
cd equipment-sme-summarizer

# Create virtual environment
python -m venv venv
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure

# Run the app
streamlit run app.py
```

## 👩‍💻 Author
Roselin Janice
