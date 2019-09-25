from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    gdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname

    class Meta:
        db_table = 'grades'

class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(sdelete=False)
    def createStudent(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.createTime = createT
        return stu

class Students(models.Model):
    #自定义模型管理器
    stuObj = models.Manager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    sdelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)
    def __str__(self):
        return self.sname

    lastTime = models.DateField(auto_now=True)
    createTime = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'students'
        ordering = ['id']

    @classmethod
    def createStudents(cls, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = cls(sname=name,sage=age, sgender=gender, scontend=contend, sgrade=grade,lastTime=lastT, createTime=createT, sdelete=isD)
        return stu
