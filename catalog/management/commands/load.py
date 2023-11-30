import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('category.json', encoding='utf-8') as f:
            data_ = json.load(f)
            for category in data_:
                Category.objects.create(title=category["fields"]["title"],description=category["fields"]["description"])

        with open('product.json', encoding='utf-8') as f:
            data_ = json.load(f)
            for product in data_:
                category = Category.objects.get(id=product["fields"]["category"])
                Product.objects.create(title=product["fields"]["title"],description=product["fields"]["description"], image=product["fields"]["image"],
                                       category=category, price=product["fields"]["price"], date_of_creation=product["fields"]["date_of_creation"],
                                       last_modified_date=product["fields"]["last_modified_date"])




