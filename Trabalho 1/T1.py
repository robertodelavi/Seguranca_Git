import socket
import time
import hashlib
import struct
import os
import thread
import math
import random

def abre_arquivo(path):  
    arquivo  = open(path, "rb")
    alfabeto = arquivo.read()    
    return alfabeto

def gravar_arquivo(path, conteudo):        
    arquivo = open(path, 'ab+')
    arquivo.truncate() # limpa arquivo, para caso de salvar arquivo ja existente
    arquivo.seek(0)
    arquivo.write(conteudo)
    arquivo.close()    

def criptografa(texto_limpo, chave):
    cifra = ''    
    for ch in texto_limpo:        
        ordC  = (ord(ch)+int(chave))%256
        cifra = cifra + chr(ordC)     
    return cifra

def descriptografa(texto_cifrado, chave):    
    texto_limpo = ''    
    for ch in texto_cifrado:
        chrC  = (ord(ch)-int(chave))%256
        texto_limpo = texto_limpo + chr(chrC)     
    return texto_limpo                

# a largura da matriz sera o tamanho da chave
def cria_matriz(conteudo, chave): # 3    
    count = 0
    tam_conteudo = len(conteudo)    
    lin = math.ceil(float(tam_conteudo)/float(chave))    
    
    A = []
    for i in range(int(lin)):         # linha      
        linha = []
        for j in range(chave): # coluna 
            # para nao dar erro de indexacao                
            if(count > (len(conteudo)-1)): 
                campo = -1
            else:
                campo = conteudo[count]
            # monta        
            linha = linha + [campo]    
            count += 1

        A = A + [linha]
    return A        

def transposta_matriz(matriz, conteudo):
    aux=[]
    for j in range(len(matriz[0])):
        linha=[]
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
        aux.append(linha)
    return aux   

def mostra_matriz(matriz, conteudo):
    count = 0
    print
    print
    print 'Matriz de transposicao'     
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):            
            print matriz[i][j],'\t',
            if(count == (len(conteudo)-1)): # para nao dar erro de indexacao
                return;
            count += 1
        print
    print 

def convert_to_text(conteudo):
    text = ''.join(conteudo)

    new_text = conteudo.split(",")
    a = ''
    for ch in new_text:
        a += ch

    new_text = a.split("'")
    b = ''
    for ch in new_text:
        b += ch

    new_text = b.split("[")
    c = ''
    for ch in new_text:
        c += ch

    new_text = c.split("]")
    d = ''
    for ch in new_text:
        d += ch

    new_text = d.split(" ")
    e = ''
    for ch in new_text:
        e += ch
    
    return e

############## CIFRA DE CESAR ##############
chave_cesar = raw_input('Cifra de Cesar - Insira a chave: ') 
# Criptografa   
texto_limpo = abre_arquivo('arquivos/cifra_cesar/descriptografado.txt')
#cifra = criptografa(texto_limpo, chave_cesar)  
cifra = criptografa(texto_limpo, chave_cesar)  
gravar_arquivo('arquivos/cifra_cesar/criptografado.txt', cifra)    
# Descriptografa
texto_cript = abre_arquivo('arquivos/cifra_cesar/criptografado.txt')
texto_limpo = descriptografa(texto_cript, chave_cesar)  
gravar_arquivo('arquivos/cifra_cesar/descriptografado.txt', texto_limpo)    

############## CIFRA DE TRANSPOSICAO ##############
texto = abre_arquivo('arquivos/cifra_transposicao/descriptografado.txt')
chave_trans = raw_input('Cifra de Transposicao - Insira a chave: ') 
# cria matriz
mat = cria_matriz(texto, int(chave_trans))
mostra_matriz(mat, texto)
# realiza a transposta
mat_trans = transposta_matriz(mat, texto)
mostra_matriz(mat_trans, texto)
# grava no arquivo

# convert list to string (para poder gravar no arquivo)
string_trans = convert_to_text(str(mat_trans))
gravar_arquivo('arquivos/cifra_transposicao/criptografado.txt', string_trans)
#string_crip = abre_arquivo('arquivos/cifra_transposicao/criptografado.txt')

print 
#print 'mat_trans'
print
#print string_trans
print





