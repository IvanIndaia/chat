# Front-End
# Back-End
# pip install flet -> No terminal

# Título HashZap
# Botão iniciar o chat
    # Popup 
        # Bem-Vindo
        # Escreva seu nome
        # Entrar no chat
# Chat
    # Lira entrou no chat
    # Mensagens do usuário
# Campo para enviar mensagem
# Botão de enviar

import flet as ft 

def main(pagina):
    #titulo = ft.Text("HashZap")

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()
    
    # =============================== TUNEL ===============================
    def enviar_mensagem_tunel(informacoes):
         chat.controls.append(ft.Text(informacoes))
         pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # =============================== ENVIAR MENSAGEM ===============================
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        #chat.controls.append(ft.Text(texto_campo_mensagem))

        pagina.pubsub.send_all(texto_campo_mensagem)
        #limpar o campo da mensagem
        campo_mensagem.value = ""

        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # =============================== ENTRAR NO CHAT ===============================
    def entrar_chat(evento):
         popup.open = False
         pagina.remove(botao_iniciar)
         pagina.add(chat)
         linha_mensagem = ft.Row(
             [campo_mensagem, botao_enviar]
         )
         pagina.add(linha_mensagem)
         
         texto = f"{nome_usuario.value} entrou no chat"

         #chat.controls.append(ft.Text(texto))
         pagina.pubsub.send_all(texto)

         pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem-Vindo ao HashZap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    
    # =============================== INICIAR CHAT ===============================
    def iniciar_chat(evento):
        # print("Iniciar o chat")
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat) 
    
    
    #pagina.add(titulo)
    pagina.add(botao_iniciar)


#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)
