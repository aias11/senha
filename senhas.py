import random #gera combinações aleatórias
import string #para poder utilizar textos

minima = 8
simbolos_permitidos = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"    
numeros = "1234567890"

def gerar_senha_aleatória(tamanho=8):
         caracteres = string.ascii_letters + string.digits + string.punctuation
         senha = ''.join(random.choices(caracteres, k=tamanho))
         return senha
    
resposta = input("Gostaria de criar uma senha? (sim/não) ").strip().lower()
    
if resposta == "sim":
         senha_gerada = gerar_senha_aleatória()
         print(f"Sua senha gerada é {senha_gerada}")

else:


            while True:


             senha = input("Digite a sua senha: ") #int para permitir apenas numeros, input para criar uma caixa de texto

             if (
                 len(senha) >= minima
                and any(char.isupper() for char in senha)  # Contém ao menos uma letra maiúscula
                 and not senha.isdigit()  # Não é composta apenas por números
                 and any(char in simbolos_permitidos for char in senha)
                 and any(char in numeros for char in senha)
                ):
                break

             else:

                if len(senha) < minima:
                 print(f"A senha deve ter no minimo 8 caracteres")
                if not any(char.isupper() for char in senha):
                 print("A senha deve conter pelo menos uma letra maiuscula")
                 if senha.isdigit():
                  print("A senha não pode ser composta apenas por números")
                if not any(char in simbolos_permitidos for char in senha): 
                 print(f"A senha deve conter pelo menos um símbolo")   
                if not any(char in numeros for char in senha):
                  print(f"A senha deve conter pelo menos 1 número")         

            print(f"Sua senha foi aceita {senha}")