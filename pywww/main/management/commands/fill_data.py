from django.core.management.base import BaseCommand
from posts.models import Post
import faker

f = faker.Faker('pl-PL')


class Command(BaseCommand):
    help = "Dodaję 3 nowe posty."

    def handle(self, *args, **options):
        print(args)
        ile_postow = int(args[0])
        for _ in range(ile_postow):
            p = Post()
            p.title = f.paragraph(2)
            p.content = '\n\n'.join([f.paragraph(6) for _ in range(5)])
            p.published = f.boolean(80)
            p.save()

    def add_arguments(self, parser):
        parser.add_argument('args', nargs="*", default="")
