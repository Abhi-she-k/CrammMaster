from fastapi import FastAPI
from functions.sentenceExtraction import sentenceExtraction
from fastapi.middleware.cors import CORSMiddleware
from os import listdir
from os.path import isfile, join

from functions.sentenceExtraction import sentenceExtraction

from functions.getSentenceVector import getSentenceVector


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # your Next.js frontend
)

# @app.get("/api/hello")
# def read_root():
#     return {"message": "Hello from FastAPI"}

# @app.get("/getSentences")
# def hello(pdfFilePath:str):
#     message = sentenceExtraction(pdfFilePath)
#     return {
#         "message": "hello"
#     }


@app.get("/learn")
def learn():
        
    path = 'C:/Users/abhis/Desktop/Projects/crammaster.ai/CramMaster/tmp/uploads'

    embeddingData = {}

    for file in listdir(path):
        if (isfile(join(path, file))):
            print(file)
            sentences = sentenceExtraction(join(path, file))

            fileVector = []

            for sentence in sentences:
            
                vector = getSentenceVector(sentence)
                fileVector.append(vector)

            embeddingData[file] = fileVector

    
    print(embeddingData.keys())


    # return {
    #     "":
    # }

