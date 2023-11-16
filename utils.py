from pytube import YouTube

message_bot = '''
*Mensagem do Desenvolvedor*\n\n"Para baixar qualquer video do YouTube envie o link aqui no chat". 👨‍💻💬
'''

def downtube(link):
    yt = YouTube(link)
    yt.streams.get_by_itag(22).download(
        output_path='video',
        filename='baixado.mp4')

def buff_file():
    video = open('video/baixado.mp4', 'rb')
    return video
