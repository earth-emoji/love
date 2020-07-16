from django.db import models

from accounts.models import Member
from campaigns.models import Campaign

class Donation(models.Model):
    # amount
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    # donor
    donor = models.ForeignKey(Member, related_name='donations', on_delete=models.CASCADE)
    # campaign
    campaign = models.ForeignKey(Campaign, related_name='donations', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'donation'
        verbose_name_plural = 'donations'

    def __str__(self):
        return f"{self.donor.get_name} for {self.campaign.title}"
