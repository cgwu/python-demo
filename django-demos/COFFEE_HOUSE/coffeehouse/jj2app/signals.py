# Listen for Django pre_save signal on model.
from django.dispatch import receiver

from django.db.models.signals import pre_save
from django.dispatch import receiver
#from .model import Store

import logging
LOG = logging.getLogger(__name__)

@receiver(pre_save, sender='jj2app.Store')
def run_before_save(sender, **kwargs):
    LOG.warning("消息监听开始Start pre_save Store in signals.py under jj2app")
    LOG.info("sender %s" % (sender))
    LOG.info("kwargs %s" % str(kwargs))

