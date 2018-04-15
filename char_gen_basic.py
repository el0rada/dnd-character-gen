#complete character
import random
import os

def clear():
	if(os.name=="nt"):
		os.system("cls")
	else:
		os.system("clear")

def stats():

	stat_list = []

	i=0
	y=0
	stat=0

	while(i<=5):

		roll_list = []
		stat=0

		while(y<=3):
			roll_list.append(random.randint(1,6))
			y+=1

		roll_list.sort()
		roll_list.pop(0)
		
		#print(roll_list)
		
		for x in roll_list:
			stat += x

		stat_list.append(stat)
		i+=1
		y=0

	stat_list.sort()
	return(stat_list)

def character_race():
	l = [
		"dwarf",
		"elf",
		"halfling",
		"human",
		"dragonborn",
		"gnome",
		"half-elf",
		"half-orc",
		"tiefling"

		]

	x = random.choice(l)

	if(x == "dwarf"):
		y = ["hill dwarf", "mountain dwarf"]
		x = random.choice(y)
	if(x == "elf"):
		y = ["high elf", "wood elf", "dark elf"]
		x = random.choice(y)
	if(x == "halfling"):
		y = ["lightfoot halfling", "stout halfling"]
		x = random.choice(y)
	if(x == "dragonborn"):
		y = ["black dragonborn", "blue dragonborn", "brass dragonborn", "bronze dragonborn", "copper dragonborn", "gold dragonborn", "green dragonborn", "red dragonborn", "silver dragonborn", "white dragonborn"]
		x = random.choice(y)
	if(x == "gnome"):
		y = ["forest gnome", "rock gnome"]
		x = random.choice(y)

	return(x.title())

def character_class():
	l = [
		"barbarian",
		"bard",
		"cleric",
		"druid",
		"fighter",
		"monk",
		"paladin",
		"ranger",
		"rogue",
		"sorcerer",
		"warlock",
		"wizard"
		]

	x = random.choice(l)

	if(x=="barbarian"):
		h = 12
	if(x in ("fighter","paladin","ranger")):
		h = 10
	if(x in ("bard","cleric","druid","monk","rogue","warlock")):
		h = 8
	if(x in ("sorcerer","wizard")):
		h = 6

	return(x.title(),h)

def background():
	background_list = ["acolyte","charlatan","criminal","entertainer","folk hero","guild artisan","hermit","noble","outlander","sage","sailor","soldier","urchin"]
	b = ""
	bi = ""

	z = random.choice(background_list)

	if(z=="acolyte"):
		l = [
				"I ran away from home at an early age and found refuge in a temple.", 
				"my family gave me to a temple, since they were unable or unwilling to care for me.", 
				"I grew up in a household with strong religious convictions. Entering the service of one or more gods seemed natural.", 
				"an impassioned sermon struck a chord deep in my soul and moved me to serve the faith.", 
				"I followed a childhood friend, a respected acquaintance, or someone I loved into religious service.",
				"after encountering a true servant of the gods, I was so inspired that I immediately entered the service of a religious group."
			]
		b = z
		bi = random.choice(l)
		a = "an"

	if(z=="charlatan"):
		l = [
				"I was left to my own devices, and my knack for manipulating others helped me survive.",
				"I learned early on that people are gullible and easy to exploit.",
				"I often got in trouble, but I managed to talk my way out of it every time.",
				"I took up with a confidence artist, from whom I learned my craft.",
				"after a charlatan fleeced my family, I decided to learn the trade so I would never be fooled by such deception again.",
				"I was poor or I feared becoming poor, so I learned the tricks I needed to keep myself out of poverty."
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="criminal"):
		l = [
			"I resented authority in my younger days and saw a life of crime as the best way to fight against tyranny and oppression.",
			"necessity forced me to take up the life, since it was the only way I could survive.",
			"I fell in with a gang of reprobates and ne'er-dowells, and I learned my specialty from them.",
			"a parent or relative taught me my criminal specialty to prepare me for the family business.",
			"I left home and found a place in a thieves' guild or some other criminal organization. ",
			"I was always bored, so I turned to crime to pass the time and discovered I was quite good at it. "
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="entertainer"):
		l = [
			"members of my family made ends meet by performing, so it was fitting for me to follow their example.",
			"I always had a keen insight into other people, enough so that I could make them laugh or cry with my stories or songs.",
			"I ran away from home to follow a minstrel troupe.",
			"I saw a bard perform once, and I knew from that moment on what I was born to do.",
			"I earned coin by performing on street corners and eventually made a name for myself.",
			"A traveling entertainer took me in and taught me the trade."
			]
		b = z
		bi = random.choice(l)
		a = "an"

	if(z=="folk hero"):
		l = [
			"I learned what was right and wrong from my family.",
			"I was always enamored by tales of heroes and wished I could be something more than ordinary.",
			"I hated my mundane life, so when it was time for someone to step up and do the right thing, I took my chance.",
			"a parent or one of my relatives was an adventurer, and I was inspired by that person's courage.",
			"a mad old hermit spoke a prophecy when I was born, saying that I would accomplish great things.",
			"I have always stood up for those who are weaker than I am."
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="guild artisan"):
		l = [
			"I was apprenticed to a master who taught me the guild's business.",
			"I helped a guild artisan keep a secret or complete a task, and in return I was taken on as an apprentice.",
			"one of my family members who belonged to the guild made a place for me.",
			"I was always good with my hands, so I took the opportunity to learn a trade.",
			"I wanted to get away from my home situation and start a new life.",
			"I learned the essentials of my craft from a mentor but had to join the guild to finish my training."
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="hermit"):
		l = [
			"my enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.",
			"I am comfortable with being isolated, as I seek inner peace.",
			"I never liked the people I called my friends, so it was easy for me to strike out on my own.",
			"I felt compelled to forsake my past, but did so with great reluctance, and sometimes I regret making that decision.",
			"I lost everything-my home, my family, my friends. Going it alone was all I could do.",
			"Society's decadence disgusted me, so I decided to leave it behind"
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="noble"):
		l = [
			"I come from an old and storied family, and it fell to me to preserve the family name.",
			"my family has been disgraced, and I intend to clear our name",
			"my family recently came by its title, and that elevation thrust us into a new and strange world.",
			"my family has a title, but none of my ancestors have distinguished themselves since we gained it.",
			"my family is filled with remarkable people. I hope to live up to their example.",
			"I hope to increase my family's power and influence."
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="outlander"):
		l = [
			"I spent a lot of time in the wilderness as a youngster, and I came to love that way of life.",
			"from a young age, I couldn't abide the stink of the cities and preferred to spend my time in nature.",
			"I came to understand the darkness that lurks in the wilds, and I vowed to combat it.",
			"my people lived on the edges of civilization, and I learned the methods of survival from my family",
			"after a tragedy I retreated to the wilderness, leaving my old life behind.",
			"my family moved away from civilization, and I learned to adapt to my new environment."
			]
		b = z
		bi = random.choice(l)
		a = "an"

	if(z=="sage"):
		l = [
			"I was naturally curious, so I packed up and went to a university to learn more about the world.",
			"my mentor's teachings opened my mind to new possibilities in that field of study.",
			"I was always an avid reader, and I learned much about my favorite topic on my own.",
			"I discovered an old library and pored over the texts I found there. That experience awakened a hunger for more knowledge.",
			"I impressed a wizard who told me I was squandering my talents and should seek out an education to take advantage of my gifts.",
			"one of my parents or a relative gave me a basic education that whetted my appetite, and I left home to build on what I had learned." 
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="sailor"):
		l = [
			"I was press-ganged by pirates and forced to serve on their ship until I finally escaped.",
			"I wanted to see the world, so I signed on as a deckhand for a merchant ship.",
			"one of my relatives was a sailor who took me to sea.",
			"I needed to escape my community quickly, so I stowed away on a ship. When the crew found me, I was forced to work for my passage.",
			"reavers attacked my community, so I found refuge on a ship until I could seek vengeance.",
			"I had few prospects where I was living, so I left to find my fortune elsewhere."
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="soldier"):
		l = [
			"I joined the militia to help protect my community from monsters.",
			"a relative of mine was a soldier, and I wanted to carry on the family tradition.",
			"the local lord forced me to enlist in the army.",
			"war ravaged my homeland while I was growing up. Fighting was the only life I ever knew.",
			"I wanted fame and fortune, so I joined a mercenary company, selling my sword to the highest bidder",
			"invaders attacked my homeland. It was my duty to take up arms in defense of my people."
			]
		b = z
		bi = random.choice(l)
		a = "a"

	if(z=="urchin"):
		l = [
			"wanderlust caused me to leave my family to see the world. I look after myself.",
			"I ran away from a bad situation at home and made my own way in the world.",
			"monsters wiped out my village, and I was the sole survivor. I had to find a way to survive.",
			"a notorious thief looked after me and other orphans, and we spied and stole to earn our keep.",
			"one day I woke up on the streets, alone and hungry, with no memory of my early childhood.",
			"my parents died, leaving no one to look after me. I raised myself."
			]
		b = z
		bi = random.choice(l)
		a = "an"

	return(b,bi,a)

def stat_assign(ch_class, ch_stats, ch_race):
	strength,dexterity,constitution,intelligence,wisdom,charisma = 0,0,0,0,0,0
	l = ch_stats
	i = 0
	r = ch_race.lower()
	c = ch_class.lower()
	removed = 0
	
	#Class Specific Stats, taking the stats and assigning them
	#highest stat is assigned to primary stat

	if(c == "barbarian"):
		strength = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "bard"):
		charisma = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)


			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "cleric"):
		wisdom = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)


			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			i+=1

	if(c == "druid"):
		wisdom = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)


			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "fighter"):

		if(random.choice(["strength", "dexterity"]) == "strength"):
			strength = l[5]
			dexterity = l[4]
		else:
			dexterity = l[5]
			strength = l[4]

		l.pop(5)
		l.pop(4)

		while(i<=3):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "monk"):

		if(random.choice(["strength", "wisdom"]) == "strength"):
			strength = l[5]
			wisdom = l[4]
		else:
			wisdom = l[5]
			strength = l[4]
		
		l.pop(5)
		l.pop(4)

		while(i<=3):
			x = random.choice(l)

			if(strength == 0):
				strength = x

				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
				removed = 0

			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "paladin"):

		if(random.choice(["strength", "charisma"]) == "strength"):
			strength = l[5]
			charisma = l[4]
		else:
			charisma = l[5]
			strength = l[4]
		
		l.pop(5)
		l.pop(4)

		while(i<=3):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "ranger"):

		if(random.choice(["dexterity", "wisdom"]) == "dexterity"):
			dexterity = l[5]
			wisdom = l[4]
		else:
			wisdom = l[5]
			dexterity = l[4]
		
		l.pop(5)
		l.pop(4)

		while(i<=3):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "rogue"):
		dexterity = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "sorcerer"):
		charisma = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "warlock"):
		charisma = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1

	if(c == "wizard"):
		intelligence = l[5]
		l.pop(5)

		while(i<=4):
			x = random.choice(l)

			if(strength == 0):
				strength = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(dexterity == 0):
				dexterity = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(constitution == 0):
				constitution = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(intelligence == 0):
				intelligence = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(wisdom == 0):
				wisdom = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0
			elif(charisma == 0):
				charisma = x
				for val in l:
					if(val == x):
						if(removed == 0):
							l.remove(val)
							removed = 1
				removed = 0

			i+=1


	#Race specific stats

	if("dwarf" in r):
		constitution += 2

		if(r == "hill dwarf"):
			wisdom += 1
		elif(r == "mountain dwarf"):
			strength += 2

	elif("elf" in r):
		dexterity += 2

		if(r == "high elf"):
			intelligence += 2
		elif(r == "wood elf"):
			wisdom += 1
		elif(r == "dark elf"):
			charisma += 1
	elif("halfing" in r):
		dexterity += 2

		if(r == "lightfoot halfling"):
			charisma += 1
		elif(r == "stout halfing"):
			constitution += 1
	elif(r == "human"):
		strength += 1
		dexterity += 1
		constitution += 1
		intelligence += 1
		wisdom += 1
		charisma += 1

	elif("dragonborn" in r):
		strength += 2
		charisma += 1

	elif("gnome" in r):
		intelligence += 2

		if(r == "forest gnome"):
			dexterity += 1
		elif(r == "rock gnome"):
			constitution += 1

	elif(r == "half-elf"):
		charisma += 2
		i = 0
		while i <= 1:

			x = random.choice("strength","dexterity","constitution","intelligence","wisdom")
			used = []

			if(x == "strength" and x not in used):
				strength += 1
				used.append(x)
				i+=1
			elif(x == "dexterity" and x not in used):
				dexterity += 1
				used.append(x)
				i+=1
			elif(x == "constitution" and x not in used):
				constitution += 1
				used.append(x)
				i+=1
			elif(x == "intelligence" and x not in used):
				intelligence += 1
				used.append(x)
				i+=1
			elif(x == "wisdom" and x not in used):
				wisdom += 1
				used.append(x)
				i+=1


	elif(r == "half-orc"):
		strength += 2
		constitution += 1

	elif(r == "tiefling"):
		intelligence += 1
		charisma += 2

	return(strength,dexterity,constitution,intelligence,wisdom,charisma)

def calc_modifiers(stat):
	mod_dict = {1:"-5",2:"-4",3:"-4",4:"-3",5:"-3",6:"-2", 7:"-2", 8:"-1", 9:"-1", 10:"0", 11:"0", 12:"+1", 13:"+1", 14:"+2", 15:"+2", 16:"+3", 17:"+3", 18:"+4", 19:"+4", 20:"+5"}

	return(mod_dict[stat])

linebreak = "\n\n" + "="*20 + "\n" + "#~#~"*5 + "\n" + "="*20
while True:
	clear()

	statslist = stats()
	char_race = character_race()
	char_class, hit_die = character_class()
	char_str, char_dex, char_con, char_int, char_wis, char_cha = stat_assign(char_class, statslist, char_race)
	back, back_info, a_or_an = background()

	output = ("Race: " + char_race + 
		  "\nClass: " + char_class + 
		  "\nHit Dice: d" + str(hit_die) +
		  "\n\nStr: " + str(char_str) + " (" + calc_modifiers(char_str) + ")" +
		  "\nDex: " + str(char_dex) + " (" + calc_modifiers(char_dex) + ")" +
		  "\nCon: " + str(char_con) + " (" + calc_modifiers(char_con) + ")" +
		  "\nInt: " + str(char_int) + " (" + calc_modifiers(char_int) + ")" +
		  "\nWis: " + str(char_wis) + " (" + calc_modifiers(char_wis) + ")" +
		  "\nCha: " + str(char_cha) + " (" + calc_modifiers(char_cha) + ")" +
		  linebreak +
		  "\nBackground: " + back.title() +
		  "\n\nI became " + a_or_an + " " + back + " becuase " + back_info
		 )

	print(output)
	
	
	x = input("\n\nRoll Again (y/N): ")

	if(x=="y"):
		pass
	else:
		clear()
		break