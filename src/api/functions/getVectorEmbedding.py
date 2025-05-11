from sentence_transformers import SentenceTransformer
# from qdrant_client.models import VectorParams, Distance

def getVectorEmbedding(text):

    try:

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        embedding = model.encode(text.strip())
        return {
            "sentence": text,
            "embedding": embedding,
            "error": "False"
        }
    
    except Exception as e:

        return {
            "message": str(e),
            "error": "True"
        }
    





