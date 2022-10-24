from tkinter import *
from chat import get_response, bot_name
import pyttsx3 as tts
import threading as td

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

engine = tts.init() 
voices = engine.getProperty('voices')
t1 = 0
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 150)


    

class ChatApplication: 
    
    def __init__(self): 
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        #head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        #tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        #text widget (Instace Variable is used here to use in another function later)
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        #scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        #bottom Label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        #message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        #send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command= lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get() 
        self._insert_message(msg, "You")
             
    
    def _insert_message(self, msg, sender):
        global t1
        if t1 == 0:
            pass
        elif t1.is_alive():
            return
        if not msg:   
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1) 
        self.text_widget.configure(state=DISABLED)
        response = get_response(msg)
        msg2 = f"{bot_name}: {response}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2) 
        self.text_widget.configure(state=DISABLED)
        t1 = td.Thread(target=speak, args=(response,))
        t1.start()
        self.text_widget.see(END)

def speak(str):
    engine.say(str)
    engine.runAndWait()
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()