import pymysql
import numpy as np
from procesarText import procesarText
from sklearn.metrics.pairwise import cosine_similarity
from getResultsIntoCSV import saveResults


def getEmbeddingsFromdb():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Lychk@ng1998",
        database="MEDICAL"
    )

    query = "SELECT nombre, embeddings FROM MedicalDocumentsEmbedded"

    mycursor = conn.cursor()

    mycursor.execute(query)

    num_rows = mycursor.rowcount
    print(f"{num_rows} rows returned from query.")

    results = mycursor.fetchall()
    names = [row[0] for row in results]
    embeddings = [list(map(float, row[1].split(','))) for row in results]

    # Create the numpy array with the specified dimensions
    array = np.array(embeddings)

    # Reshape the array to (11, 300)
    array = array.reshape(11, 300)

    conn.close()

    return names, array


def similarities(prompt, comparationMatrix, names):
    promptEmbeddings = procesarText(prompt)
    promptEmbeddings = promptEmbeddings.reshape(1, -1)
    comparationMatrix = comparationMatrix.reshape(-1, 300)  # Reshape comparationMatrix
    similarity = cosine_similarity(promptEmbeddings, comparationMatrix) #The enumerate() function provides the index i, which can be used to access the corresponding name from the names list
    results = []
    for i, score in enumerate(similarity[0]):
        results.append((names[i], score))
    return results


if __name__=="__main__":

    print("BIENVENIDO AL BUSCADOR SEMANTICO!\n")

   

    while True:
        prompt = input("Ingresa una búsqueda (escribe 'Terminar' para salir): ")

        if prompt == "Terminar":
            break

        names, array = getEmbeddingsFromdb()

        res = similarities(prompt, array, names)

        for i in res:
            print(i)

        saveResults(prompt, res)  # Pass the header_written flag to saveResults

    

    print("Programa terminado.")
    
