'''
RESULTADO
Senha:  ADS-Grupo-04-448
Texto:  I think it's fair to say that personal computers have become the most empowering tool we've ever created. They're tools of communication, they're tools of creativity, and they can be shaped by their user.
'''

from Crypto.Cipher import AES
import base64
from threading import Thread

LISTA_CARACTERES = ['0','1','2','3','4','5','6','7','8','9', 'A']
LIMITE = int((len(LISTA_CARACTERES) / 2)+1)


BLOCK_SIZE = 16
PADDING = '0' # A VALIDAÇÃO PODE SER FEITA COM QUALQUER CARACTER COMO PADDING, POREM OS DESAFIOS DÃO ERRO

TEXTO_VALIDACAO = b'1xsedtC1eXsogUTMM5OuNNsQMyAnjbsCnPoDECRWDyxHQTKxhAfb+K0FVfbdH3XvyATdV4aauW4mknchRmOUuPMW3plZ5EXJEbSQRSJFKv7GVObF82Fvjt1UXWHssnIbYCu+vWO5Kpk6jy/IWVfNFsJfuyELKoUTGY7VPXpChtQofERr+xSKiHmhg7a1C6D0zeLRRDBfQOYiM2yCy+KUHY+7uJUqdtc8nmWxfSovsGtESDGaw8mGN5Vyj8NhWE1XB9zy2KKc7gvRVFl5ogXTDQ=='
PREFIXO_SENHA = 'ADS-Grupo-04-'

def descriptografar(texto_encriptado, senha):
    decodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    cipher = AES.new(senha)
    decoded = decodeAES(cipher, texto_encriptado)
    texto = str(decoded.decode()).strip(PADDING)
    return texto

def descriptografar_t1():
    for x in range(0, LIMITE):
        for y in range(0, len(LISTA_CARACTERES)):
            for z in range(0, len(LISTA_CARACTERES)):
                passwd = PREFIXO_SENHA + LISTA_CARACTERES[x] + LISTA_CARACTERES[y] + LISTA_CARACTERES[z]
                print(passwd)
                try:
                    texto = descriptografar(TEXTO_VALIDACAO, passwd)
                    print("Senha: ", passwd)
                    print("Texto: ", texto)
                    save_point = len(LISTA_CARACTERES)+1
                    z = save_point
                    y = save_point
                    x = save_point
                    break
                except:
                    continue

def descriptografar_t2():
    for x in range(LIMITE, len(LISTA_CARACTERES)):
        for y in range(0, len(LISTA_CARACTERES)):
            for z in range(0, len(LISTA_CARACTERES)):
                passwd = PREFIXO_SENHA + LISTA_CARACTERES[x] + LISTA_CARACTERES[y] + LISTA_CARACTERES[z]
                print(passwd)
                try:
                    texto = descriptografar(TEXTO_VALIDACAO, passwd)
                    print("Senha: ", passwd)
                    print("Texto: ", texto)
                    save_point = len(LISTA_CARACTERES)+1
                    z = save_point
                    y = save_point
                    x = save_point
                    break
                except:
                    continue


thread1 = Thread(target=descriptografar_t1())
thread2 = Thread(target=descriptografar_t2())

thread1.start()
thread2.start()
