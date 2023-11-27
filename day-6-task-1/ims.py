from abc import abstractmethod
def display(sorted_list):
    for s in sorted_list:
        print(f"\nname:{s._name}\nprice:{s._price}\ncategory:{s._category}\nquantity:{s._quantity}\n".center(100, "*"))



class InventoryItem:
    items=[]
    def __init__(self, name, price, quantity, category):
        self._name=name
        self._price=price
        self._quantity=quantity
        self._category=category
    

    @abstractmethod
    def report_low_stock(self):
        pass
        


    @abstractmethod
    def sort_items(self):
        pass

    def remove(self):
        name=str(input("Enter name of item to be removed: ")).strip().lower()
        for i in self.items:
            if i._name.lower()==name:
                self.items.remove(i)
            else:
                print("item not found")
    def view(self):
        if self.items:
            sorted_list = self.sort_items()
            display(sorted_list)
        else:
            print("No Items currently")


    def update(self):

        if self.items:
            name=str(input("Enter name of item to be updated: ")).strip().lower()
            sorted_list = self.sort_items()
            for item in sorted_list:
                try:
                    if item._name.lower()==name:
                        name=str(input("Enter name of item: ")).strip()
                        price=input("Enter price of item: ").strip()
                        quantity=input("Enter quantity of item: ").strip()
                        if name:
                            item._name=name
                        if price:
                            a=int(price)
                            if a >0:
                                item._price=a
                            
                        if quantity:
                            b=int(quantity)
                            if b>0:
                                item._quantity=b
                    else:
                        print("Item Not Found;")
                except Exception as e:
                    price(e)

        else:
            print("No Items to update")


class Item(InventoryItem):
    def __init__(self, name, price, quantity, category):
        super().__init__(name, price, quantity,category)

    def report_low_stock(self):
        i= [item for item in self.items if item._quantity<10]
        return i
    
    def sort_items(self):
        return sorted(self.items,key=lambda x:x._price)
    
    def add(self):
        name=str(input("Enter name of item: ")).strip()
        price=int(input("Enter price of item: "))
        quantity=int(input("Enter quantity of item: "))
        if price > 0 and quantity > 0:
            item = Item(name, price, quantity, self._category)
            self.items.append(item)
        else:
            print("Invalid price or quantity. Both must be greater than 0.")



electronics=Item("",0,0,"electronics")
clothes=Item("",0,0,"clothes")
def show_help(show=False):
    if show:
        print(
        '''
        • add \n
        • remove\n
        • update\n
        • view\n
        • report\n
        • help\n
        • exit\n
        '''
        )
show_help(True)
try:
    while True:
        command=str(input("enter command: ")).strip().lower()

        
        match command:
            case "add":    
                cat=str(input("choose category\nc->clothes\ne->electronics: \n")).strip().lower()
                if cat !="c" and cat !='e':
                    print("Invalid category")
                    continue           
                electronics.add() if cat=='e' else clothes.add()

            case "remove":
                electronics.remove()
            case "view":
                electronics.view() 
            case "update":
                electronics.update()
            case "report":
                items=electronics.report_low_stock()
                display(items)
            case _:
                print("Invalid command")
                show_help(True)
            


except Exception as e:
    print(e)