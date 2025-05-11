import pdfplumber
import spacy

def sentenceExtraction(pdfFilePath):
    
    print("PDF File Path: ", pdfFilePath)

    try:

        with pdfplumber.open(pdfFilePath) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        text = text.lower()

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents]
        
        return {
            "sentences": sentences,
            "error": "False"
        }

    except Exception as e:
        
        return {
            "message": str(e),
            "error": "True"        
        }
        


