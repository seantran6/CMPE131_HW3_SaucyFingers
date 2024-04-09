class User:
    def __init__(self, username, goals):
        self.username = username
        self.goals = goals

class RecommendationAlgorithm:
    def generate_recommendations(self, user_goals):
        # Sophisticated algorithm placeholder based on user goals
        base_supplements = ["Whey Protein", "BCAAs"]
        if 'weight loss' in user_goals:
            # Added weight loss specific supplements
            return base_supplements + ["Fat Burner", "L-Carnitine", "Green Tea Extract"]
        elif 'muscle gain' in user_goals:
            return base_supplements + ["Creatine", "Pre-Workout", "Mass Gainer"]
        else:
            return base_supplements

class SupplementRecommenderSystem:
    def __init__(self):
        self.users = {}  # Simulating a database with a dictionary
        self.recommendation_algorithm = RecommendationAlgorithm()

    def add_user(self, username, goals):
        if username not in self.users:
            self.users[username] = User(username, goals)
            print(f"User {username} added with goals: {', '.join(goals)}")
        else:
            print("User already exists.")

    def recommend_for(self, username):
        if username in self.users:
            user = self.users[username]
            recommendations = self.recommendation_algorithm.generate_recommendations(user.goals)
            print(f"Recommended supplements for {username}: {', '.join(recommendations)}")
        else:
            print("User not found.")

# Main program
if __name__ == "__main__":
    supplement_recommender_system = SupplementRecommenderSystem()
    
    # Adding users with different fitness goals
    supplement_recommender_system.add_user("JohnDoe", ["muscle gain"])
    supplement_recommender_system.add_user("JaneDoe", ["weight loss"])
    
    # Generating recommendations for both users
    supplement_recommender_system.recommend_for("JohnDoe")
    supplement_recommender_system.recommend_for("JaneDoe")