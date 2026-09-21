print("TECH PATH EXPLORER")
print("AI-powered technology career exploration")

print()
print("Let's explore which technology paths")
print("might be interesting for you!")


# ==========================================
# QUESTION 1
# ==========================================

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

interest = input("Choose an option: ").upper()


# ==========================================
# QUESTION 2
# ==========================================

print()
print("2. How do you feel about coding?")
print("A. I love coding")
print("B. I like coding when the problem is interesting")
print("C. I can code, but I don't particularly enjoy it")
print("D. I dislike coding")
print("E. I've barely tried coding")

coding = input("Choose an option: ").upper()


# ==========================================
# QUESTION 3
# ==========================================

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

work = input("Choose an option: ").upper()


# ==========================================
# QUESTION 4
# ==========================================

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

future_goal = input("Choose an option: ").upper()


# ==========================================
# QUESTION 5
# ==========================================

print()
print("5. Tell us a little about your background.")
print("You can mention your education, coding experience,")
print("projects, courses, hobbies, or anything else relevant.")

background = input("Tell us about yourself: ")


# ==========================================
# CONVERT ANSWERS INTO READABLE TEXT
# ==========================================

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


# ==========================================
# CREATE USER PROFILE
# ==========================================

print()
print("Analyzing your answers...")
print("Finding technology paths worth exploring...")
print()

print("Your answers:")
print()
print("Interest:", interest_names.get(interest, "Not specified"))
print("Coding:", coding_names.get(coding, "Not specified"))
print("Work:", work_names.get(work, "Not specified"))
print("Future goal:", future_goal_names.get(future_goal, "Not specified"))
print("Background:", background)

print()
print("User profile created successfully!")


# ==========================================
# PATH SCORES
# ==========================================

scores = {
    "Artificial Intelligence": 0,
    "Cybersecurity": 0,
    "Data Science": 0,
    "Software Engineering": 0,
    "Information Technology": 0,
    "Cloud / DevOps": 0,
    "Robotics": 0,
    "UI/UX & Product Design": 0
}


# ==========================================
# QUESTION 1 SCORING
# ==========================================

interest_paths = {
    "A": "Artificial Intelligence",
    "B": "Cybersecurity",
    "C": "Data Science",
    "D": "Software Engineering",
    "E": "Information Technology",
    "F": "Cloud / DevOps",
    "G": "Robotics",
    "H": "UI/UX & Product Design"
}

if interest in interest_paths:
    scores[interest_paths[interest]] += 3


# ==========================================
# QUESTION 2 SCORING
# ==========================================

if coding == "D":
    scores["Information Technology"] += 1

if coding == "E":
    scores["Information Technology"] += 1


# ==========================================
# QUESTION 3 SCORING
# ==========================================

work_paths = {
    "A": "Software Engineering",
    "B": "Artificial Intelligence",
    "C": "Cybersecurity",
    "D": "Data Science",
    "E": "Robotics",
    "F": "Cloud / DevOps",
    "G": "Artificial Intelligence",
    "H": "UI/UX & Product Design"
}

if work in work_paths:
    scores[work_paths[work]] += 2


# ==========================================
# QUESTION 4 SCORING
# ==========================================

if future_goal == "C":
    scores["UI/UX & Product Design"] += 2
    scores["Software Engineering"] += 1

if future_goal == "D":
    scores["Artificial Intelligence"] += 2
    scores["Robotics"] += 1

if future_goal == "E":
    scores["UI/UX & Product Design"] += 2

if future_goal == "F":
    scores["Artificial Intelligence"] += 1
    scores["Cybersecurity"] += 1

if future_goal == "G":
    scores["Software Engineering"] += 1
    scores["Cybersecurity"] += 1
    scores["Information Technology"] += 1

if future_goal == "H":
    scores["Data Science"] += 1
    scores["Artificial Intelligence"] += 1


# ==========================================
# QUESTION 5 SCORING
# ==========================================

background_lower = background.lower()

if "python" in background_lower:
    scores["Artificial Intelligence"] += 1
    scores["Data Science"] += 1

if "ai" in background_lower or "artificial intelligence" in background_lower:
    scores["Artificial Intelligence"] += 2

if "security" in background_lower or "cyber" in background_lower:
    scores["Cybersecurity"] += 2

if "robot" in background_lower or "arduino" in background_lower:
    scores["Robotics"] += 2

if "design" in background_lower or "ui" in background_lower:
    scores["UI/UX & Product Design"] += 2

if "c++" in background_lower:
    scores["Software Engineering"] += 1


# ==========================================
# RANK TECHNOLOGY PATHS
# ==========================================

ranked_paths = sorted(
    scores,
    key=scores.get,
    reverse=True
)


# ==========================================
# PATH DESCRIPTIONS
# ==========================================

path_descriptions = {

    "Artificial Intelligence":
        "Build systems that can learn, generate content, recognize patterns, or make predictions.",

    "Cybersecurity":
        "Protect computers, networks, applications, and data from security threats.",

    "Data Science":
        "Use data to discover patterns, answer questions, and support better decisions.",

    "Software Engineering":
        "Design and build software applications, websites, and other digital products.",

    "Information Technology":
        "Work with computer systems, networks, technical support, and technology infrastructure.",

    "Cloud / DevOps":
        "Work with cloud platforms, automation, deployment, and systems that keep applications running.",

    "Robotics":
        "Combine software, electronics, and hardware to build machines that can sense and act.",

    "UI/UX & Product Design":
        "Design useful, understandable, and enjoyable digital products and user experiences."
}


# ==========================================
# SHOW TOP 4 PATHS
# ==========================================

print()
print("Technology paths worth exploring:")

for path in ranked_paths[:4]:

    print()
    print(path)
    print(path_descriptions[path])


# ==========================================
# FINAL MESSAGE
# ==========================================

print()
print("These are areas worth investigating based on your answers.")
print("Try the suggested paths before deciding what you want to pursue.")
