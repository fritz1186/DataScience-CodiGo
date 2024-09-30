class TextAnalyzer():

    def __init__(self):               
        self.fmt_text = ""
        self.wordList = []    

    # Metodo Estatico para extraer texto de un archivo
    @staticmethod
    def extract_text (filename):
        try:
            file = open(filename, encoding="utf-8")

            extracted_text = file.read()
            return extracted_text
        
            file.close()
        except Exception as error:
            print ("Error al Extraer: ", error)

    @staticmethod
    def insert_text (wordlist, filename):

        with open(filename, 'w', encoding="utf-8") as outputFile:
            outputFile.write("[")
            for word in wordlist:
                outputFile.write(f"'{word}', ")                       
            outputFile.write("]")                  

    # Metodo para procesar un texto, filtrando palabras determinadas
    def process_text (self, raw_text, stop_words):

        #1. Convertir todo el texto a minusculas
        formatted_text = raw_text.lower()

        #2.1 Eliminar saltos de linea, los convierte a espacio porque sino se pega a la otra letra                        
        formatted_text = formatted_text.replace("\n"," ")

        #2.2 Eliminar caracteres que no sean letras +
        #3. Eliminar cualquier digito presente en el texto
        caracteresNoLetras = "1234567890.,;:¿?¡!()"
        formatted_text = ''.join([char for char in formatted_text if char not in caracteresNoLetras])
        
        self.fmt_text = formatted_text

        print("Raw Text: ", self.fmt_text , "\n") 

        #4. Tokenizar el texto (convertirlo en una lista de palabras)
        #Separa el texto por cada espacio    
        wordList = self.fmt_text.split(" ")
        #Borra los espacios vacios ingresados en la lista
        while "" in wordList:
            wordList.remove("")      
        print("Tokenized Text: ", wordList, "\n")

        #5. Remover las stopwords mas comunes en español
        #Se crea una lista de las StopWord, para esto se separa el texto
        stop_wordList = stop_words.split("\n")
        #Se crea una Lista Auxiliar para guardar las palabras adminitidas
        wordSetFiltered =[]
        
        #Solo se agrega las palabas permitidas a la lista Auxiliar
        for word in wordList:                        
            if word not in stop_wordList:                
                wordSetFiltered.append(word)        
        
        self.wordList = wordSetFiltered
        print ("Filtrado:" , self.wordList , "\n") 
    
    
    #Paso 4: Contral la frecuencia de cada palabra
    def frequency_all(self):
        
        #Se inicializa el mapa de frecuencias
        frequency_map ={}        

        print("WordSet:", set(self.wordList), "\n")

        for word in set(self.wordList):
            frequency_map[word] = self.wordList.count(word)        
        return frequency_map

    # Paso 5: contar la frecuencia de una sola palaba
    def frequency_of_word(self, word):
        frequeny_map = self.frequency_all()
        if word in frequeny_map:
            return frequeny_map[word]
        else:
            return 0
        

########################################################################
# 1. Abrir el archivo raw-text.txt y extraer el texto a Analizar.
raw_text = TextAnalyzer.extract_text("raw-text.txt")

# 2. Abrir el archivo stop-word.txt y extraer el texto a Filtrar.
stop_words = TextAnalyzer.extract_text("stop-words.txt")

# 3. Procesar el texto, como resultado da una lista de palabras que se guarda en el archivo processe-text.txt
analized_text = TextAnalyzer()
analized_text.process_text (raw_text, stop_words)

# 4. Inserta el texto en el archivo "processed-text.txt"
TextAnalyzer.insert_text (analized_text.wordList, 'processed-text.txt')

# 5. Contrar la frecuencia de todas slas palabras en el texto
frequencyAllWords = analized_text.frequency_all()
print ("Frequency All Word", frequencyAllWords)

# 6. Contrar la frecuencia de una palaba determinada
word = "inteligencia"
print (f"Ocurrence of {word}': '{ analized_text.frequency_of_word(word)}")