import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
import ollama
st.set_page_config(
    page_title="mini rag Q&A",
    page_icon="📚📚"
)
st.title("📚Mini Rag Q&A")
st.write("paste a document ,store it in chromaDB,and ask questions about it")
@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")
embedding_model = load_embedding_model()
client=chromadb.Client()
collection = client.get_or_create_collection(name="documents")
document=st.text_area(
    "📃 paste your document here",
    height=250,
    placeholder="paste your notes,article,syllabus,etc."
)
if st.button("➕Add Document"):
    if not document.strip():
        st.warning("please enter some text.")
    else:
        chunks=[
            document[i:i+50]
            for i in range(0,len(document),500)

        ]
        embeddings=embedding_model.encode(chunks)
        collection.add(
            ids=[f"chunk_{i}" for i in range(len(chunks))],
            documents=chunks,
            embeddings=embeddings.tolist()
        )
        st.success(f"Added{len(chunks)} chunk(s) to ChromaDB.")
question=st.text_input("❓Ask a question about your document")
if st.button("🔎 Ask AI"):
    if not question.strip():
        st.warning("please enter a question")
    elif collection.count()==0:
        st.warning("Please add a document first.")
    else:
        question_embedding=embedding_model.encode([question])[0]
        results=collection.query(
            query_embeddings=[question_enbedding.tolist()],
            n_result=min(3,collection.count())

        )
        retrived_chunks=result["documents"][0]
        context="\n\n".join(retrived_chunks)
        prompt=f"""
you are a helpful AI assistant.
answer the question only using the context below.
context:
{context}
Question:
{question}
if the answer is not present in the context,
asy "i don't know based on the provided document."
"""
        try:
            response = ollama.chat(
                model="llama3.2",
                meassages=[{"role":"user","content":prompt}]
            )
            st.subheader("🤖 Answer")
            st.write(response["message"]["content"])
            with st.expander("🔎 Retrieved context"):
                for i ,chunk in enumerate(retrieved_chunks):
                    st.write(f"**Chunk{i+1}:**")
                    st.write(chunk)
        except Exception as e:
            st.error(
                "could not connect ollama"
            )
            st.code(str(e))
st.divider()
st.caption("python+sentence transformer+Chromadb +OLLAMA+streamlit")

            