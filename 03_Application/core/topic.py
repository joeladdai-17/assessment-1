# Creating a topic class
class Topic():
# Constructor method
    def __init__(self, name, difficulty, confidence):
        self.name = name
        self.difficulty = difficulty
        self.confidence = confidence

# Updating the users confidence on a certain topic
    def update_confidence(self, new_confidence):
        self.confidence = new_confidence

# Updating the users difficulty rating
    def update_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty


    
        

    