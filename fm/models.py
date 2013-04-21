from django.db import models
import datetime
from django.contrib.auth.models import User


class Document(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=2000)
    content_type = models.CharField(max_length=100)
    date_created = models.CharField(max_length=10)
    date_uploaded = models.DateTimeField(default=datetime.datetime.utcnow())
    document_file = models.FileField(upload_to='filetest/%Y/%m/%d')
    # uploaded_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_description = models.CharField(max_length=2000)
    event_participants = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.event_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=200, unique=True)
    tag_description = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.tag_name


class DocumentTag(models.Model):
    document_ref = models.ForeignKey(Document)
    tag_ref = models.ForeignKey(Tag)

    def __unicode__(self):
        return 'doc ref: %d tag ref: %d' % (self.document_ref, self.tag_ref)