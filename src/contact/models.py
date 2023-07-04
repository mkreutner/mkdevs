from django.db import models

class ContactMessage(models.Model):

    name = models.CharField(null=False, max_length=512)
    email = models.EmailField(null=False)
    message = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_created=True)
    is_read = models.BooleanField(default=False)
    is_treated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        db_table_comment = 'Contact messages'

    def delete(self):
        self.is_deleted = True
        self.save()
