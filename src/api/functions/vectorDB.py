from qdrant_client import QdrantClient, models

def writeToQdrantDB(embeddings, fileName):

    try:

        qdrant_client = QdrantClient(
                url="https://42fe4619-4c3a-47cf-949c-bacc1592c62e.us-west-1-0.aws.cloud.qdrant.io:6333",
                api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.PG80eZa1mZVjl6JhTEpVumAyHTTQFn_0Z_OCNikjhoY",
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

  
