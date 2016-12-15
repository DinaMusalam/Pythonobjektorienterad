# -*- coding: cp1252 -*-

import os
import view
import models

class HardwareProductRegistry:
    # create array for hardware and software so it will be easy then to show it .
    def __init__(self):
        self.__hardwarep=[]

    def add(self, hardwarep):
        self.__hardwarep.append(hardwarep)

    def get_all_product(self):
        return self.__hardwarep
        
class SoftwareProductRegistry:
    def __init__(self):
        self.__softwarep=[]

    def add(self, softwarep):
        self.__softwarep.append(softwarep)

    def get_all_product(self):
        return self.__softwarep

  
class Functions:        
# Standardfunktion för att ta emot endast int i input
# Indata: max (antalet val som kan göras), prompt (texten för input)
    def input_int(self, max=0, prompt="choose somthing: ", clear=True):
            correct = False
            while correct != True:
                try:
                        
                        choice = input(prompt)
                        if isinstance(choice, int):
                                if choice <= max:
                                    return choice
                                else:
                                    os.system('cls' if os.name=='nt' else 'clear') # check the operating system if its windows nt then kör cls or clear for other OS ( just to clean the screen )
                                    print "Wrong choice, tray again !!!! "
                                            
                except ValueError:
                        os.system('cls' if os.name=='nt' else 'clear')
                        print "Wrong data type , tray again with interger data !!!! "


    def input_int2(self, prompt="choose somthing: "):
            # Standardfunktion för att ta emot endast int or float  i input
            correct = False
            while correct != True:
                try:
                        
                        inputData = input(prompt)
                        if isinstance(inputData, float) or isinstance(inputData, int) :
                                return inputData
                        else:
                            print "Input data must be number , tray again !!!! "
                                            
                except ValueError:
                       print "Wrong data type , tray again with interger data !!!! "

                except NameError :
                        print "Wrong data type , tray again with interger data !!!! "
                    
    def show_data_file(self, filename = "results.txt"):
            # show the data from file 
            f = open("results.txt")
            all_lines = f.readlines()
            print " Filen har " , len ( all_lines), " rader : "
            print "\n", "-" * 30

            for line in all_lines:
                print  line , "\n"
            f.close()
            print "Done"

    def count_moms(self , amount):
        # Standardfunktion för att räckna ut moms 
        total = amount * 1.25
        return total
        
class ApplicationController:

    def __init__(self):
        self.__ui= view.UI()
        self.__hardware= models.HardWare()
        self.__software = models.SoftWare()
        self.__hregistry = HardwareProductRegistry()
        self.__sregistry = SoftwareProductRegistry()
        self.__functions = Functions()
        
    def run_menu(self):
        choice = None
        while choice != 0:
            self.__ui.main_menu()
            choice = self.__ui.get_main_menu_choice()
            if choice == 1:
                self.run_stuff_menu()
            elif choice == 2:
                # show product list for python
                self.__ui.show_product()
                self.show_all_hardware()
                self.show_all_software()
                
                
            elif choice == 3 :
                print "Show one product: "
                self.find_product()
                
            elif choice == 4 :
                print "save to file!!!"
                self.save_all_products()

            elif choice == 5 :
                self.__functions.show_data_file()

            elif choice == 6 :
                print "Show one product from file: "
                self.find_product_file()
                
        print "\n Thaks for using our system , se you soon :) \n"

    def run_stuff_menu(self):
        
        choice = -1
        while choice != 0:
            self.__ui.stuff_menu()
            choice = self.__ui.get_stuff_menu_choice()
            if choice == 1:
               self.__add_hardware_product() 
            elif choice == 2:
                self.__add_softdware_product()
        self.run_menu()


    def __add_hardware_product(self):
        print
        print "Add New Hardware Product... "
        print "-" * 30
        print 
        # get product info
        name= raw_input("Enter name: " )
        tillverkare= raw_input("Enter mainfactory: ")
        
        price= self.__functions.input_int2("Enter Price exkl moms: ")
        total_price = self.__functions.count_moms(price)
        print "Total Price inkl moms : ", total_price
        
        productNummer= raw_input("Enter product number: ")
        P = models.Product(name , tillverkare , price , productNummer )
        vikten = self.__functions.input_int2("Enter weight : ")
        if vikten > 25 :
            total_price = total_price + 200
            print "OBS !!! The weight over 25 so the rice will increas 200 .  "
            print "Price inkl moms and 200. New price is :  " , total_price 
        H = models.HardWare(name , tillverkare , total_price , productNummer,vikten )
        self.__hregistry.add(H)
        self.__ui.show_add_success()
        
        
        
        
        
    def __add_softdware_product(self):
        print
        print "Add New SoftWare Product... "
        print "-" * 30
        print
        # get product info
        name= raw_input("Enter name: " )
        tillverkare= raw_input("Enter mainfactory: ")
        
        price= self.__functions.input_int2("Enter Price exkl moms: ")
        total_price = self.__functions.count_moms(price)
        print "Total Price inkl moms : ", total_price
        
        productNummer= raw_input("Enter product number: ")
        P = models.Product(name , tillverkare , price , productNummer )
        medium= raw_input("Enter Medium : ")
        S = models.SoftWare(name , tillverkare , total_price , productNummer,medium )
        self.__sregistry.add(S)
        self.__ui.show_add_success()
        

    def show_all_hardware(self):
        #print "All hardware products !!!"
        for product in self.__hregistry.get_all_product():
            print product
        print  
        
    def show_all_software(self):
        #print "All software products !!!"
        for product in self.__sregistry.get_all_product():
            print product
        print 

    def save_all_products(self):
        # save to file
        f = open("results.txt", "a")
        for product in self.__hregistry.get_all_product():
            f.writelines (str(product))
        for product in self.__sregistry.get_all_product():
            f.writelines (str(product))
        
        f.close()
        self.__ui.show_save_success()

    def find_product_file(self):
        # find product in file
        num = input ("Type Number : ")  
        search = open("results.txt","r")
        for index, line in enumerate(search.readlines()):
           rad = index + 1
           if rad == num:
               print line

    def find_product(self):
        # find product 
        num = input ("Type Number : ")
        all_product =[]
        all_product = self.__hregistry.get_all_product() + self.__sregistry.get_all_product()
        # print all_product
        for index, line in enumerate(all_product):
           rad = index + 1
           if rad == num:
               print line  
                    
                    
        
