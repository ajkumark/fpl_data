from django.db import models

from djangotoolbox.fields import DictField


class Data(models.Model):
    fpl_data = DictField()

    def __unicode__(self):
    	return u'%s' % (self.fpl_data)