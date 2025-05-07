from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

def getSentenceVector(text, referenceSentence=False):
    

    if(referenceSentence):
        text = text.lower()

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        embedding = [model.encode(text.strip())]

        #QdrantClient stuff

        return embedding
    else:
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        embedding = model.encode(text.strip())

        return embedding



