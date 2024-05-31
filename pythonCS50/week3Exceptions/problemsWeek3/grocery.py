def main():
    items = count_items(get_items())
    for item in items:
        print(item)

#       get the items from the user
def get_items():

    item_list = []
    while True:
        try:
            items = str(input())
        except ValueError:
            print("please enter an item")
        except EOFError:
            break
        
        item_list.append(items)

    #sort the list
    item_list.sort()

    return item_list

#       count the items
def count_items(item_list):
    uniq_item_list = set(item_list)
    final_item_list = []
    count = 0
    for item in uniq_item_list:
        for item_l in item_list:
            if item == item_l:
                count = count +1 
        item_count = str(count) + " " + item.upper()
        final_item_list.append(item_count)
        count = 0
    return final_item_list

main()