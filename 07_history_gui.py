from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Five item list
        # self.all_calculations = ['0 F is -18 C', '0 C is 32 F',
        #                           '30 F is -1 C', '30C is 86 F','
        #                           '40 F is 4 C']

        # Six item list
        self.all_calculations = ['0 F is -18 C', '0 C is 32 F',
                                 '30 F is -1 C', '30C is 86 F',
                                 '40 F is 4 C', '100 C is 212 F']

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame,
                                        text="history",
                                        bg="#CC6600",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=0, padx=5, pady=5)

    def to_history(self):
        DisplayHistory(self)


class DisplayHistory:

    def __init__(self, partner):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300,
                                   height=200,
                                   bg=background)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, bg=background,
                                           text="history",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        history_text = "To use the video 11 2:18"

        self.history_text_label = Label(self.history_frame, bg=background,
                                        text=history_text, wraplength=350,
                                        justify="left")
        self.history_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes history dialogue (used by button and x at top of dialogue)
    def close_history(self, partner):
        # put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    Converter()
    root.mainloop()
