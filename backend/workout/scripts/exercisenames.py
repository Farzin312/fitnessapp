from ..models import UserBodyPart, UserWorkout

def add_exercise(exercise_name, primary_target, secondary_targets):
    primary, _ = UserBodyPart.objects.get_or_create(name=primary_target)
    workout = UserWorkout.objects.create(exercise_name=exercise_name, primary_target=primary)

    for target in secondary_targets:
        secondary, _ = UserBodyPart.objects.get_or_create(name=target)
        workout.secondary_targets.add(secondary)

def populate_exercises():
    exercises = [
        ('Bench Press', 'Chest', ['Triceps', 'Shoulders']),
        ('Squat', 'Quads', ['Glutes', 'Hamstrings']),
        ('Deadlift', 'Hamstrings', ['Back', 'Glutes']),
        ('Overhead Press', 'Shoulders', ['Triceps']),
        ('Pull-Up', 'Back', ['Biceps']),
        ('Barbell Row', 'Back', ['Biceps']),
        ('Dips', 'Triceps', ['Chest', 'Shoulders']),
        ('Leg Press', 'Quads', ['Glutes', 'Hamstrings']),
        ('Lunges', 'Quads', ['Glutes', 'Hamstrings']),
        ('Push-Up', 'Chest', ['Triceps', 'Shoulders']),
        ('Lat Pulldown', 'Back', ['Biceps']),
        ('Barbell Curl', 'Biceps', []),
        ('Tricep Pushdown', 'Triceps', []),
        ('Face Pull', 'Shoulders', ['Upper Back']),
        ('Leg Curl', 'Hamstrings', []),
        ('Leg Extension', 'Quads', []),
        ('Calf Raise', 'Calves', []),
        ('Incline Bench Press', 'Upper Chest', ['Shoulders', 'Triceps']),
        ('Front Squat', 'Quads', ['Glutes', 'Hamstrings']),
        ('Pendlay Row', 'Back', ['Biceps']),
        ('Military Press', 'Shoulders', ['Triceps']),
        ('T-Bar Row', 'Back', ['Biceps']),
        ('Seated Row', 'Back', ['Biceps']),
        ('Romanian Deadlift', 'Hamstrings', ['Glutes', 'Lower Back']),
        ('Bulgarian Split Squat', 'Quads', ['Glutes', 'Hamstrings']),
        ('Close-Grip Bench Press', 'Triceps', ['Chest', 'Shoulders']),
        ('Preacher Curl', 'Biceps', []),
        ('Skull Crushers', 'Triceps', []),
        ('Hack Squat', 'Quads', ['Glutes', 'Hamstrings']),
        ('Good Morning', 'Hamstrings', ['Lower Back']),
        ('Upright Row', 'Shoulders', ['Upper Back']),
        ('Cable Crossover', 'Chest', []),
        ('Reverse Fly', 'Upper Back', ['Shoulders']),
        ('Decline Bench Press', 'Lower Chest', ['Triceps', 'Shoulders']),
        ('Chin-Up', 'Back', ['Biceps']),
        ('Hip Thrust', 'Glutes', ['Hamstrings']),
        ('Box Jump', 'Quads', ['Glutes', 'Calves']),
        ('Farmer\'s', 'Forearms', ['Shoulders', 'Traps']),
        ('Kettlebell Swing', 'Glutes', ['Hamstrings', 'Lower Back']),
        ('Clean and Press', 'Shoulders', ['Legs', 'Back']),
        ('Snatch', 'Shoulders', ['Legs', 'Back']),
        ('Turkish Get-Up', 'Full Body', []),
        ('Thruster', 'Shoulders', ['Quads', 'Glutes']),
        ('Wall Ball', 'Quads', ['Shoulders', 'Glutes']),
        ('Battle Ropes', 'Arms', ['Shoulders']),
        ('Sled Push', 'Legs', ['Glutes']),
        ('Sled Pull', 'Back', ['Hamstrings']),
        ('Goblet Squat', 'Quads', ['Glutes', 'Hamstrings']),
        ('Zercher Squat', 'Quads', ['Glutes', 'Back']),
        ('Sumo Deadlift', 'Glutes', ['Hamstrings', 'Back']),
        ('Rack Pull', 'Back', ['Hamstrings']),
        ('Reverse Lunge', 'Quads', ['Glutes', 'Hamstrings']),
        ('Split Squat', 'Quads', ['Glutes', 'Hamstrings']),
        ('Inverted Row', 'Back', ['Biceps']),
        ('Hammer Curl', 'Biceps', ['Forearms']),
        ('Concentration Curl', 'Biceps', []),
        ('Spider Curl', 'Biceps', []),
        ('Cable Curl', 'Biceps', []),
        ('Overhead Tricep Extension', 'Triceps', []),
        ('Tricep Kickback', 'Triceps', []),
        ('Standing Babrell Shoulder Press', 'Shoulders', ['Triceps', 'Chest', 'Abs']),
        ('Seated Barbell Shoulder Press', 'Shoulders', ['Triceps', 'Chest']),
    ]

    for exercise in exercises:
        add_exercise(*exercise)

if __name__ == '__main__':
    populate_exercises()
