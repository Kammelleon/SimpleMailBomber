import smtplib
import time
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
import threading

class MainFrame(tkinter.ttk.Frame):
    def __init__(self, container, width=452, height=686):
        super().__init__(container, width=width, height=height)
        self.canvas = Canvas(
            window,
            bg="#000000",
            height=686,
            width=452,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.spam_button_image = PhotoImage(file=f"main_frame_elements/img0.png")
        self.spam_button = Button(
            image=self.spam_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self._start_spam,
            relief="flat")

        self.spam_button.place(
            x=127, y=555,
            width=205,
            height=75)

        self.background_img = PhotoImage(file=f"main_frame_elements/background.png")
        self.canvas.create_image(
            226.0, 251.0,
            image=self.background_img)




        self.username_background = PhotoImage(file=f"main_frame_elements/img_textBox0.png")  #USERNAME
        self.canvas.create_image(
            219.5, 80.0,
            image=self.username_background)

        self.username_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.username_entry.place(
            x=117.0, y=64,
            width=205.0,
            height=30)






        self.password_background = PhotoImage(file=f"main_frame_elements/img_textBox1.png")  # PASSWORD
        self.canvas.create_image(
            219.5, 168.0,
            image=self.password_background)

        self.password_entry = Entry(
            bd=0,
            bg="#ffffff",show="*",
            highlightthickness=0)

        self.password_entry.place(
            x=117.0, y=152,
            width=205.0,
            height=30)






        self.message_entry_background = PhotoImage(file=f"main_frame_elements/img_textBox3.png") # MESSAGE
        self.canvas.create_image(
            228.0, 287.0,
            image=self.message_entry_background)

        self.message_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.message_entry.place(
            x=51.0, y=271,
            width=354.0,
            height=30)


        self.number_of_mails_background = PhotoImage(file=f"main_frame_elements/img_textBox4.png") # NUMBER OF MAILS
        self.canvas.create_image(
            226.0, 388.0,
            image=self.number_of_mails_background)

        self.number_of_mails_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.number_of_mails_entry.place(
            x=219.0, y=372,
            width=14.0,
            height=30)

        self.target_email_background = PhotoImage(file=f"main_frame_elements/img_textBox2.png")   # TARGET EMAIL
        self.canvas.create_image(
            225.5, 493.0,
            image=self.target_email_background)

        self.target_email_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.target_email_entry.place(
            x=123.0, y=477,
            width=205.0,
            height=30)

    def _start_spam(self):
        spam_thread = threading.Thread(target=self.spam)
        spam_thread.start()

    def spam(self):
        stop_spam = False

        login = str(self.username_entry.get())
        if not "@" in login:
            messagebox.showerror("Error","Login must be an gmail email (have to contain: '@gmail')")
            stop_spam = True

        password = str(self.password_entry.get())
        message = str(self.message_entry.get())

        try:
            number_of_mails = int(self.number_of_mails_entry.get())
        except:
            messagebox.showerror("Error","Number of mails have to be integer")
            stop_spam = True

        target_email = str(self.target_email_entry.get())
        if not "@" in target_email:
            messagebox.showerror("Error","Target email must be an email (have to contain: '@')")
            stop_spam = True

        if not stop_spam:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(login, password)

            for i in range(number_of_mails):
                smtp_server.sendmail(login, target_email, message)
                time.sleep(0.1)


if __name__ == "__main__":
    window = Tk()
    window.wm_title("Simple Mail Bomber")
    window.geometry("452x686")
    window.configure(bg="#000000")
    main_frame = MainFrame(window)
    window.resizable(False, False)
    window.mainloop()
