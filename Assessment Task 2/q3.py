def add_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inventory: inventory[name]+=quantity
    else: inventory[name]=quantity
 
def remove_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inventory:
        if quantity>=inventory[name]:inventory[name]=0
        else:inventory[name]-=quantity
    else:inventory[name]=-1
 
def get_stock_report(inventory: dict) -> str:
    fordel=[]
    for i in inventory:
        if inventory[i]>0:
            print(f"{i}: {inventory[i]}")
        else:
            if inventory[i]>-1:
                print(f"({i} at 0 -- excluded)")
                fordel.append(i)
            else:
                print(f"(no error -- {i} never existed)")
                fordel.append(i)
    for i in fordel:
        del inventory[i]

inv={}
add_item(inv, 'apples', 10)
add_item(inv, 'bananas', 5)
get_stock_report(inv)
add_item(inv, 'apples', 5)
remove_item(inv, 'bananas', 10)
get_stock_report(inv)
remove_item(inv, 'oranges', 3)
get_stock_report(inv)
