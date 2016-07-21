name = 'Zed A. Shaw'
age = 35
height = 74 
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d." % (
        age, height, weight, age + height + weight )

height_metric = height * 2.54
weight_metric = weight * 0.453592

print "Metrically, he's %d centimeters tall and weighs %d kilos" % (height_metric, weight_metric)
print "Octally, that's %o centimenters tall, and %o kilos" % (height, weight)
print "What does %%r do?  %r %r %r" % (age, height, weight)
