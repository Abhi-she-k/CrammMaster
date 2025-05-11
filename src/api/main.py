from fastapi import FastAPI
from functions.sentenceExtraction import sentenceExtraction
from fastapi.middleware.cors import CORSMiddleware
from os import listdir
from os.path import isfile, join

from functions.sentenceExtraction import sentenceExtraction
from functions.getVectorEmbedding import getVectorEmbedding
from functions.vectorDB import writeToQdrantDB

from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/learn")
def learn():
        
    print("hello")

    path = 'C:/Users/abhis/Desktop/Projects/crammaster.ai/CramMaster/tmp/uploads'

    def processFile(file):

        if (isfile(join(path, file))):
            
            sentences = sentenceExtraction(join(path, file))

            if (sentences.get("error") == "True"):
                return {
                    "message": sentences.get("message"),
                    "status": "400"
                }

            fileEmbeddings = []

            for sentence in sentences.get("sentences"):
            
                vectorEmbedding = getVectorEmbedding(sentence)

                if (vectorEmbedding.get("error") == "True"):
                    return {
                        "message": vectorEmbedding.get("message"),
                        "status": "400"
                    }

                fileEmbeddings.append(vectorEmbedding)

            dbWrite = writeToQdrantDB(fileEmbeddings, file)

            if(dbWrite.get("error") == "True"):
                return {
                    "message": dbWrite.get("message"),
                    "status": "400"
                }
            
    with ThreadPoolExecutor() as executor:
        list(executor.map(processFile, [file for file in listdir(path)]))

    return {
        "message": "Learn Process Completed Successfully.",
        "status": "200"
    }
