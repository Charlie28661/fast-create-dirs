import os
import tkinter

gui = tkinter.Tk()
gui.geometry("500x300")
gui.title("創建資料夾")


def send():
    send_font.set("已創建成功,前往 {} 查看吧!".format(path_location.get()))
    name = 0
    for i in range(0 ,times.get()):
        os.makedirs("{}\{}".format(path_location.get(), name))
        name = name + 1

header_text = tkinter.Label(gui, text="快速創建更多資料夾吧!!", font=(35), padx=20, pady=10)
path_text = tkinter.Label(gui, text="請輸入創建路徑", padx=20, pady=10)
path_location = tkinter.StringVar()
location = tkinter.Entry(gui, textvariable=path_location)
times_text = tkinter.Label(gui, text="請輸入創建次數", padx=20, pady=10)
times = tkinter.IntVar()
times_times = tkinter.Entry(gui, textvariable=times)
send_font = tkinter.StringVar()
foooter_button = tkinter.Button(gui, textvariable=send_font, command=send, padx=10)
send_font.set("送出")



header_text.pack()
path_text.pack()
location.pack()
times_text.pack()
times_times.pack()
foooter_button.pack()
gui.mainloop()