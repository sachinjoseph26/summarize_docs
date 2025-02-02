from phi.agent import Agent
from phi.model.openai import OpenAIChat
from backend.config import Config

# Initialize OpenAI Model for Phidata
openai_model = OpenAIChat(api_key=Config.OPENAI_API_KEY, model="gpt-4-turbo")

# Summarization Agent
summarization_agent = Agent(
    name="SummarizationAgent",
    role="Summarizes documents concisely",
    model=openai_model,
    instructions=["Provide structured summaries with bullet points.", "Limit summaries to 200 words."],
)

def summarize_text(document_text):
    """Summarize the extracted text using the Phidata AI agent."""
    response = summarization_agent.run(
        messages=[
            {"role": "system", "content": "You are an AI assistant that summarizes documents."},
            {"role": "user", "content": f"Summarize this document: {document_text[:4000]}"}  # Limit input
        ]
    )
    return response  # Return the summary

# Q&A Agent (Phidata-based)
qa_agent = Agent(
    name="QAAgent",
    role="Answer questions based on document content",
    model=openai_model,
    instructions=["Use the document text to answer questions accurately.", "Provide direct answers without extra information."],
)

def ask_question(document_text, user_question):
    """Answer user questions using the extracted document text."""
    response = qa_agent.run(
        messages=[
            {"role": "system", "content": "You are an AI that answers user questions based on a document."},
            {"role": "user", "content": f"Based on this document: {document_text[:4000]}, answer: {user_question}"}
        ]
    )
    return response  # Return the answer
