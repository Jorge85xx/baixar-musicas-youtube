from pytube import YouTube

link = input("Digite o link do video que voce deseja baixar: ")

yt = YouTube(link)
print("Baixando: ", yt.title)

audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
audio_stream.download(output_path=".", filename=f"{yt.title}.mp3")
print("Dowload concluido")
