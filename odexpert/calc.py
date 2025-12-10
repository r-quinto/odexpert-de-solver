import customtkinter as ctk
import tkinter.messagebox as messagebox

import logic


class HomePage:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.configure(fg_color="#1f212e")
        self.root.title('DE Calculator')
        self.root.geometry('500x600')
        self.equation1 = ctk.StringVar()
        self.equation2 = ctk.StringVar()

        self.enter1 = ""
        self.enter2 = ""
        self.active_entry = ""
        self.call = logic.FinalHomoExact()



        text_frame = ctk.CTkFrame(self.root, fg_color="#1f212e")
        text_frame.grid(row=0, column=0, columnspan=7, pady=4)

        frame1 = ctk.CTkFrame(text_frame, fg_color="#1f212e")
        frame1.pack(side="top")

        label1 = ctk.CTkLabel(frame1, text="ODE", text_color="#FFC045", font=("Stencil", 30, "bold"))
        label1.pack(side="left")

        label2 = ctk.CTkLabel(frame1, text="XPERT", text_color="white", font=("Stencil", 30, "bold"))
        label2.pack(side="left")

        frame_1_label = ctk.CTkLabel(master=text_frame, text="ORDER ONE DIFFERENTIAL EQUATION",
                                     font=("TW Cen MT", 15, "bold"), text_color="white")
        frame_1_label.pack(side="top")

        entry_frame = ctk.CTkFrame(master=text_frame, width=470, height=50, fg_color="#1f212e")
        self.entry = ctk.CTkEntry(master=entry_frame, height=50, width=225, placeholder_text="Input: ",
                             textvariable=self.equation1, fg_color="#04040d", text_color='grey',
                             border_width=0, state="disabled")
        self.entry.pack(side="left", padx=5)
        self.entry_2 = ctk.CTkEntry(master=entry_frame, height=50, width=225, placeholder_text="Input: ",
                               textvariable=self.equation2, fg_color="#04040d", text_color='grey',
                               border_width=0, state="disabled")
        self.entry_2.pack(side="left", padx=5)
        entry_frame.pack()

        answer_frame = ctk.CTkFrame(self.root, fg_color="#04040d", width=475, height=80, border_width=0)
        answer_frame.grid(row=2, column=0, columnspan=7, pady=5, padx=15, sticky="w")

        self.answer_label = ctk.CTkLabel(master=answer_frame, text=" ", font=("Fira Sans", 14))
        self.answer_label.place(x= 20, y= 20, anchor="w")

        self.answer_label2 = ctk.CTkLabel(master=answer_frame, text="Answer: ", text_color='grey',font=("Fira Sans", 14))
        self.answer_label2.place(x=20, y= 40, anchor="w")

        frame2 = ctk.CTkFrame(self.root, fg_color="#04040d", width=360, height=900)
        frame2.grid(row=3, column=0, columnspan=7, pady=10, padx=10, sticky="w")

        button_1 = ctk.CTkButton(master=frame2, text='1', command=lambda: self.click(1), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_1.grid(row=5, column=0, padx=5, pady=5)

        button_2 = ctk.CTkButton(master=frame2, text='2', command=lambda: self.click(2), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_2.grid(row=5, column=1, padx=5, pady=5)

        button_3 = ctk.CTkButton(master=frame2, text='3', command=lambda: self.click(3), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_3.grid(row=5, column=2, padx=5, pady=5)

        button_4 = ctk.CTkButton(master=frame2, text='4', command=lambda: self.click(4), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_4.grid(row=4, column=0, padx=5, pady=5)

        button_5 = ctk.CTkButton(master=frame2, text='5', command=lambda: self.click(5), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_5.grid(row=4, column=1, padx=5, pady=5)

        button_6 = ctk.CTkButton(master=frame2, text='6', command=lambda: self.click(6), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_6.grid(row=4, column=2, padx=5, pady=5)

        button_7 = ctk.CTkButton(master=frame2, text='7', command=lambda: self.click(7), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_7.grid(row=3, column=0, padx=5, pady=5)

        button_8 = ctk.CTkButton(master=frame2, text='8', command=lambda: self.click(8), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_8.grid(row=3, column=1, padx=5, pady=5)

        button_9 = ctk.CTkButton(master=frame2, text='9', command=lambda: self.click(9), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_9.grid(row=3, column=2, padx=5, pady=5)

        button_0 = ctk.CTkButton(master=frame2, text='0', command=lambda: self.click(0), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        button_0.grid(row=6, column=0, padx=5, pady=5)

        plus_button = ctk.CTkButton(master=frame2, text='+', command=lambda: self.click('+'), height=50, width=50,
                                    font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        plus_button.grid(row=5, column=3, padx=5, pady=5)

        minus_button = ctk.CTkButton(master=frame2, text='-', command=lambda: self.click('-'), height=50, width=50,
                                     font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        minus_button.grid(row=6, column=3, padx=5, pady=5)

        multiply_button = ctk.CTkButton(master=frame2, text='*', command=lambda: self.click('*'), height=50, width=50,
                                        font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        multiply_button.grid(row=4, column=3, padx=5, pady=5)

        divide_button = ctk.CTkButton(master=frame2, text='/', command=lambda: self.click('/'), height=50, width=50,
                                      font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        divide_button.grid(row=3, column=3, padx=5, pady=5)

        decimal_button = ctk.CTkButton(master=frame2, text='.', command=lambda: self.click('.'), height=50, width=50,
                                       font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        decimal_button.grid(row=6, column=1, padx=5, pady=5)

        del_button = ctk.CTkButton(master=frame2, text='del', command=self.delete, height=50, width=110,
                                   font=("Fira Sans", 16), fg_color='#FFC045', text_color="#04040d")
        del_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        clear_button = ctk.CTkButton(master=frame2, text='Clear', command=self.clear, height=50, width=110,
                                     font=("Fira Sans", 16), fg_color='#FFC045', text_color="#04040d")
        clear_button.grid(row=3, column=6, columnspan=2, padx=5, pady=5)

        e_button = ctk.CTkButton(master=frame2, text='e', command=lambda: self.click('e'), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#2D4356")
        e_button.grid(row=7, column=4, padx=5, pady=5)

        x_button = ctk.CTkButton(master=frame2, text='x', command=lambda: self.click('x'), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#2D4356")
        x_button.grid(row=5, column=4, padx=5, pady=5)

        y_button = ctk.CTkButton(master=frame2, text='y', command=lambda: self.click('y'), height=50, width=50,
                                 font=("Fira Sans", 16), fg_color="#2D4356")
        y_button.grid(row=6, column=4, padx=5, pady=5)

        ln_button = ctk.CTkButton(master=frame2, text='ln', command=lambda: self.click('ln('), height=50, width=50,
                                  font=("Fira Sans", 16), fg_color="#2D4356")
        ln_button.grid(row=4, column=4, padx=5, pady=5)

        sin_button = ctk.CTkButton(master=frame2, text='sin', command=lambda: self.click('sin('), height=50, width=50,
                                   font=("Fira Sans", 16), fg_color="#2D4356")
        sin_button.grid(row=5, column=5, padx=5, pady=5)

        cos_button = ctk.CTkButton(master=frame2, text='cos', command=lambda: self.click('cos('), height=50, width=50,
                                   font=("Fira Sans", 16), fg_color="#2D4356")
        cos_button.grid(row=4, column=5, padx=5, pady=5)

        dx_button = ctk.CTkButton(master=frame2, text='dx', command=self.set_entry1, height=50, width=50,
                                   font=("Fira Sans", 16), fg_color="#FFC045",  text_color="#04040d")
        dx_button.grid(row=2, column=4, padx=5, pady=5)

        log_button = ctk.CTkButton(master=frame2, text='log', command=lambda: self.click('log('), height=50, width=50,
                                   font=("Fira Sans", 16), fg_color="#2D4356")
        log_button.grid(row=3, column=4, padx=5, pady=5)

        par1_button = ctk.CTkButton(master=frame2, text='(', command=lambda: self.click('('), height=50, width=50,
                                    font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        par1_button.grid(row=7, column=2, padx=5, pady=5)

        par2_button = ctk.CTkButton(master=frame2, text=')', command=lambda: self.click(')'), height=50, width=50,
                                    font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        par2_button.grid( row=7, column=3, padx=5, pady=5)

        exp_button = ctk.CTkButton(master=frame2, text='^', command=lambda: self.click('^'), height=50, width=50,
                                      font=("Fira Sans", 16), fg_color="#dcd7c9", text_color="#04040d")
        exp_button.grid(row=6, column=2, padx=5, pady=5)

        solve_button = ctk.CTkButton(master=frame2, text='Solve', command=self.equal, height=50, width=110,
                                     font=("Fira Sans", 16), fg_color='#FFC045', text_color="#04040d")
        solve_button.grid(row=2, column=6, columnspan=2, padx=5, pady=5)

        tan_button = ctk.CTkButton(master=frame2, text='tan', command=lambda: self.click('tan('), height=50, width=50,
                                  font=("Fira Sans", 16), fg_color='#2D4356')
        tan_button.grid(row=6, column=5, padx=5, pady=5)

        cot_button = ctk.CTkButton(master=frame2, text='cot', command=lambda: self.click('cot('), height=50, width=50,
                                  font=("Fira Sans", 16), fg_color='#2D4356')
        cot_button.grid(row=6, column=6, padx=5, pady=5)

        sec_button = ctk.CTkButton(master=frame2, text='sec', command=lambda: self.click('sec('), height=50, width=50,
                                   font=("Fira Sans", 16), fg_color='#2D4356')
        sec_button.grid(row=3, column=5, padx=5, pady=5)

        csc_button = ctk.CTkButton(master=frame2, text='csc', command=lambda: self.click('csc('), height=50, width=50,
                                   font=("Fira Sans", 16), fg_color='#2D4356')
        csc_button.grid(row=5, column=6, padx=5, pady=5)

        dy_button = ctk.CTkButton(master=frame2, text='dy', command=self.set_entry2, height=50, width=50,
                                   font=("Fira Sans", 16), fg_color='#FFC045', text_color="#04040d")
        dy_button.grid(row=2, column=5, padx=5, pady=5)

        atan_button = ctk.CTkButton(master=frame2, text='tan^-1', command=lambda: self.click('ARCTAN('), height=50,
                                    width=50,
                                    font=("Fira Sans", 13), fg_color='#2D4356')
        atan_button.grid(row=5, column=7, padx=5, pady=5)

        acos_button = ctk.CTkButton(master=frame2, text='cos^-1', command=lambda: self.click('ARCCOS('), height=50,
                                    width=50,
                                    font=("Fira Sans", 13), fg_color='#2D4356')
        acos_button.grid(row=4, column=6, padx=5, pady=5)

        asin_button = ctk.CTkButton(master=frame2, text='sin^-1', command=lambda: self.click('ARCSIN('), height=50,
                                    width=50,
                                    font=("Fira Sans", 13), fg_color='#2D4356')
        asin_button.grid(row=4, column=7, padx=5, pady=5)

        rt_button = ctk.CTkButton(master=frame2, text='n.rt', command=lambda: self.click('.rt('), height=50,
                                    width=50,
                                    font=("Fira Sans", 16), fg_color='#2D4356')
        rt_button.grid(row=6, column=7, padx=5, pady=5)

        pi_button = ctk.CTkButton(master=frame2, text='π', command=lambda: self.click('π'), height=50,
                                  width=50,
                                  font=("Fira Sans", 16), fg_color='#2D4356')
        pi_button.grid(row=7, column=5, padx=5, pady=5)

        sqrt_button = ctk.CTkButton(master=frame2, text='sqrt', command=lambda: self.click('sqrt('), height=50,
                                  width=50,
                                  font=("Fira Sans", 16), fg_color='#2D4356')
        sqrt_button.grid(row=7, column=6, padx=5, pady=5)
        cbrt_button = ctk.CTkButton(master=frame2, text='cbrt', command=lambda: self.click('cbrt('), height=50,
                                    width=50,
                                    font=("Fira Sans", 16), fg_color='#2D4356')
        cbrt_button.grid(row=7, column=7, padx=5, pady=5)

        solu = ctk.CTkButton(master=frame2, text='Show Solution', height=50, width=230, command= self.solution,
                                font=("Fira Sans", 16), fg_color='#152A38', text_color="white")
        solu.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

    def solution(self):
        call = logic.FinalHomoExact()
        try:
            m, n = self.equation1.get(), self.equation2.get()
            is_exact = call.is_exact(m, n)
            c1, c2, c3, c4, c5 = call.solve_exact(m, n)
            if is_exact:
                messagebox.showinfo("Solution ", f" dM/dy: {c4} \n dN/dx: {c5} \n Integration: {c1} \n Integration: {c2} \n General Solution: {c3}")
            else:
                messagebox.showinfo("No Solution", "NO SOLUTION!!!!!!!!!\n NOT EXACT!!!!!!!!")
        except Exception:
            self.answer_label2.configure(text="Invalid Input.", text_color="red")

    def set_entry1(self):
        self.entry.focus_set()
        self.active_entry = "Entry 1"

    def set_entry2(self):
        self.entry_2.focus_set()
        self.active_entry = "Entry 2"

    def equal(self):

        call = logic.FinalHomoExact()


        try:
            eq1 = self.equation1.get()
            eq2 = self.equation2.get()

            is_homogeneous, degree = call.isHomo(eq1, eq2)

            if is_homogeneous:
                self.answer_label.configure(text=f"The equation is homogeneous of degree {degree}.", text_color="green")

            else:
                self.answer_label.configure(text="The equation is not homogeneous.", text_color="red")


            exact = call.is_exact(eq1, eq2)

            if exact:
                self.answer_label2.configure(text=f"The equation is Exact.", text_color="green")
            else:
                self.answer_label2.configure(text=f"The equation is not Exact.", text_color="red")

        except Exception:
            self.answer_label.configure(text= " ")
            self.answer_label2.configure(text="Invalid Input. ", text_color="red")


    def click(self, value):
        if self.active_entry == "Entry 1":
            self.enter1 += str(value)
            self.equation1.set(self.enter1)
        if self.active_entry == "Entry 2":
            self.enter2 += str(value)
            self.equation2.set(self.enter2)

    def clear(self):
        if self.active_entry == "Entry 1":
            self.enter1 = ""
            self.equation1.set("")

        if self.active_entry == "Entry 2":
            self.enter2 = ""
            self.equation2.set("")

    def delete(self):
        if self.active_entry == "Entry 1":
            self.enter1 = self.enter1[:-1]
            self.equation1.set(self.enter1)

        if self.active_entry == "Entry 2":
            self.enter2 = self.enter2[:-1]
            self.equation2.set(self.enter2)

    def starting_func(self):
        self.root.mainloop()
