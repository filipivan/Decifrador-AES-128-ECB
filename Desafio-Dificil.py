'''
RESULTADO
SI-ADS182-LSoajO
Senha:  SI-ADS182-LSoajO
Texto:  There are two doors. The door to your right leads to the Source and the salvation of Zion. The door to your left leads back to the Matrix, to her... and to the end of your species. As you adequately put, the problem is choice. But we already know what you are going to do, don't we? Already I can see the chain reaction: the chemical precursors that signal the onset of an emotion, designed specifically to overwhelm logic and reason. An emotion that is already blinding you to the simple and obvious truth: she is going to die and there is nothing you can do to stop it.     
'''

from Crypto.Cipher import AES
import base64
from threading import Thread

LISTA_CARACTERES = ['A','B','C','D','E','F','G','H','I','J',
                    'K','L','M','N','O','P','Q','R','S','T',
                    'U','V','W','X','Y','Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z',
                    '0','1','2','3','4','5','6','7','8','9']
LISTA_VOGAIS = ['A','E','I','O','U','a','e', 'i','o','u']
LIMITE = int((len(LISTA_CARACTERES) / 2)+1)


BLOCK_SIZE = 16
PADDING = '0' # A VALIDAÇÃO PODE SER FEITA COM QUALQUER CARACTER COMO PADDING, POREM OS DESAFIOS DÃO ERRO

TEXTO_VALIDACAO = b'dxWoS1MaBPPlSHgSfOiwtH5Lx8THLuHtiH1v54Lp6H3i5ihkn3OTKOK9+QDjEJUJgwUJo4900wcDHWr1RW/MvtYBIOoiM4sp8N7Z+2O9kco61WyT2+0onossy8HD3aDvFFoPThVly57DLD+WoYKPijU7hMwnLF98YtIiqQex7nuqvj74DqWAVDCQPedMKI6jG+vovVHki65UtpTCDSDFxn0KpVX934FqZos60W/byvFgDM2Fb0ktmInqP7Ohus/Q2JbTE5erlrXDw2tMmVgPbzXTPebMgbEBHJiblSrCfsA4SVZDw4dFk3tAUVPxuF02FN1ysujwGsWhWdjTGd5QkZY4i4fBwu17H/NZzlFIH+zBPEPgavg5tmpMkVw6BaBUo/itI/ujnVVapfN2KxSBkdAB5NowAPCd5t5JhsjVwpq+zlEON8uEpnKroVEMmmCU7wMqdkWaIm90DZm6Qlsfk+kZIaGDDienfJyPK5VlH13JtumPrJ6GISNnGVBRRjnw4ZIJ6g/t9PvPdV1RUoKOYbtyM8UQOC9ecA8M/M6OrfxhcCKhlmS73i9I6f2OoFxZHXyTCQE1UU4On5e0+O6GBteTScjVUyOASPyP2c0Pd73y0Jygu/1j1NGL2MFSPFUPkZWTrTG+gRqdOU5Uejg47AFyPIvWER2CgcxtTN64DFes2osJgCL91Q3p7XIcA9FA61krHhotbbEnvlCUSol6DKGYmmXELAQNDKrmUMjfqQyk8pcncT0Texu5Tr+6TGBu'
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
                        for x6 in range(0, len(LISTA_VOGAIS)):
                            passwd = PREFIXO_SENHA + LISTA_CARACTERES[x1] + LISTA_CARACTERES[x2] + LISTA_CARACTERES[x3] + LISTA_CARACTERES[x4] + LISTA_CARACTERES[x5] + LISTA_VOGAIS[x6]
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
                        for x6 in range(0, len(LISTA_VOGAIS)):
                            passwd = PREFIXO_SENHA + LISTA_CARACTERES[x1] + LISTA_CARACTERES[x2] + LISTA_CARACTERES[x3] + LISTA_CARACTERES[x4] + LISTA_CARACTERES[x5] + LISTA_VOGAIS[x6]
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
