from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class Word(models.Model):
    member = models.TextField()
    content = models.TextField()
    create_date = models.DateTimeField()
    NNBC= models.TextField()
    NR= models.TextField()
    NP= models.TextField()
    VV= models.TextField()
    VA= models.TextField()
    VX= models.TextField()
    VCP= models.TextField()
    VCN= models.TextField()
    MM= models.TextField()
    MAG= models.TextField()
    MAJ= models.TextField()
    IC= models.TextField()
    JKS= models.TextField()
    JKC= models.TextField()
    JKG= models.TextField()
    JKO= models.TextField()
    JKB= models.TextField()
    JKV= models.TextField()
    JKQ= models.TextField()
    JC= models.TextField()
    JX= models.TextField()
    EP= models.TextField()
    EF= models.TextField()
    EC= models.TextField()
    ETN= models.TextField()
    ETM= models.TextField()
    XPN= models.TextField()
    XSN= models.TextField()
    XSV= models.TextField()
    XSA= models.TextField()
    XR= models.TextField()
    SF= models.TextField()
    SE= models.TextField()
    SSO= models.TextField()
    SSC= models.TextField()
    SC= models.TextField()
    SY= models.TextField()
    SH= models.TextField()
    SL= models.TextField()
    SN= models.TextField()
