from blog.models import LCategory
from django.core.management import BaseCommand

class Command(BaseCommand):
    help="This helps to insert the data"
    def handle(self, *args, **options):
        LCategory.objects.all().delete()
        category = [
            "Food",
            "Sports",
            "Technology",
            "Science",
            "Arts",
        ]

  
        for categories in category:
            LCategory.objects.create(d_category_name=categories)
        self.stdout.write(self.style.SUCCESS("Completed inserted data"))


 