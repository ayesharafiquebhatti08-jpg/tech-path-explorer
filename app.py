print("===================================")
print("       TECH PATH EXPLORER")
print("AI-powered technology career exploration")
print("===================================")

print()
print("Let's explore which technology paths")
print("might be interesting for you!")

print()
print("1. What interests you the most?")
print("A. Artificial Intelligence")
print("B. Cybersecurity")
print("C. Data Science")
print("D. Software Engineering")
print("E. Information Technology")
print("F. Cloud / DevOps")
print("G. Robotics")
print("H. UI/UX & Product Design")

interest = input("Choose an option: ")

print()
print("You selected:", interest)

print()
print("2. How do you feel about coding?")
print("A. I love coding")
print("B. I like coding when the problem is interesting")
print("C. I can code, but I don't particularly enjoy it")
print("D. I dislike coding")
print("E. I've barely tried coding")

coding = input("Choose an option: ")

print()
print("You selected:", coding)

print()
print("3. What kind of work sounds cool to you?")
print("A. Building apps or products")
print("B. Creating AI systems")
print("C. Finding security problems")
print("D. Working with data and finding patterns")
print("E. Building robots or smart devices")
print("F. Automating repetitive tasks")
print("G. Researching and experimenting")
print("H. Managing ideas, products, or teams")
print("I. I'm not sure yet")

work = input("Choose an option: ")

print()
print("You selected:", work)

print()
print("4. What are your future goals?")
print("A. Get a good-paying job")
print("B. Have remote or flexible work")
print("C. Build my own products or business")
print("D. Work with cutting-edge technology")
print("E. Have creative freedom")
print("F. Make an impact")
print("G. Have strong job opportunities")
print("H. Become highly skilled in a specific field")
print("I. I'm still figuring it out")

future_goal = input("Choose an option: ")

print()
print("You selected:", future_goal)

print()
print("5. Tell us a little about your background.")
print("You can mention your education, coding experience,")
print("projects, courses, hobbies, or anything else relevant.")

background = input("Tell us about yourself: ")

print()
print("Thanks! We have your background information.")

print()
print("===================================")
print("      ANALYZING YOUR ANSWERS...")
print("===================================")
print("Finding technology paths worth exploring...")

print()
print("Here is what you told us:")
print("Interest:", interest)
print("Coding:", coding)
print("Work:", work)
print("Future goals:", future_goal)
print("Background:", background)

user_profile = f"""
User's technology interests: {interest}

Coding preference: {coding}

Type of work they find interesting: {work}

Future goals: {future_goal}

Background:
{background}
"""

print()
print("User profile created successfully!")

