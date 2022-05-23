## 1. Tasks

Basic CRUD Functionality. :
Create inventory items,
Edit Them,
Delete Them,
View a list of them.
  
Create “shipments” and assign inventory to the shipment, and adjust inventory appropriately

## 2. Requirements
- Python3.7 
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.7
```
- Dependencies
```
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

## 3. Run the Script
```
$ py manage.py runserver 0.0.0.0:8000
```
## 4. Links

- Add new Items/view items --> [http://127.0.0.1:8000/items](http://127.0.0.1:8000/items)
- Add item to shipment/view shipment --> [http://127.0.0.1:8000/shipment](http://127.0.0.1:8000/shipment/)
- Update/Delete Items --> [http://127.0.0.1:8000/items/\<int: id\>](http://127.0.0.1:8000/items/\<id\>)
- Update/Delete  shipment item --> [http://127.0.0.1:8000/shipment/\<int: id\>](http://127.0.0.1:8000/shipment/\<id\>)

## 5. Comments

Supports: Adding new Item, view all items, view particular item, update/delete items.

Add an item to shipment - If shipment quantity is less than available quantity return "out of stock".
Update the remaining quantity of item in items db.

Standard delivery time: 10 days.

For Fast delivery: delivery time: 1 day, 10$ shipping charge.


