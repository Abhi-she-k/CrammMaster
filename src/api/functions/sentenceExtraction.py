import pdfplumber
import spacy

def sentenceExtraction(pdfFilePath):
    
    print("PDF File Path: ", pdfFilePath)

    nlp = spacy.load("en_core_web_sm")

    with pdfplumber.open(pdfFilePath) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()


    text = text.lower()
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    return sentences


