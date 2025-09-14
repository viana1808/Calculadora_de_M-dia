3. Digite as notas quando solicitado.

---

## Objetivo do projeto

Esse projeto foi criado para praticar conceitos básicos de:
- Entrada de dados com `input`
- Conversão de tipos (`float`)
- Estruturas condicionais (`if`, `elif`, `else`)


# Calculadora de Média
# Desenvolvido como projeto simples em Python

def calcular_media():
    print("Calculadora de Média Escolar 📚")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    print(f"Sua média final é: {media:.2f}")

    if media >= 7.0:
        print("Aprovado! 🎉")
    elif media >= 5.0:
        print("Recuperação. 😬")
    else:
        print("Reprovado. 💔")

if __name__ == "__main__":
    calcular_media()
