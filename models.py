# -*- coding: cp1252 -*-

class Product:
    def __init__(self, name = "unknown" , tillverkare = "unknown" , price = 0, productNummer = "unknown"):
        self.__name = name
        self.__tillverkare= tillverkare
        self.__price = price
        self.__productNummer = productNummer
        
    def set_name(self,new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
     
    def set_tillverkare(self, new_tillverkare):
        self.__age = new_tillverkare
      
    def get_tillverkare(self):
        return self.__tillverkare

    def set_price(self, new_price):
        self.__price = new_price

    def get_price(self):
        return self.__price

    def set_productNummer(self, new_productNummer):
        self.__productNummer = new_productNummer

    def get_productNummer(self):
        return self.__productNummer
        
    def __str__(self):
        return  self.__name +"\t"+ self.__tillverkare +"\t"+ str(self.__price) +"\t"+ self.__productNummer

class HardWare(Product):
    def __init__(self, name = "unknown" , tillverkare = "unknown" , price = 0, productNummer = "unknown", vikten = 0):
        Product.__init__(self, name , tillverkare, price, productNummer)
        self.__vikten = vikten

    def set_vikten(self, new_vikten):
        self._vikten = new_vikten

    def get_vikten(self):
        return self.__vikten
    
                
    def __str__(self, filename = "results.txt"):
        return  "Product name: "+ str(self.get_name()) +"\t"+ "MainFactory: " + str(self.get_tillverkare()) +"\t"+"Price: "+ str(self.get_price()) + " KR "+ "\t"+"Product number: "+ str(self.get_productNummer()) +"\t"+"Weight: "+  str(self.__vikten)+" K " +"\n"       
                     

class SoftWare(Product):
    def __init__(self, name = "unknown" , tillverkare = "unknown" , price = 0, productNummer = "unknown", medium = "unknown"):
        Product.__init__(self, name , tillverkare, price, productNummer)
        self.__medium = medium
        
    def set_medium(self, new_medium):
        self.__medium= new_medium

    def get_medium(self):
        return self.__medium

        
    def __str__(self):
        return   "Product name: "+ str(self.get_name()) +"\t"+ "MainFactory: " + str(self.get_tillverkare()) +"\t"+"Price: "+ str(self.get_price()) +" KR " +"\t"+"Product number: "+ str(self.get_productNummer()) +"\t"+ "Medium: "+  self.__medium + "\n"


    
