from openai import OpenAI

client = OpenAI(
    api_key = "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"
)


def enviar_mensagem(msg, lista_msg=[]):
    lista_msg.append({"role": "user", "content": msg})
    resposta = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": msg},
        ]
    )

    return resposta.choices[0].message

lista_msg = []

while True:
    texto = input("escreva aqui sua mensagem: ")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_msg)
        lista_msg.append(resposta)
        print("Chat: ", resposta.content)
