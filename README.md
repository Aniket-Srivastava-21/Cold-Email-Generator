# 🚀 Cold Email Generator using LangChain, Groq, and LLaMA 3.3 70B  

An intelligent **AI-powered cold email generator** that automates personalized outreach based on job openings.  
This project uses a **Retrieval-Augmented Generation (RAG)** pipeline to find your most relevant projects and craft tailored cold emails showcasing your portfolio — all through a simple **Streamlit web app**.  

---

## 🧠 Overview  

This project bridges the gap between your resume and job description by generating **customized cold emails** that highlight your most relevant work.  

Given a **job posting URL**, the app:  
1. Extracts job details.  
2. Searches your indexed projects stored in **ChromaDB**.  
3. Retrieves the most relevant projects using **semantic similarity search**.  
4. Generates a **personalized cold email** using **LLaMA 3.3 70B** accelerated with **Groq inference**.  

---

## ⚙️ Tech Stack  

| Component | Technology |
|------------|-------------|
| **Framework** | LangChain |
| **LLM** | LLaMA 3.3 70B (via Groq API) |
| **Vector Store** | ChromaDB |
| **Interface** | Streamlit |
| **Language** | Python |
| **Architecture** | Retrieval-Augmented Generation (RAG) |

---

## 🧩 Features  

✅ **Job-Aware Email Generation** – Tailors the email to each job description.  
✅ **Contextual Project Retrieval** – Uses embeddings to match the most relevant projects.  
✅ **High-Speed Inference** – Powered by **Groq** for lightning-fast text generation.  
✅ **User-Friendly Interface** – Built with **Streamlit** for an interactive experience.  
✅ **Modular & Extensible** – Easily adaptable to new models or use cases.  

---

## 🖥️ How It Works  

1. **Store Your Project Data**  
   - Project descriptions are embedded and stored in a **ChromaDB vector store**.  

2. **Input a Job Opening URL**  
   - The app parses the job details from the given link.  

3. **Retrieve Relevant Projects**  
   - LangChain retrieves similar projects using **embedding similarity search**.  

4. **Generate the Cold Email**  
   - The context is passed to **LLaMA 3.3 70B**, which generates a professional cold email.  

---

## 🧰 Installation  

```bash
# Clone this repository
git clone https://github.com/Aniket-Srivastava-21/Cold-Email-Generator.git
cd cold-email-generator

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Run the App
```bash
streamlit run app.py
```

After successful run, you should see something like this:

<img width="1913" height="646" alt="image" src="https://github.com/user-attachments/assets/bb581a24-7964-4e94-96e2-c5e0a8c51cc8" />


After you paste an url and hit submit, the processing starts and the generated email looks like this:

<img width="1904" height="960" alt="Screenshot 2025-11-02 150159" src="https://github.com/user-attachments/assets/0995db4e-21ed-4b4a-8de4-c775baa728c5" />
