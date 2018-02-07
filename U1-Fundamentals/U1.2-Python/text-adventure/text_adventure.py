start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in
your room. You’re in the middle of a giant maze. A sign is hanging from the ivy:
“You have one hour. Don’t touch the walls.” There is a hallway to your right and
to your left.
'''

left_hallway = '''
You go left and as you go farther down the path the ivy starts to change color
going from green to white. You are drenched in sweat by the time you reach the
next room where you find a glass of water on the stump of a tree. There is a
passageway to your right. The glass has condensation on the outside like it is
cold. You are so thirsty that you reach for it. As soon as the glass is off the
stump the room goes up in flames. Even the stump is on fire. You drink the
water. It is cold. You run as fast you can to the passageway to your right
catching a few minor burns along the way.
'''
right_hallway = '''
You go right and as you go the ground feels softer. It's like walking on a balloon.
It's so hard to keep your balance that you're on your hands and knees as you reach
a room with nothing but swords sticking out of the wall and a passageway to your left.
In the center of the room is a big fluffy red bathrobe laying on top of a table.
You go to examine the bathrobe but as you pick it up the swords on the wall
start hitting each other. It's as if there are people on the other side holding
on to the swords and dueling. Then the walls start closing in, you put the robe
on to protect yourself as you run for the passageway to your left. By the time
you make it to the passageway the robe has been cut to shreds, catching a few
cuts on your skin along the way.
'''

right_corridor = '''
You go along the passageway trying to assess the damage to yourself when you
come upon a third room. This room has an office desk in the middle with a big
rotary telephone. The phone is ringing. You pick it up and notice that it smells
like fresh squeezed orange juice and the receiver has the texture of hair. On it
you hear your mothers voice repeating, "Why?" over and over. You try to talk to it but
there is no response, just "Why?". The voice suddenly stops and you hear the slow
creaking of two doors opening. You turn around and see two doorways into complete
darkness. One is framed in red and one is framed in white.
'''

left_corridor = '''
You go along the passageway trying to assess the damage to yourself when you
come upon a third room. This room has an office desk in the middle with a big
rotary telephone. The phone is ringing. You pick it up and notice that it smells
like fresh squeezed orange juice and the receiver has the texture of hair. On it
you hear your mothers voice repeating, "Why?" over and over. You try to talk to it but
there is no response, just "Why?". The voice suddenly stops and you hear the slow
creaking of two doors opening. You turn around and see two doorways into complete
darkness. One is framed in yellow and one is framed in blue.
'''
print(start)
done = False
color = ""

while not done:
		user_input = input("Type 'left' to go left or 'right' to go right: ")
		if user_input == "left":
			print(left_hallway)
			print(left_corridor)
			color = "blue_yellow"
			done = True
		elif user_input == "right":
			print(right_hallway)
			print(right_corridor)
			color = "red_white"
			done = True
		else:
			print("Please type 'left' or 'right'");


blue_doorway = '''
You walk into the darkness through the blue doorway and immediately get the sensation
that you are falling. You try to scream but can't even hear your own voice. Then
you start to see your things fly past you. Your phone, you favorite pair of shoes,
your favorite toy, pictures from your childhood. You see memories, but you can't
feel them. They are all happening to this other person that looks like you but is
a stranger. You hear your mother's voice, "Why?". Then you hit something.
'''

yellow_doorway = '''
You walk into the darkness through the yellow doorway and feel yourself pulled up
like you're in a vacuum, but gently. A soft breeze that smells of vanilla seems
to envelope you and you sense two large hands underneath pushing you up. You weren't
being sucked up but carried up. You hear your mothers voice again, "Why?". Then
you stop.
'''

red_doorway = '''
You walk into the darkness through the red doorway and immediately get the sensation
that you are falling. You try to scream but can't even hear your own voice. Then
you start to see your things fly past you. Your phone, you favorite pair of shoes,
your favorite toy, pictures from your childhood. You see memories, but you can't
feel them. They are all happening to this other person that looks like you but is
a stranger. You hear your mother's voice, "Why?". Then you hit something.
'''

white_doorway = '''
You walk into the darkness through the white doorway and feel yourself pulled up
like you're in a vacuum, but gently. A soft breeze that smells of vanilla seems
to envelope you and you sense two large hands underneath pushing you up. You weren't
being sucked up but carried up. You hear your mothers voice again, "Why?". Then
you stop.
'''

end_of_story_red_white = '''
You're in bed. You stand up in bed and turn off your alarm. It's time to
to start your day. You put on your pair of mismatched slippers, red and white, and
go to the bathroom.
'''

end_of_story_blue_yellow = '''
You're in bed. You stand up in bed and turn off your alarm. It's time to
to start your day. You put on your pair of mismatched slippers, blue and yellow, and
go to the bathroom.
'''

done = False
while not done:
	if(color == "red_white"):
		user_input = input("Type 'red' to go into the red doorway or 'white' to into the white doorway: ")
		if user_input == "red":
			print(red_doorway)
			print(end_of_story_red_white)
			done = True
		elif user_input == "white":
			print(white_doorway)
			print(end_of_story_red_white)
			done = True
		else:
			print("Please type 'red' or 'white'");
	elif(color == "blue_yellow"):
		user_input = input("Type 'blue' to go into the blue doorway or 'yellow' to into the yellow doorway: ")
		if user_input == "blue":
			print(blue_doorway)
			print(end_of_story_blue_yellow)
			done = True
		elif user_input == "yellow":
			print(yellow_doorway)
			print(end_of_story_blue_yellow)
			done = True
		else:
			print("Please type 'blue' or 'yellow'");
	else:
		print("You wake up suddenly and confused. How did you end up here?")
		done = True

		