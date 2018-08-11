from bloodgroup.models import BloodGroup, BloodBank, Organization
import random
orgs = Organization.objects.all()
bloodgroups = BloodGroup.objects.all()
bloodgroups_count = range(1, len(bloodgroups)+1)
for i in xrange(5):
	org = random.choice(orgs)
	bloodgroups = random.sample(bloodgroups,
		random.choice(bloodgroups_count))
	bank = BloodBank(name=org.name+" blood bank%s"%i, Organization=org)
	bank.save()
	for group in bloodgroups:
		bank.bloodgroups.add(group)