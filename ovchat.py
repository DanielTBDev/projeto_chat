import flet as ft

def main(pagina):
    titulo = ft.Text('OVChat')

    titulo_janela = ft.Text('Bem-vindo ao OVChat!')
    nome = ft.TextField(label='Digite seu nome')
    chat = ft.Column()

    def global_msg(mensagem):
        chat_text = ft.Text(mensagem)
        chat.controls.append(chat_text)
        pagina.update()

    pagina.pubsub.subscribe(global_msg)

    def enviar_mensagem(evento):
        texto_msg = campo_msg.value
        username = nome.value
        mensagem = f'{username}: {texto_msg}'
        pagina.pubsub.send_all(mensagem)
        campo_msg.value = ''
        pagina.update()


    campo_msg = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar_msg = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_msg = ft.Row([campo_msg, botao_enviar_msg])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open=False
        pagina.add(chat)
        pagina.add(linha_msg)
        mensagem = f'{nome.value} entrou no chat.'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=nome, actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)