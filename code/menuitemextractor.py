from menuitem import MenuItem

if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    clean_price = price.replace('$','')
    return float(clean_price)

def clean_scraped_text(scraped_text: str) -> list[str]:

    pass # TODO  replace with code

def extract_menu_item(item_category:str, item_price: str, item_name:str, item_desc:str) -> MenuItem:
    menu_item = MenuItem(name = item_name, 
                    price = item_price, 
                    category= item_category, 
                    description=item_desc)
    return menu_item


if __name__=='__main__':
    pass
