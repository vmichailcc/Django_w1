from django.db import models

books = [
    {'id': 1,
     'title': 'Fluent Python',
     'released_year': 2015,
     'description': 'Python’s simplicity lets you become productive quickly, but this often means you aren’t '
                    'using everything it has to offer. With this hands-on guide, you’ll learn how to write '
                    'effective, idiomatic Python code by leveraging its best—and possibly most neglected—features.'
                    ' Author Luciano Ramalho takes you through Python’s core language features and libraries, '
                    'and shows you how to make your code shorter, faster, and more readable at the same time.',
     'author_id': 1
     },
    {'id': 2,
     'title': 'Python Pocket Reference',
     'released_year': 2014,
     'description': "Updated for both Python 3.4 and 2.7, this convenient pocket guide is the perfect on-the-job quick "
                    "reference. Youâ??ll find concise, need-to-know information on Python types and statements, special "
                    "method names, built-in functions and exceptions, commonly used standard library modules, and other "
                    "prominent Python tools. The handy index lets you pinpoint exactly what you need.",
     'author_id': 2
     },
    {'id': 3,
     'title': 'Learning Python',
     'released_year': 2013,
     'description': "Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. "
                    "Based on author Mark Lutz’s popular training course, this updated fifth edition will help you "
                    "quickly write efficient, high-quality code with Python. It’s an ideal way to begin, whether you’re "
                    "new to programming or a professional developer versed in other languages.",
     'author_id': 2
     },
    {'id': 4,
     'title': 'Designing Data-Intensive Applications',
     'released_year': 2017,
     'description': "Data is at the center of many challenges in system design today. Difficult issues need to be "
                    "figured out, such as scalability, consistency, reliability, efficiency, and maintainability. "
                    "In addition, we have an overwhelming variety of tools, including relational databases,"
                    "NoSQL datastores, stream or batch processors, and message brokers. What are the right choices for "
                    "your application? How do you make sense of all these buzzwords?",
     'author_id': 3
     },
    {'id': 5,
     'title': 'Making Sense of Stream Processing',
     'released_year': 2016,
     'description': "How can event streams help make your application more scalable, reliable, and maintainable? "
                    "In this report, O’Reilly author Martin Kleppmann shows you how stream processing can make your "
                    "data storage and processing systems more flexible and less complex. Structuring data as a stream "
                    "of events isn’t new, but with the advent of open source projects such as Apache Kafka and Apache "
                    "Samza, stream processing is finally coming of age.",
     'author_id': 3
     },
    {'id': 6,
     'title': 'Python Crash Course',
     'released_year': 2019,
     'description': "This is the second edition of the best selling Python book in the world. Python Crash Course, "
                    "2nd Edition is a straightforward introduction to the core of Python programming."
                    " Author Eric Matthes dispenses with the sort of tedious, unnecessary information that can "
                    "get in the way of learning how to program, choosing instead to provide a foundation in general"
                    " programming concepts, Python fundamentals, and problem solving. Three real-world projects in the "
                    "second part of the book allow readers to apply their knowledge in useful ways.",
     'author_id': 4
     },

]

authors = [
    {'id': 1,
     'first_name': 'Luciano',
     'last_name': 'Ramalho',
     'age': 51,
     },
    {'id': 2,
     'first_name': 'Mark',
     'last_name': 'Lutz',
     'age': 81,
     },
    {'id': 3,
     'first_name': 'Martin',
     'last_name': 'Kleppmann',
     'age': 42,
     },
    {'id': 4,
     'first_name': 'Eric',
     'last_name': 'Matthes',
     'age': 47,
     },
]


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name="Title")
    released_year = models.IntegerField(verbose_name="Released year")
    description = models.TextField(max_length=5000, verbose_name="Description")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE, verbose_name="Author")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
