import tkinter as tk
import customtkinter as ctk
from Shop import Shop
from CTkTable import *


class Sort:

    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1920x1080")
        self.app.configure(fg_color="#1F1F1F")
        self.app.title("Sorting")

        self.input_frame = ctk.CTkFrame(self.app)
        self.name_text_box = ctk.CTkEntry(self.input_frame)
        self.total_sold_box = ctk.CTkEntry(self.input_frame)

        self.table_frame = ctk.CTkScrollableFrame(self.app, height=400, width=600, bg_color="#1F1F1F", fg_color="#1F1F1F")
        self.table_frame.place(relx=0.85, rely=0.05, anchor="ne")
        from data import data
        self.table = self.display_data_in_table(data, self.table_frame)
        self.table.pack(padx=20, pady=20, expand=True, fill="both")
        self.selected_row_index = 1
        self.run()
        self.app.mainloop()

    def run(self):

        self.input_frame.configure(self.app, height=200, width=500, bg_color="#1F1F1F", fg_color="#2F2F2F")
        self.input_frame.place(relx=0.05, rely=0.05, anchor="nw")

        self.name_text_box.configure(self.input_frame, width=400, bg_color="#2F2F2F", fg_color="#4F4F4F", height=30,
                                     corner_radius=45, placeholder_text="Enter cashier name")
        self.name_text_box.place(relx=0.05, rely=0.1, anchor="nw")

        self.total_sold_box.configure(self.input_frame, width=400, bg_color="#2F2F2F", fg_color="#4F4F4F", height=30,
                                     corner_radius=45, placeholder_text="Enter total sold value")
        self.total_sold_box.place(relx=0.05, rely=0.4, anchor="nw")

        submit_button = ctk.CTkButton(self.input_frame, width=80, height=40, text="Submit", text_color="#2F2F2F",
                                      font=("Arial", 14), bg_color="#2F2F2F", fg_color="#FA7328", corner_radius=45, command=self.submit)
        submit_button.place(relx=0.05, rely=0.7, anchor="nw")

        clear_button = ctk.CTkButton(self.input_frame, width=80, height=40, text="Clear", text_color="#2F2F2F",
                                     font=("Arial", 14), bg_color="#2F2F2F", fg_color="#FA7328",
                                     command=self.clear_text_boxes, corner_radius=45)
        clear_button.place(relx=0.3, rely=0.7, anchor="nw")

        delete_button = ctk.CTkButton(self.input_frame, width=80, height=40, text="Delete", text_color="#2F2F2F",
                                      font=("Arial", 14), bg_color="#2F2F2F", fg_color="#FA7328", corner_radius=45,
                                      command=self.delete_row)
        delete_button.place(relx=0.55, rely=0.7, anchor="nw")

        combo_box_options = ["Bubble", "Shaker"]
        sorting_method_select = ctk.CTkComboBox(self.app, width=150, height=30, bg_color="#1F1F1F", fg_color="#FA7328",
                                                text_color="#1F1F1F", corner_radius=45, values=combo_box_options)
        sorting_method_select.place(relx=0.6, rely=0.6, anchor="e")

        sort_button = ctk.CTkButton(self.app, width=100, height=40, bg_color="#1F1F1F", fg_color="#FA7328",
                                    text_color="#1F1F1F", corner_radius=45, font=("Arial", 14), text="Sort")
        sort_button.place(relx=0.7, rely=0.6, anchor="e")

    def display_data_in_table(self, data, root):
        # Create the table
        table = CTkTable(master=root, column=2, colors=["#1F1F1F", "#2F2F2F"], header_color="#FA7328",
                         command=self.row_on_click)
        table.insert(row=0, column=0, value="Name")
        table.insert(row=0, column=1, value="Overall sold")
        # Insert the data into the table
        row_index = 1

        for obj in data:
            table.add_row(index=row_index, values=[obj.name, obj.overall_sold])
            row_index += 1

        return table

    def clear_text_boxes(self):
        self.name_text_box.delete(0, 'end')
        self.total_sold_box.delete(0, 'end')

    def submit(self):
        obj = Shop(self.name_text_box.get(), self.total_sold_box.get())
        from data import data
        data.append(obj)
        self.table.destroy()
        self.table = self.display_data_in_table(data, self.table_frame)
        self.table.pack(expand=True, fill="both")

    def row_on_click(self, cell):
        selected_row = self.table.get_row(cell["row"])
        self.selected_row_index = cell["row"]

        name = selected_row[0]
        total_sold = selected_row[1]

        self.name_text_box.delete(0, tk.END)
        self.name_text_box.insert(0, name)

        self.total_sold_box.delete(0, tk.END)
        self.total_sold_box.insert(0, total_sold)

    def delete_row(self):
        from data import data
        data.__delitem__(self.selected_row_index-1)
        self.table.delete_row(self.selected_row_index)
        self.selected_row_index = 1
        print("Deleted")
