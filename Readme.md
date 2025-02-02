# 📄 AI-Powered Document Summarization & Q&A 

**AI-powered document summarization and Q&A system** built using **Streamlit, Phidata, and OpenAI**.

## 🚀 Features
✅ Upload **PDF, DOCX, or TXT** documents  
✅ AI-powered **document summarization**  
✅ **Q&A on document content** using OpenAI  
✅ **Automated CI/CD deployment** from GitHub to **Streamlit Cloud**  
✅ Secure **API Key Handling** with **Streamlit Secrets Manager**  

---

## 📂 Project Structure
```sh
📂 summarize_docs
|    | 📂 backend 
|    │ │── 📄 init.py  
|    │ │── 📄 agents.py # Phidata AI Agents  
|    │ │── 📄 config.py 
|    │ │── 📄 document_processing.py 
|    │ 📂 frontend 
|    │ │── 📄 app.py 
|    │ 📂 .github 
|    │ │── 📂 workflows 
|    │      |── 📄 deploy.yml
|    │── 📂 uploads 
|    │── 📄 .env  
|    │── 📄 .gitignore 
|    │── 📄 README.md
|    │── 📄 requirements.txt 

```

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/sachinjoseph26/summarize_docs.git
cd ai-document-qa
```

### **2️⃣ Create a Virtual Environment**

```sh
python -m venv rag_env
source rag_env/bin/activate  # macOS/Linux
rag_env\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**
```sh
OPENAI_API_KEY=your-openai-api-key
```

### 🚀 Running the App Locally

```sh
streamlit run frontend/app.py
```

## 🌎 Deployment to Streamlit Cloud (CI/CD)

- The project includes a GitHub Actions workflow (.github/workflows/deploy.yml) that: 
    - ✅ Detects new commits to GitHub
    - ✅ Automatically deploys to Streamlit Cloud


## 📜 Tech Stack

- ### Frontend: Streamlit
- ### AI Processing: Phidata + OpenAI
- ### Deployment: GitHub Actions + Streamlit Cloud
