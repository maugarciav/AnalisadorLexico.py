import re

def split_cadenas(texto):


  numeros_reales_pattern = r'[-]?[\.]?\d+[.]?\d*[(e|E)]?[-]?\d*'
  variables_pattern = r'[A-Za-z][\w]*'
  comment_patern= r'//.*'
  operadores_pattern  = r'[=*+-/^()]'
  
  list = re.findall(numeros_reales_pattern + "|" + variables_pattern + "|" + comment_patern + "|" + operadores_pattern,texto) 
  


  return list 
  
# texto = "a var  6.1E-8 2.3E3 mauricio 6.345e-5 -0.001E-3 .467E9 //comentario hello"
texto = "b=7 a = 32.4 *(-8.6 - b)/       6.1E-8 d = a ^ b // Esto es un comentario"
# texto = "a = 32.4 *(-8.6 - b)/        6.1E-8   10.//hello this is a comment"
newtext = split_cadenas(texto)

print(newtext)
