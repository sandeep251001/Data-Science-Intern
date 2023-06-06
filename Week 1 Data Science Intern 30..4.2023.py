#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import numpy
import matplotlib.pyplot as plt


# In[2]:


inventory_file = "Med.json"


# In[3]:


def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as f:
            inventory = json.load(f)
    else:
        inventory = {}
    return inventory


# In[4]:


def save_inventory(inventory):
    with open(inventory_file, "w") as f:
        json.dump(inventory, f)


# In[5]:


def add_item(inventory, item_name, item_quantity):
    if item_name in inventory:
        inventory[item_name] += item_quantity
    else:
        inventory[item_name] = item_quantity


# In[6]:


def remove_item(inventory, item_name, item_quantity):
    if item_name in inventory:
        if inventory[item_name] >= item_quantity:
            inventory[item_name] -= item_quantity
        else:
            print("Error: Not enough quantity of item to remove.")
    else:
        print("Error: Item not found in inventory.")


# In[7]:


def get_total_quantity(inventory):
    return sum(inventory.values())


# In[8]:


def get_top_items(inventory):
    sorted_inventory = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    top_items = sorted_inventory[:5]
    return top_items


# In[9]:


inventory = load_inventory()
print("Initial inventory:", inventory)

while True:
    action = input("Do you want to add or remove items? Type 'add' or 'remove' (or 'done' to exit): ")
    
    if action == "add":
        item_name = input("Enter item name: ")
        item_quantity = int(input("Enter quantity to add: "))
        add_item(inventory, item_name, item_quantity)
        print(f"Added {item_quantity} {item_name}(s) to inventory.")
        print("Current inventory:", inventory)
        
    elif action == "remove":
        item_name = input("Enter item name: ")
        item_quantity = int(input("Enter quantity to remove: "))
        remove_item(inventory, item_name, item_quantity)
        print(f"Removed {item_quantity} {item_name}(s) from inventory.")
        print("Current inventory:", inventory)
        
    elif action == "done":
        break
        
    elif action == "clear":
        inventory = {}
        
    else:
        print("Invalid input. Please enter 'add', 'remove', 'clear', or 'done'.")

print("Total quantity of items:", get_total_quantity(inventory))
print("Top 5 items:", get_top_items(inventory))

save_inventory(inventory)
print("Inventory saved to file:", inventory_file)


# In[10]:


inventory = load_inventory()

item_names = list(inventory.keys())
item_quantities = list(inventory.values())

plt.pie(item_quantities, labels=item_names, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Current Inventory')
plt.show()


# In[ ]:




