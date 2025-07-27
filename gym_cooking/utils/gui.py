from tkinter import *
from tkinter import ttk
"""
import pyaudio
import wave
import whisper
"""

def popup_text_source(description: str = '', fill_in: str = '') -> str | None:
    root = Tk()
    # root.geometry("300x300")
    root.title("Input Window OK?")

    ret = None

    def take_input():
        i = inputtxt.get("1.0", "end-1c")
        nonlocal ret
        ret = i
        root.destroy()

    label = Label(text=description, font=('microsoftyaheiui', 15, 'bold'))
    inputtxt = Text(root, height=15, width=30, bg="light yellow", font=('microsoftyaheiui', 15, 'bold'))
    inputtxt.insert("end-1c", fill_in)
    display = Button(root, height=2, width=5, text="Submit", command=lambda: take_input())

    label.pack()
    inputtxt.pack()
    display.pack()

    mainloop()

    return ret

"""
def popup_text_voice(description: str = '', fill_in: str = '') -> str | None:
    root = Tk()
    # root.geometry("300x300")
    root.title("Input Window")

    ret = None

    def take_input():
        i = inputtxt.get("1.0", "end-1c")
        nonlocal ret
        ret = i
        root.destroy()

    image = PhotoImage(file='voice.png')
    #label = Label(text=description, font=('microsoftyaheiui', 15, 'bold'))
    label = ttk.Label(root,
                      text=description,
                      font=('microsoftyaheiui', 15, 'bold'),
                      image=image,
                      compound='bottom')
    
    #inputtxt = Text(root, height=15, width=30, bg="light yellow", font=('microsoftyaheiui', 15, 'bold'))
    #inputtxt.insert("end-1c", fill_in)
    display = Button(root, height=2, width=10, text="録音", command=lambda: take_input())

    label.pack()
    #inputtxt.pack()
    display.pack()

    mainloop()

    return ret


def popup_text(description: str = '', fill_in: str = '') -> str | None:
    root = Tk()
    #root.geometry("300x300")
    root.title("Input Window OK?")

    ret = None

    def take_input():
        i = inputtxt.get("1.0", "end-1c")
        nonlocal ret
        ret = i
        root.destroy()

    def streaming():
        chunk = 1024 * 4 #バッファのサイズ　リアルタイム性を求めるなら小さく
        format = pyaudio.paInt32
        channels = 2
        fs = 44100
        record_second = 5

        model = whisper.load_model("base", device="cpu")
        mic = pyaudio.PyAudio()
        stream = mic.open(format=format, channels=channels, rate=fs, input=True, frames_per_buffer=chunk)
        print("* recording")
        frames = []
        nonlocal ret
        for i in range(0, int(fs / chunk * record_second)):
            data = stream.read(chunk)
            frames.append(data)
        print("Done.")

        stream.stop_stream()
        stream.close()
        mic.terminate()

        out_path = "./voice/data/output.wav"
        wf = wave.open(out_path, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(mic.get_sample_size(format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close

        result = model.transcribe("./voice/data/output.wav", language="ja", fp16=False)
        ret = result['text']
        root.destroy()

    label = Label(text=description, font=('Times New Roman', 20, 'bold'))
    inputtxt = Text(root, height=15, width=30, bg="light yellow", font=('Times New Roman', 20, 'bold'))
    inputtxt.insert("end-1c", fill_in)
    display1 = Button(root, height=5, width=10, text="Submit", command=lambda: take_input())
    display2= Button(root, height=5, width=10, text="Rcording", command=lambda: streaming())

    label.grid(row=0, column=0, columnspan=2, pady=10)
    inputtxt.grid(row=1, column=0, columnspan=2, pady=10)
    display1.grid(row=2, column=0, padx=10, pady=10)
    display2.grid(row=2, column=1, padx=10, pady=10)
    mainloop()

    return ret

def popup_choice(description: str, choices: list[str]) -> str | None:
    root = Tk()
    root.geometry("300x200")
    root.title("Choose Window")

    ret = None

    def take_input():
        nonlocal ret
        ret = var.get()
        root.destroy()

    label = Label(text=description, font=('Times New Roman', 15, 'bold'))
    var = StringVar(root)
    var.set(choices[0])
    option = OptionMenu(root, var, *choices)
    display = Button(root, height=2, width=5, text="Submit", command=lambda: take_input())

    label.pack()
    option.pack(expand=True)
    display.pack()

    mainloop()

    return ret

def popup_box(description: str = '') -> bool | None:
    root = Tk()
    # root.geometry("300x300")
    root.title("Box Window")

    ret = None

    def take_yes():
        nonlocal ret
        ret = True
        root.destroy()

    def take_no():
        nonlocal ret
        ret = False
        root.destroy()

    label = Label(text=description, font=('Times New Roman', 15, 'bold'))
    display_yes = Button(root, height=2, width=5, text="Yes", command=lambda: take_yes())
    display_no = Button(root, height=2, width=5, text="No", command=lambda: take_no())

    label.pack()
    display_yes.pack()
    display_no.pack()

    mainloop()

    return ret

if __name__ == '__main__':
    print(popup_text("test", "test"))
    print(popup_choice("tes11111t", ["test1", "test2"]))
    print(popup_box("tes22222"))
"""
