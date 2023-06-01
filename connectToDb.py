from procesarText import procesarText

import pymysql
import PyPDF2
import io
import traceback

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="M@sterchief98",
    database="MEDICAL"
)

def process_document(document):
    try:
        id, nombre, documento = document
        nombre = str(nombre)
        data = io.BytesIO(documento)
        pdfReader = PyPDF2.PdfReader(data)
        text = ""
        for page in range(len(pdfReader.pages)):
            text += pdfReader.pages[page].extract_text()
        embeddings = procesarText(text)
        return (nombre, data, embeddings.tobytes())
    except Exception as e:
        traceback.print_exc()

# SQL statement to get the documents
statementGetDocuments = "SELECT id, nombre, documento FROM pdfMedicalDocuments"

# Create a cursor
mycursor = conn.cursor()
mycursor.execute(statementGetDocuments)
documents = mycursor.fetchall()
num_rows = mycursor.rowcount
print(f"{num_rows} rows returned from query.")



