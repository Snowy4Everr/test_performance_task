options = {
    "go outside": [
        "You leave the house and go outside.",
        "You look at the suburban life around you.",
        "You feel happier."
    ],
    "stay in bed": [
        "You decide to enjoy your day by taking it easy.",
        "You catch up on your life, take time to relax, and you smile.",
        "Within the confines of your bed, you feel warmer.",
        "You feel happier."
    ],
    "sleep": [
        "You decide that today isn't for you.",
        "Adding more hours could serve its own benefits, you think.",
        "You dream...",
        "You feel happier."
    ],
    "eat breakfast": [
        "You woke up feeling hungry.",
        "You walk into the kitchen and think about your options.",
        "You end up making cereal, sausage, and a small bowl of mixed berries.",
        "You are full, and happier."
    ],
    "go to your job": [
        "You start to worry.",
        "Then you remember you don't have a job.",
        "You feel happier."
    ]
}

def saturday_morning(category):
    if category in options and len(options[category]) > 0:
        for step in options[category]:
            input(step + " ")
        options.pop(category)
    else:
        print("Invalid choice or no more options available for this category.")

def ask_continue():
    return input("Do you want to continue? (yes/no): ").lower() 

def rating():
    recommend = input("Would you recommend this experience to a friend? (yes/no): ").lower()
    if recommend == "yes":
        print("Thank you for your recommendation!")
    else:
        print("Thank you for your feedback!")

def main():
        start_experience = input("Do you want to go through the Saturday morning experience? (yes/no): ").lower()

        if start_experience == "no":
            print("Thank you for being honest.")
            return
        
        completed_all = True

        while start_experience == "yes" and len(options) > 0:
            print("Available options:", ", ".join(options.keys()))
            choice = input("Choose an option: ").lower()

            saturday_morning(choice)
            
            if ask_continue() != "yes":
                completed_all = False
                break
        if completed_all:
            print("You chose every option!")

        rating()

main()