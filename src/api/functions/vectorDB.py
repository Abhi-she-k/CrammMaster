from qdrant_client import QdrantClient, models

def writeToQdrantDB(embeddings, fileName):

    try:

        qdrant_client = QdrantClient(

        )

        if(qdrant_client.collection_exists(collection_name="sentences")):
            
            qdrant_client.delete_collection(collection_name="sentences")
            
            qdrant_client.create_collection(
            collection_name="sentences",
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
        )
            
        for i in range(len(embeddings)):
            qdrant_client.upsert(
                collection_name="sentences",
                points=[{
                    "id": i,
                    "vector": embeddings[i].get("embedding"),
                    "payload": {
                        "text": embeddings[i].get("sentence"),
                        "fileName": fileName
                    }
                }]
            )

        print("Data written to Qdrant DB successfully.")

        return {
            "message": "Data written to Qdrant DB successfully.",
            "error": "False"        
        }
    
    except Exception as e: 

        return {
            "message": str(e),
            "error": "True"
        }

  
