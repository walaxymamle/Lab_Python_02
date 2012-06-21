theInput = raw_input("Enter an integer: ")
print '---------------------------------------------------------------'
primarySchoolAge = 4
legalVotingAge = 18
print legalVotingAge,'years'
ageForPresident= 40
print ageForPresident,'years'
officialRetirementAge = 65
print officialRetirementAge,'years'
personAge = input("Enter an age: ")
print personAge
print '----------------------------------------------------------------'
if personAge<18:
   a="Too young."
elif personAge==18:
    a="Remember to vote"
elif personAge>40:
    a="Vote for me"
elif personAge<40:
    a="You can't be president"
elif personAge>65:
    a="Too old."
print a
print '-----------------------------------------------------------------'
for i in range(39,-1,-3):
   if i%3==0:
    print i
print '----------------------------------------------------------------'
i=7
while i<30:
    print i
    i=i*4
