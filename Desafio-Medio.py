'''
RESULTADO
Senha:  SI-ADS182-KT6LQW
Texto:  Why, Mr. Anderson? Why, why? Why do you do it? Why, why get up? Why keep fighting? Do you believe you're fighting... for something? For more than your survival? Can you tell me what it is? Do you even know? Is it freedom? Or truth? Perhaps peace? Could it be for love? Illusions, Mr. Anderson. Vagaries of perception. Temporary constructs of a feeble human intellect trying desperately to justify an existence that is without meaning or purpose. And all of them as artificial as the Matrix itself, although... only a human mind could invent something as insipid as love. You must be able to see it, Mr. Anderson. You must know it by now. You can't win. It's pointless to keep fighting. Why, Mr. Anderson? Why? Why do you persist?
'''

from Crypto.Cipher import AES
import base64
from threading import Thread

LISTA_CARACTERES = ['A','B','C','D','E','F','G','H','I','J',
                    'K','L','M','N','O','P','Q','R','S','T',
                    'U','V','W','X','Y','Z',
                    '0','1','2','3','4','5','6','7','8','9']
LIMITE = int((len(LISTA_CARACTERES) / 2)+1)


BLOCK_SIZE = 16
PADDING = '0' # A VALIDAÇÃO PODE SER FEITA COM QUALQUER CARACTER COMO PADDING, POREM OS DESAFIOS DÃO ERRO

TEXTO_VALIDACAO = b'OTPo13y3UribI/7BRivfgiEJ3bF+KgYSyJ32/qERi85cBE79aRSsW8wVmBc1yBiJks5fxTDTGQOQ3O+PQMAwUTeZfWYxlGuMuDypX94sCN9kdx+BtmpFS6knGSbmYPLMsjUerBilDO+nf/AFgGIdNG+p0+nqtunuKqXdp7Q7R+UtKPellrArCjUlbcNNcOLsFzKZ2uRC1RrLxYRN2XJi0mODIeKGJ3twVmP62RWqxNFG/wlrQJEnuMu+JMmjySvuAeOlSMFPgUtqSwWFJAe9kTC2qKaNxDDTELMpLHj09QiKKaz4foQJu75i20To3jPRIVgXcwPrd9y+VH38GWAsVaWIUyYBl1mDanlW023a9c3VUEoPub0T/vfr/VlitJGcYlQYAH91Tpep5cEhB8lN9xrz3bDLIN/UHCBD9j4qgix71soGW2Psqrlm9z0ZMPs0pJzDITAJPDp3tkXnbgs9rGbPohsxQ3WGNrruhZM9FoVFT/fgXg9dkBzgLGuaxP2J3b4bFk6EsS17EGL5kBNjdtKQ+D0Gsq43rGShM7PfMZ1dZBpYUAFxu0n6lAMavrdXgdJkNxydTZuLjtV/Aq53w6oUy+qUpyM5kPdnHJqqr4hKCNtKySi1KpC22laqg3+B1wASfMBzl16DJQFPQfvM7Uo/cN2uWduKGqIf2zyds2cvQNqhHrgmUpNrr2JYTrB0P+nH+77KEYZJCIbgA+ZFJDXf2jQG4GrkRQaps/l5k/xeFEdiqBeajWu13WSyT2Uekd8/Fg05L+3+BmpKPHymMRwLOAIWw/aDBSqiau15aumBEsEjpIdAtLaBShWh4Zat1IjXItkxGu0X83bLq0rusAg96WD3EHES+DOkfjIneJYYmV/tBtmgqxYki9qjMKpGPoSwchEo+x56/13jcSB4S4ltSZt6Kgm5HW0oJY/mQMsda90hQ1fBFdawEmcb41Ed5dTxFvMYXTI5w9CzekEYHg=='
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
