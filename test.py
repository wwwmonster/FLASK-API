from dataclasses import dataclass
import uuid


def orderPizza(pizza, size, **kwargs):
    print(f"Ordering pizza with {pizza} and size {size}")
    if kwargs.get("extra_cheese"):
        print("Adding extra cheese")
    if kwargs.get("spicy"):
        print("Adding spicy toppings")
    else:
        print("No spicy toppings added")


orderPizza(
    "Margherita", "large", extra_cheese=True
)  # This will raise an error because 'Pizza' is not defined yet
