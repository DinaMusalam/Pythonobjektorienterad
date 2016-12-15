# -*- coding: cp1252 -*-

import controller

class UI:

        def main_menu(self):
                print """\t WELCOME TO PRODUCT COMPANY
 ----------------------------------------
    1. Add product.
    2. Show product list.
    3. Show (one) product.
    4. Save Product list to a text file.
    5. Show product list from text file.
    6. Show one product list from file. 
    0. Finish. """
                        
        def stuff_menu(self):
                print """\t Add menu
-------------------------------
    1. Add hard ware
    2. Add soft ware
    0. Go back """

        def get_main_menu_choice(self):
                xu = controller.Functions()
                choice = xu.input_int(6, "Write your choice: ", False)
                return choice

        def get_stuff_menu_choice(self):
                xu = controller.Functions()
                choice = xu.input_int(3, "Write your choice: ", False)
                return choice

        def show_product(self):
                print
                print "All Products "
                print "*" * 20               
                

        def show_add_success(self):
                print
                print "Added!!!"
        def show_save_success(self):
                print
                print "Saved!!!"
        def show_open_file(self):
                print
                print "Text file oppend!!!"
                controller.Functions.show_data_file()

        



