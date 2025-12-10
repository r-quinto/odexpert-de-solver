import tkinter as tk
import calc


class LoadingScreen:
    def __init__(self):
        self.root = tk.Tk()

        width_window = 427
        height_window = 250
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2) - (width_window / 2))
        y = int((screen_height / 2) - (height_window / 2))

        self.root.geometry(f"{width_window}x{height_window}+{x}+{y}")
        self.root.overrideredirect(1)


        tk.Frame(self.root, width=427, height=250, bg='#1f212e').place(x=0, y=0)

        frame1 = tk.Frame(self.root, bg="#1f212e")
        frame1.place(x=103, y=80)

        label1 = tk.Label(frame1, text="ODE", fg="#FFC045", bg="#1f212e", font=("Stencil", 30, "bold"))
        label1.pack(side="left")

        label2 = tk.Label(frame1, text="XPERT", fg="white", bg="#1f212e", font=("Stencil", 30, "bold"))
        label2.pack(side="left")

        label3 = tk.Label(self.root, text='Code, Click, Calculate', fg='white', bg='#1f212e', font=("TW Cen MT", 12, "bold"))
        label3.place(x=137, y=123)

        label4 = tk.Label(self.root, text='Loading...', fg='white', bg='#1f212e', font=("Calibri", 11))
        label4.place(x=10, y=215)

        self.frame2 = tk.Frame(self.root, bg="#1f212e", width=160, height=20, highlightbackground="white", highlightthickness=1)
        self.frame2.place(x=133, y=165)
    def start_calc_window(self):
        self.root.destroy()
        q = calc.HomePage()
        q.starting_func()

    def loading_animation(self, step=0):
        if step > 15:
            self.start_calc_window()
            return

        for j in range(step):
            label = tk.Label(self.frame2, text="■", fg="white", bg="#1f212e", border=0, relief=tk.SUNKEN)
            label.place(x=2 + (j * 10), y=0)

        self.root.after(275, self.loading_animation, step + 1)

    def run(self):
        self.root.after(100, self.loading_animation)
        self.root.mainloop()



r = LoadingScreen()
r.run()
