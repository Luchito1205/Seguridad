import time

alfa = "abcdefghijklmnñopqrstuvwxyz"
alfa += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfa += "1234567890"
alfa += "!@#$%^&*()_+-=[]|;:',.<>?/"

contra = "abcd"
inten1 = 0

tiempo_inicio = time.time()

for largo in range(1,5):
    index = [0] * largo
    while True:
        inten = ""
        for i in index:
            inten += alfa[i]
        inten1 += 1
        
        if inten == contra:
            tiempo_termina = time.time()
            print("Contraseña encontrada:", inten)
            print("Número de intentos:", inten1)
            print("Tiempo de ejecución:", tiempo_termina - tiempo_inicio, "segundos")
            exit()
        
        for i in range(largo - 1, -1, -1):
            if index[i] + 1 < len(alfa):
                index[i] += 1
                break
            else:
                index[i] = 0
        else:
            break 