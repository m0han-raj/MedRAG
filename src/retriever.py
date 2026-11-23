from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")
vector_store = Chroma(
    persist_directory="chroma_index", embedding_function=embedding_model
)
retriever = vector_store.as_retriever()
