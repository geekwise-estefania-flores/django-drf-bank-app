from django.db import models

#Account model
class Account(models.Model):
    account_number = models.CharField(max_length = 4)

#branch model
class Branch(models.Model):
  
  class Meta:
    verbose_name_plural = "branches"

  bank = models.ForeignKey('auth.User', related_name='bank', null=True,
    on_delete=models.CASCADE)

  def __str__(self):
    return self.bank


#customer model
class Customer(models.Model):
  customer_name = models.CharField(max_length = 30)
  customer_email = models.EmailField(max_length = 100)

  account = models.ForeignKey('auth.User', related_name='account', null=True,
    on_delete=models.CASCADE)

  def __str__(self):
    return self.account

#product model
class Product(models.Model):
  
  product_options = (
    ('savings', 'SAVINGS'),
    ('checking', 'CHECKING'),
    )
  card_options = (
    ('debit', 'DEBIT'),
    ('credit', 'CREDIT')
  )
  product_options = models.CharField(max_length = 8, choices = product_options, default = product_options[0])

  card_options = models.CharField(max_length = 8,
  choices = card_options, default = card_options[0])

  product = models.OneToOneField(
    Branch, 
    on_delete=models.CASCADE, 
    primary_key=True)

  def __str__(self):
    return self.bank
