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
print()
print("Analyzing your answers...")
print("Finding technology paths worth exploring...")
print()

interest_names = {
    "A": "Artificial Intelligence",
    "B": "Cybersecurity",
    "C": "Data Science",
    "D": "Software Engineering",
    "E": "Information Technology",
    "F": "Cloud / DevOps",
    "G": "Robotics",
    "H": "UI/UX & Product Design"
}

coding_names = {
    "A": "I love coding",
    "B": "I like coding when the problem is interesting",
    "C": "I can code, but I don't particularly enjoy it",
    "D": "I dislike coding",
    "E": "I've barely tried coding"
}

work_names = {
    "A": "Building apps or products",
    "B": "Creating AI systems",
    "C": "Finding security problems",
    "D": "Working with data and finding patterns",
    "E": "Building robots or smart devices",
    "F": "Automating repetitive tasks",
    "G": "Researching and experimenting",
    "H": "Managing ideas, products, or teams",
    "I": "I'm not sure yet"
}

future_goal_names = {
    "A": "Get a good-paying job",
    "B": "Have remote or flexible work",
    "C": "Build my own products or business",
    "D": "Work with cutting-edge technology",
    "E": "Have creative freedom",
    "F": "Make an impact",
    "G": "Have strong job opportunities",
    "H": "Become highly skilled in a specific field",
    "I": "I'm still figuring it out"
}

print("Your answers:")
print()
print("Interest:", interest_names.get(interest, "Not specified"))
print("Coding:", coding_names.get(coding, "Not specified"))
print("Work:", work_names.get(work, "Not specified"))
print("Future goal:", future_goal_names.get(future_goal, "Not specified"))
print("Background:", background)

print()
print("User profile created successfully!")

