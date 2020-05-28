from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId=models.AutoField(primary_key=True)
    MovieName=models.CharField(max_length=50)
    MovieType=models.CharField(max_length=50)
    MovieLanguage=models.CharField(max_length=50)
    MovieCast=models.CharField(max_length=50)
    MovieDirector=models.CharField(max_length=50)
    MovieDuration=models.CharField(max_length=50)
    MovieReleaseDate=models.CharField(max_length=50)
    MovieImg=models.ImageField(upload_to="movieImage/",default="No-img.jpg")
    class Meta:
        db_table="movie_408"
class Customer(models.Model):
    CustId=models.AutoField(primary_key=True)
    CustFName=models.CharField(max_length=50)
    CustLName=models.CharField(max_length=50)
    CustEmailId=models.CharField(max_length=50)
    CustPassword=models.CharField(max_length=50)
    CustContactNo=models.CharField(max_length=50)
    CustAddress=models.CharField(max_length=50)
    class Meta:
        db_table="customer_408"
class Admin(models.Model):
    adminEmailId=models.CharField(primary_key=True,max_length=50)
    adminPassword=models.CharField(max_length=50)
    class Meta:
        db_table="admin_408"
class Shows(models.Model):
    ShowId=models.AutoField(primary_key=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    #has-a relationship
    #when movie ger delete shows also deleted Automatically
    theatreNameLocation=models.CharField(max_length=100)
    screen=models.CharField(max_length=20)
    showDate=models.CharField(max_length=50)
    showTime=models.CharField(max_length=50)
    showPrice=models.FloatField(max_length=50)
    class Meta:
        db_table="shows_408"
