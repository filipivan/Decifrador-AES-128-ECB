'''
RESULTADO
Senha:  SI-ADS182-VGZFUF
Texto:  They come from a much older version of the Matrix, but like so many back then they caused more problems than they solved. My husband saved them because they are notoriously difficult to terminate. How many people keep silver bullets in their gun?
'''

from Crypto.Cipher import AES
import base64
from threading import Thread

LISTA_CARACTERES = ['A','B','C','D','E','F','G','H','I','J',
                    'K','L','M','N','O','P','Q','R','S','T',
                    'U','V','W','X','Y','Z']
LIMITE = int((len(LISTA_CARACTERES) / 2)+1)


BLOCK_SIZE = 16
PADDING = '0' # A VALIDAÇÃO PODE SER FEITA COM QUALQUER CARACTER COMO PADDING, POREM OS DESAFIOS DÃO ERRO

TEXTO_VALIDACAO = b'TVJs13K4WpOSz5c1gs1Ri6ximORCVk+r1bLR3/RmtSG3rkQFJmS1gMlfAMbe5OKz0jbWHiuTYgVgbYP1XQs9dJWn7HjkQmkIER0G5WstLGSoSYT/jDv0cToFMiWqkOheKbmr/X68WE9yBYjOKo5PZ0hxpOg4tV5/obq4hOAfZgECZpfYy0qpFmN8eFmqzoDKsra+ELml8rPYmGuw5LJK/ekE1zc6K6GPQZ85XOp5YrqkpJLQtFrNXjbZIjlkMlnWPCeeaxBPF3GxKuRNLLvbb9c4i8kigYqAgzeMsdY+7MlJpzLdq9xQFQVI4bOlsa/4WTMaJoywLaqX0MjJ3Uoh6g=='
PREFIXO_SENHA = 'SI-ADS182-'

def descriptografar(texto_encriptado, senha):
    decodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
    cipher = AES.new(senha)
    decoded = decodeAES(cipher, texto_encriptado)
    texto = str(decoded.decode()).strip(PADDING)
    return texto

def descriptografar_t1():
    for x1 in range(0, LIMITE):
        for x2 in range(0, len(LISTA_CARACTERES)):
            for x3 in range(0, len(LISTA_CARACTERES)):
                for x4 in range(0, len(LISTA_CARACTERES)):
                    for x5 in range(0, len(LISTA_CARACTERES)):
                        for x6 in range(0, len(LISTA_CARACTERES)):
                            passwd = PREFIXO_SENHA + LISTA_CARACTERES[x1] + LISTA_CARACTERES[x2] + LISTA_CARACTERES[x3] + LISTA_CARACTERES[x4] + LISTA_CARACTERES[x5] + LISTA_CARACTERES[x6]
                            print(passwd)
                            try:
                                texto = descriptografar(TEXTO_VALIDACAO, passwd)
                                print("Senha: ", passwd)
                                print("Texto: ", texto)
                                save_point = len(LISTA_CARACTERES)+1
                                x1 = save_point
                                x2 = save_point
                                x3 = save_point
                                x4 = save_point
                                x5 = save_point
                                x6 = save_point
                                break
                            except:
                                continue

def descriptografar_t2():
    for x1 in range(LIMITE, len(LISTA_CARACTERES)):
        for x2 in range(0, len(LISTA_CARACTERES)):
            for x3 in range(0, len(LISTA_CARACTERES)):
                for x4 in range(0, len(LISTA_CARACTERES)):
                    for x5 in range(0, len(LISTA_CARACTERES)):
                        for x6 in range(0, len(LISTA_CARACTERES)):
                            passwd = PREFIXO_SENHA + LISTA_CARACTERES[x1] + LISTA_CARACTERES[x2] + LISTA_CARACTERES[x3] + LISTA_CARACTERES[x4] + LISTA_CARACTERES[x5] + LISTA_CARACTERES[x6]
                            print(passwd)
                            try:
                                texto = descriptografar(TEXTO_VALIDACAO, passwd)
                                print("Senha: ", passwd)
                                print("Texto: ", texto)
                                save_point = len(LISTA_CARACTERES)+1
                                x1 = save_point
                                x2 = save_point
                                x3 = save_point
                                x4 = save_point
                                x5 = save_point
                                x6 = save_point
                                break
                            except:
                                continue


thread1 = Thread(target=descriptografar_t1())
thread2 = Thread(target=descriptografar_t2())

thread1.start()
thread2.start()
