#Tarea 1: Convertir Strings en Minusculas

#Tarea 2: Frecuencia de cada palabra en una cadena determinada

#Tarea 3: Frecuencia de una palabra especifica 

#Tare Extra: El analizador recibe un nombre de archivo y procesa el contenido del mismo, tiene un Metodo
#            que permite escribir la frecuencia de palabras en otro archivo.

# VER VIDEO DEL TUTORIAL

import time

# PASO 1 : DEFINIR EL STRING

input = """La inteligencia artificial (IA) es un campo de estudio que abarca desde la simulación del razonamiento humano hasta la creación de máquinas que pueden aprender y tomar decisiones. A lo largo de los años, la IA ha avanzado significativamente, transformando industrias como la medicina, el transporte y la educación.

El aprendizaje automático, una rama de la IA, permite que las computadoras desarrollen habilidades sin estar explícitamente programadas para ello. En lugar de seguir instrucciones específicas, las máquinas pueden analizar grandes cantidades de datos y detectar patrones para mejorar su rendimiento.

Sin embargo, con estos avances también surgen preocupaciones. La ética en la inteligencia artificial es un tema que se discute ampliamente, ya que las decisiones automatizadas pueden afectar la privacidad y los derechos de las personas. A medida que la IA continúa desarrollándose, es fundamental establecer regulaciones y principios éticos que guíen su implementación.

Por otro lado, el impacto positivo de la IA es innegable. Desde diagnósticos médicos más rápidos y precisos hasta vehículos autónomos que prometen reducir los accidentes de tránsito, las aplicaciones de la IA son diversas y están en constante expansión. En el futuro, se espera que la inteligencia artificial siga revolucionando la manera en que vivimos y trabajamos, brindando soluciones a problemas complejos que hasta hace poco parecían imposibles de resolver."""



def replaceFromList(text, repList = []):
  newText = ''
  repSet = set(repList)
  
  for char in text:
    if char not in repSet:
      newText = newText + char

  return newText

# PASO 2: DEFINIR LA CLASE Y SUS ATRIBUTOS
class TextAnalyzer():
  
  def __init__(self, text = ''):
    # formattedText = text.replace('.', '').replace('!','').replace('?','').replace(',','')
    formattedText = replaceFromList(text, ['.', ',', '!', '¡', '¿', '?', ';'])

    # PASO 3: PASAR EL STRING A MINÚSCULAS    
    self.fmtText = formattedText.lower()
    print (self.fmtText)
  

  # Paso 4: Contar la frecuencia de todas las palabras unicas
  def freqAll(self):

    #Partir cada vez que encuentre un espacio
    wordList = self.fmtText.split(' ')

    freqMap = {}
    for word in set(wordList):
      freqMap[word] = wordList.count(word)

    return freqMap


  # PASO 5: CONTAR LA FRECUENCIA DE UNA PALABRA EN ESPECÍFICO
  def freqOf(self, word):

    freqDict = self.freqAll()

    if word in freqDict:
      return freqDict[word]
    else:
      return 0


###########__Main__########################
analyzed = TextAnalyzer(input)

freqOfAllWords = analyzed.freqAll()

print(freqOfAllWords)
print(f"Occurrences of 'inteligencia': {analyzed.freqOf('inteligencia')}")