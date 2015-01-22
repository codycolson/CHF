from django.db import models
from polymorphic import PolymorphicModel

class Address(models.Model):
    address1 = models.TextField(max_length=30)
    address2 = models.TextField(max_length=30)
    city = models.TextField(max_length=30)
    state = models.TextField(max_length=30)
    zip = models.DecimalField(max_digits=5, decimal_places=0)

class Legal_Entity(models.Model):
    given_name = models.TextField(max_length=30)
    account_creation_date = models.DateField()
    contact = models.TextField(max_length=30)
    email = models.TextField(max_length=50)
    address = models.ForeignKey(Address, related_name='+')

class Person(Legal_Entity):
    '''
    Every person that has an account on the system.
    '''
    last_name = models.TextField(max_length=30)
	
class Organization(Legal_Entity):
    '''
    
    '''
    organization_type = models.TextField(max_length=30)
	
class Phone(models.Model):
    '''
    
    '''
    number = models.IntegerField()
    extension = models.IntegerField()
    type = models.TextField(max_length=30)
    legal_entity = models.ForeignKey(Legal_Entity, related_name='+')    
    
    def __str__(self):              
    # __unicode__ on Python 2
        return self.name
    
class Item(models.Model):
    '''
    
    '''
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    standard_rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    legal_entity = models.ForeignKey(Legal_Entity, related_name='+')
	
class Wardrobe_Item(Item):
    '''
    
    '''
    size = models.TextField(max_length=30)
    size_modifier = models.TextField(max_length=30)
    gender = models.TextField(max_length=30)
    color = models.TextField(max_length=30)
    pattern = models.TextField(max_length=30)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    note = models.TextField(max_length=200)
	
class Rentable_Item(Item):
    '''
    
    '''
	
class Rental(models.Model):
    '''
    
    '''
    rental_time = models.DateField()
    due_date = models.DateField()
    discount_percent = DecimalField(max_digits=3, decimal_places=2)
    rented_item = models.ManyToManyField(Rentable_Item, through='Rented_Item')
	
class Rented_Item(models.Model):
    '''
    
    '''
    condition = models.TextField(max_length=30)
    new_damage = models.TextField(max_length=30)
    damage_fee = models.DecimalField(max_digits=10, decimal_places=2)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2)
    rentable_item = models.ForeignKey(Rentable_Item)
    rental = models.ForeignKey(Rental)

class Return(models.Model):
    '''
    
    '''
    return_time = models.DateField()
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
	
class Area(models.Model):
    '''
    
    '''
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200)
    place_number = models.IntegerField() 
    
    def __str__(self):
        return self.name
	
class Sale_Item(models.Model):
    '''
    
    '''
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=200)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.ForeignKey(Area)
	
class Event(models.Models):
    '''
    
    '''
    start_date = models.DateField()
    end_date = models.DateField()
    map_file_name = models.TextField(max_length=30)
	
class Public_Event(Event):
    '''
    
    '''
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=30)
    
class Venue(models.Model):
    '''
    
    '''
    name = models.TextField(max_length=30)
    address = models.ForeignKey(Address, related_name='+')
    
class Order(models.Model):	
    '''
    
    '''
    order_date = models.DateField()
    date_packed = models.DateField()
    date_paid = models.DateField()
    date_shipped = models.DateField()
    tracking_number = models.IntegerField()
	
class Product(PolymorphicModel):
    '''
    
    '''
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=30)
    category = models.TextField(max_length=30)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    legal_entity = models.ForeignKey(Legal_Entity)
	
class Bulk_Product(Product):
    '''
    
    '''
    quantity_on_hand = models.TextField(max_length=30)
    bulk_detail = models.ManyToManyField(Order, through='Bulk_Detail')
    
class Individual_Product(Product):
    '''
    
    '''
    date_made = models.DateField()
	
class Personal_Product(Product):
    '''
    
    '''
    order_form_name = models.TextField(max_length=30)
    production_time = models.TextField(max_length=30)
    personal_detail = models.ManyToManyField(Order, through='Personal_Detail')
	
class Bulk_Detail(models.Model):
    '''
    
    '''
    quantity = models.TextField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bulk_product = models.ForeignKey(Bulk_Product)
    order = models.ForeignKey(Order)
	
class Personal_Detail(models.Model):
    '''
    
    '''
    order_file = models.TextField(max_length=30)
    personal_product = models.ForeignKey(Personal_Product)
    order = models.ForeignKey(Order)

class Vendor(models.Model):
    '''
    A vendor (supplier) of products in our catalog.
    Note that related_name='+' disables navigation across the foreign key.
    This is how you can implement the navigation visibilty found in your DCD.
    If there isn't a navigation visibility on an association, turn off Django's
    automatic backward navigation.  In this case, we can get to Address from
    Vendor, but Address won't be able to retrieve an associated Vendor.
    '''
    name = models.TextField(max_length=30)
    phone = models.TextField(max_length=30)
    contact = models.TextField(max_length=30)
    address = models.ForeignKey(Address, related_name='+')


class ProductSpecification(models.Model):
    '''
    A product specification that describes an entry in the product catalog.
    '''
    name = models.TextField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    manufacturer = models.TextField(max_length=30)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    commission_rate = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.TextField(max_length=30)
    category = models.ForeignKey(Category)
    vendors = models.ManyToManyField(Vendor, related_name='+')
