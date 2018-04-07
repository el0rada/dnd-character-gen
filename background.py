#random background picker
import random

def background():
	background_list = ["acolyte","charlatan","criminal","entertainer","folk hero","guild artisan","hermit","noble","outlander","sage","sailor","soldier","urchin"]
	output = ""

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
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became an acolyte because " + random.choice(l)

	if(z=="charlatan"):
		l = [
				"I was left to my own devices, and my knack for manipulating others helped me survive.",
				"I learned early on that people are gullible and easy to exploit.",
				"I often got in trouble, but I managed to talk my way out of it every time.",
				"I took up with a confidence artist, from whom I learned my craft.",
				"after a charlatan fleeced my family, I decided to learn the trade so I would never be fooled by such deception again.",
				"I was poor or I feared becoming poor, so I learned the tricks I needed to keep myself out of poverty."
			]
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a charlatan because " + random.choice(l)

	if(z=="criminal"):
		l = [
			"I resented authority in my younger days and saw a life of crime as the best way to fight against tyranny and oppression.",
			"necessity forced me to take up the life, since it was the only way I could survive.",
			"I fell in with a gang of reprobates and ne'er-dowells, and I learned my specialty from them.",
			"a parent or relative taught me my criminal specialty to prepare me for the family business.",
			"I left home and found a place in a thieves' guild or some other criminal organization. ",
			"I was always bored, so I turned to crime to pass the time and discovered I was quite good at it. "
			]
		
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a criminal because " + random.choice(l)

	if(z=="entertainer"):
		l = [
			"members of my family made ends meet by performing, so it was fitting for me to follow their example.",
			"I always had a keen insight into other people, enough so that I could make them laugh or cry with my stories or songs.",
			"I ran away from home to follow a minstrel troupe.",
			"I saw a bard perform once, and I knew from that moment on what I was born to do.",
			"I earned coin by performing on street corners and eventually made a name for myself.",
			"A traveling entertainer took me in and taught me the trade."
			]
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became an entertainer because " + random.choice(l)

	if(z=="folk hero"):
		l = [
			"I learned what was right and wrong from my family.",
			"I was always enamored by tales of heroes and wished I could be something more than ordinary.",
			"I hated my mundane life, so when it was time for someone to step up and do the right thing, I took my chance.",
			"a parent or one of my relatives was an adventurer, and I was inspired by that person's courage.",
			"a mad old hermit spoke a prophecy when I was born, saying that I would accomplish great things.",
			"I have always stood up for those who are weaker than I am."
			]
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a folk hero because " + random.choice(l)

	if(z=="guild artisan"):
		l = [
			"I was apprenticed to a master who taught me the guild's business.",
			"I helped a guild artisan keep a secret or complete a task, and in return I was taken on as an apprentice.",
			"one of my family members who belonged to the guild made a place for me.",
			"I was always good with my hands, so I took the opportunity to learn a trade.",
			"I wanted to get away from my home situation and start a new life.",
			"I learned the essentials of my craft from a mentor but had to join the guild to finish my training."
			]
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a guild artisan because " + random.choice(l)

	if(z=="hermit"):
		l = [
			"my enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.",
			"I am comfortable with being isolated, as I seek inner peace.",
			"I never liked the people I called my friends, so it was easy for me to strike out on my own.",
			"I felt compelled to forsake my past, but did so with great reluctance, and sometimes I regret making that decision.",
			"I lost everything-my home, my family, my friends. Going it alone was all I could do.",
			"Society's decadence disgusted me, so I decided to leave it behind"
			]
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a hermit because " + random.choice(l)

	if(z=="noble"):
		l = [
			"I come from an old and storied family, and it fell to me to preserve the family name.",
			"my family has been disgraced, and I intend to clear our name",
			"my family recently came by its title, and that elevation thrust us into a new and strange world.",
			"my family has a title, but none of my ancestors have distinguished themselves since we gained it.",
			"my family is filled with remarkable people. I hope to live up to their example.",
			"I hope to increase my family's power and influence."
			]
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a noble because " + random.choice(l)

	if(z=="outlander"):
		l = [
			"I spent a lot of time in the wilderness as a youngster, and I came to love that way of life.",
			"From a young age, I couldn't abide the stink of the cities and preferred to spend my time in nature.",
			"I came to understand the darkness that lurks in the wilds, and I vowed to combat it.",
			"My people lived on the edges of civilization, and I learned the methods of survival from my family",
			"After a tragedy I retreated to the wilderness, leaving my old life behind.",
			"My family moved away from civilization, and I learned to adapt to my new environment."
			]
		
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became an outlander because " + random.choice(l)

	if(z=="sage"):
		l = [
			"I was naturally curious, so I packed up and went to a university to learn more about the world.",
			"My mentor's teachings opened my mind to new possibilities in that field of study.",
			"I was always an avid reader, and I learned much about my favorite topic on my own.",
			"I discovered an old library and pored over the texts I found there. That experience awakened a hunger for more knowledge.",
			"I impressed a wizard who told me I was squandering my talents and should seek out an education to take advantage of my gifts.",
			"One of my parents or a relative gave me a basic education that whetted my appetite, and I left home to build on what I had learned." 
			]
		
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a sage because " + random.choice(l)

	if(z=="sailor"):
		l = [
			"I was press-ganged by pirates and forced to serve on their ship until I finally escaped.",
			"I wanted to see the world, so I signed on as a deckhand for a merchant ship.",
			"One of my relatives was a sailor who took me to sea.",
			"I needed to escape my community quickly, so I stowed away on a ship. When the crew found me, I was forced to work for my passage.",
			"Reavers attacked my community, so I found refuge on a ship until I could seek vengeance.",
			"I had few prospects where I was living, so I left to find my fortune elsewhere."
			]
		
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a sailor because " + random.choice(l)

	if(z=="soldier"):
		l = [
			"I joined the militia to help protect my community from monsters.",
			"A relative of mine was a soldier, and I wanted to carry on the family tradition.",
			"The local lord forced me to enlist in the army.",
			"War ravaged my homeland while I was growing up. Fighting was the only life I ever knew.",
			"I wanted fame and fortune, so I joined a mercenary company, selling my sword to the highest bidder",
			"Invaders attacked my homeland. It was my duty to take up arms in defense of my people."
			]
		
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became a soldier because " + random.choice(l)

	if(z=="urchin"):
		l = [
			"Wanderlust caused me to leave my family to seethe world. I look after myself.",
			"I ran away from a bad situation at home and made my own way in the world.",
			"Monsters wiped out my village, and I was the sole survivor. I had to fi nd a way to survive.",
			"A notorious thief looked after me and other orphans, and we spied and stole to earn our keep.",
			"One day I woke up on the streets, alone and hungry, with no memory of my early childhood.",
			"My parents died, leaving no one to look after me. I raised myself."
			]
		
		output += "="*len(z)+ "\n" + z.upper() + "\n" + "="*len(z) + "\n\nI became an urchin because " + random.choice(l)

	print(output)

while True:
	background()
	x = input("Roll Again (y/N): ")
	if(x==""):
		break
	elif(x=="y"):
		pass
	else:
		break