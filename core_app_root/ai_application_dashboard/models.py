from django.db import models
from django.contrib import auth
from django.db import models
from core_app_root.security.models import User
# Create your models here.
class Books(models.Model):
    book_title=models.CharField(max_length=2000)

class Category(models.Model):
    """A contributor to a Book, e.g. author, editor, co-author."""
    book_category = models.CharField(max_length=1050,
                                   help_text="The contributor's first name or names.")
    book_distributors = models.CharField(max_length=1050,
                                  help_text="The contributor's last name or names.")    

    def __str__(self):
        return self.book_category

class Publisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(max_length=50,
                            help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __str__(self):
        return self.name


class Book(models.Model):
    """A published book."""
    book_category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=70,
                             help_text="The title of the book.")
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20,
                            verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE)
   
    cover = models.ImageField(null=True,
                              blank=True,
                              upload_to="media/book_covers/")
    sample = models.FileField(null=True,
                              blank=True,
                              upload_to="media/book_samples/")
    
    book_details=models.TextField(null=True,blank=True)
    
    number_of_times_read=models.IntegerField(null=True,blank=True)
    
    def get_first_30_words(self):
        words = self.book_details.split()[:30]
        return ' '.join(words) + ('...' if len(words) == 30 else '')

    def __str__(self):
        return "{} ({})".format(self.title, self.isbn)

    def isbn13(self):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(self.isbn[0:3], self.isbn[3:4],
                                       self.isbn[4:6], self.isbn[6:12],
                                       self.isbn[12:13])



class RecommendedBookCategory(models.Model):
    """A contributor to a Book, e.g. author, editor, co-author."""
    book_category = models.CharField(max_length=1050,
                                   help_text="The contributor's first name or names.")
    book_distributors = models.CharField(max_length=1050,
                                  help_text="The contributor's last name or names.")    

    def __str__(self):
        return self.book_category

class RecommendedBookPublisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(max_length=50,
                            help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __str__(self):
        return self.name


class RecommendedBook(models.Model):
    """A published book."""
    book_category=models.ForeignKey(RecommendedBookCategory,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=70,
                             help_text="The title of the book.")
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20,
                            verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(RecommendedBookPublisher,
                                  on_delete=models.CASCADE)
   
    cover = models.ImageField(null=True,
                              blank=True,
                              upload_to="media/book_covers/")
    sample = models.FileField(null=True,
                              blank=True,
                              upload_to="media/book_samples/")
    
    book_details=models.TextField(null=True,blank=True)
    
    number_of_times_read=models.IntegerField(null=True,blank=True)
    
    def get_first_30_words(self):
        words = self.book_details.split()[:30]
        return ' '.join(words) + ('...' if len(words) == 30 else '')

    def __str__(self):
        return "{} ({})".format(self.title, self.isbn)

    def isbn13(self):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(self.isbn[0:3], self.isbn[3:4],
                                       self.isbn[4:6], self.isbn[6:12],
                                       self.isbn[12:13])
