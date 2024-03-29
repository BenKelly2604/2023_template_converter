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
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        state=DISABLED,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

        # **** Remove when integrating !! ***
        self.to_history_button.config(state=NORMAL)

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
                                   height=200
                                   )
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, bg=background,
                                           text="history / Export",
                                           font=("Arial", "16", "bold"))
        self.history_heading_label.grid(row=0)

        # History text and label
        history_text = "Below are your recent calculations - " \
                       "showing 3 / 3 calculations. " \
                       " All calculations are shown to the nearest degree"
        self.text_instructions_label = Label(self.history_frame,
                                             text=history_text,
                                             width=45, justify="left",
                                             wraplength=300,
                                             padx=10, pady=10)
        self.text_instructions_label.grid(row=1)

        self.all_calcs_label = Label(self.history_frame,
                                     text="calculations go here",
                                     padx=10, pady=10, bg="#ffe6cc",
                                     width=40, justify="left")
        self.all_calcs_label.grid(row=2)

        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
                    "<Export>) or simply push <Export> to save your " \
                    "calculations in a text file. If the " \
                    "filename already exists, it will be overwritten!"
        self.save_instructions_label = Label(self.history_frame,
                                             text=save_text,
                                             justify="left", width=40,
                                             padx=10, pady=10)
        self.save_instructions_label.grid(row=3)

        # Filename entry widget, white background to start
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"),
                                    bg="#FFFFFF", width=25)
        self.filename_error_label.grid(row=4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame,
                                          text="Filename error goes here",
                                          fg="#9C0000",
                                          font=("Arial", "12", "bold"))
        self.filename_error_label.grid(row=5)

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
