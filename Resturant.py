from menu import menu

class rest(menu):
    def get(self):
        super().additem()    
        super().showmenu()   
        super().modyfyitems()  
        super().orderitem()  
        super().showorder()  
        
