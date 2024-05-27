import tkinter as tk
import customtkinter as ctk
from Shop import Shop
from CTkTable import *


class Form:

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
        self.sorting_method_select = ctk.CTkComboBox(self.app)

        self.search_input = ctk.CTkEntry(self.app)
        self.search_combo_box = ctk.CTkComboBox(self.app)
        from data import Data
        self.data = Data()
        try:
            self.data.load_data()
        except Exception:
            print("Exception")
        self.table = self.display_data_in_table(self.data.data_list)
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

        refresh_button = ctk.CTkButton(self.input_frame, width=80, height=40, text="Refresh", text_color="#2F2F2F",
                                      font=("Arial", 14), bg_color="#2F2F2F", fg_color="#FA7328", corner_radius=45,
                                      command= lambda: self.refresh(self.data.data_list))
        refresh_button.place(relx=0.75, rely=0.7, anchor="nw")

        combo_box_options = ["Bubble", "Shaker", "Insertion", "Selection", "Shell (Sedgewick)", "Shell (Knuth)", "Quick sort", "Heap (1)", "Heap (2)"]
        self.sorting_method_select = ctk.CTkComboBox(self.app, width=150, height=30, bg_color="#1F1F1F", fg_color="#FA7328",
                                                text_color="#1F1F1F", corner_radius=45, values=combo_box_options)
        self.sorting_method_select.place(relx=0.6, rely=0.6, anchor="e")

        sort_button = ctk.CTkButton(self.app, width=100, height=40, bg_color="#1F1F1F", fg_color="#FA7328",
                                    text_color="#1F1F1F", corner_radius=45, font=("Arial", 14), text="Sort", command=self.sort_ocl)
        sort_button.place(relx=0.7, rely=0.6, anchor="e")


        self.search_input = ctk.CTkEntry(self.app, width=400, bg_color="#2F2F2F", fg_color="#4F4F4F", height=30,
                                     corner_radius=45, placeholder_text="Enter an overall sold value for search")
        self.search_input.place(relx=0.1, rely=0.6, anchor="w")

        self.search_combo_box = ctk.CTkComboBox(self.app, width=150, height=30, bg_color="#1F1F1F", fg_color="#FA7328",
                                                text_color="#1F1F1F", corner_radius=45, values=['Binary', 'Interpolation'])
        self.search_combo_box.place(relx=0.1, rely=0.7, anchor="w")

        search_button = ctk.CTkButton(self.app, width=100, height=40, bg_color="#1F1F1F", fg_color="#FA7328",
                                    text_color="#1F1F1F", corner_radius=45, font=("Arial", 14), text="Search", command=self.search_ocl)
        search_button.place(relx=0.3, rely=0.7, anchor="w")


    def display_data_in_table(self, list):
        # Create the table
        table = CTkTable(master=self.table_frame, column=2, colors=["#1F1F1F", "#2F2F2F"], header_color="#FA7328",
                         command=self.row_on_click)
        table.insert(row=0, column=0, value="Name")
        table.insert(row=0, column=1, value="Overall sold")
        # Insert the data into the table
        row_index = 1

        for obj in list:
            table.add_row(index=row_index, values=[obj.name, obj.overall_sold])
            row_index += 1

        return table

    def refresh(self, list):
        self.data.load_data()
        self.table.destroy()
        self.table = self.display_data_in_table(list)
        self.table.pack(expand=True, fill="both")

    def clear_text_boxes(self):
        self.name_text_box.delete(0, 'end')
        self.total_sold_box.delete(0, 'end')

    def submit(self):
        obj = Shop(self.name_text_box.get(), self.total_sold_box.get())
        self.data.data_list.append(obj)
        self.data.save_data()
        self.table.destroy()
        self.table = self.display_data_in_table(self.data.data_list)
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
        self.data.data_list.__delitem__(self.selected_row_index-1)
        self.table.delete_row(self.selected_row_index)
        self.selected_row_index = 1
        print("Deleted")

    def sort_ocl(self):
        method = self.sorting_method_select.get()
        if method.__eq__("Bubble"):
            from Sorting import BubbleSort as Bs
            bs = Bs()
            self.data.data_list = bs.sort()
        if method.__eq__("Shaker"):
            from Sorting import ShakerSort as Ss
            ss = Ss()
            self.data.data_list = ss.sort()
        if method.__eq__("Insertion"):
            from Sorting import InsertionSort
            insertion_sort = InsertionSort()
            self.data.data_list = insertion_sort.sort()
        if method.__eq__("Selection"):
            from Sorting import SelectionSort
            selection_sort = SelectionSort()
            self.data.data_list = selection_sort.sort()
        if method.__eq__("Shell (Sedgewick)"):
            from Sorting import ShellSort
            shell_sort = ShellSort()
            self.data.data_list = shell_sort.sort(gap_sequence="sedgewick")
        if method.__eq__("Shell (Knuth)"):
            from Sorting import ShellSort
            shell_sort = ShellSort()
            self.data.data_list = shell_sort.sort(gap_sequence="knuth")
        if method.__eq__("Quick sort"):
            from Sorting import QuickSort
            quick_sort = QuickSort()
            self.data.data_list = quick_sort.sort()
        if method.__eq__("Heap (1)"):
            from Sorting import HeapSortWithFormula1
            heap_sort = HeapSortWithFormula1()
            self.data.data_list = heap_sort.sort()
        if method.__eq__("Heap (2)"):
            from Sorting import HeapSortWithFormula2
            heap_sort = HeapSortWithFormula2()
            self.data.data_list = heap_sort.sort()

        self.table.destroy()
        self.table = self.display_data_in_table(self.data.data_list)
        self.table.pack(expand=True, fill="both")

    def search_ocl(self):
        match self.search_combo_box.get():
            case 'Binary':
                from Search import BinarySearch
                search = BinarySearch(self.data.data_list, 0, len(self.data.data_list)-1, self.search_input.get())
                result_index = search.search()
                list = [self.data.data_list[result_index]]
                print(self.data.data_list)
                self.refresh(list)
            case 'Interpolation':
                from Search import InterpolationSearch
                search = InterpolationSearch(self.data.data_list, 0, len(self.data.data_list) - 1,
                                             self.search_input.get())
                result_index = search.search()
                if result_index != -1:
                    list = [self.data.data_list[result_index]]
                    print(self.data.data_list)
                    self.refresh(list)
                else:
                    print("Element not found")
