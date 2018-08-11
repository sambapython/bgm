from bloodgroup.models import BloodGroup, BloodBank, Organization
import random
orgs = Organization.objects.all()
bloodgroups = BloodGroup.objects.all()

for i in xrange(5000):
	org = random.choice(orgs)
	bloodgroups = random.sample(bloodgroups,
		4)
	bank = BloodBank(name=org.name+" blood bank%s"%i, organization=org)
	bank.save()
	for group in bloodgroups:
		bank.bloodgroups.add(group)