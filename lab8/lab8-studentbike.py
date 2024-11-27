def assign_bikes(students, bikes):
    assignments = [-1] * len(students)
    distances = []

    for i, student in enumerate(students):
        for j, bike in enumerate(bikes):
            dist = abs(student[0] - bike[0]) + abs(student[1] - bike[1])
            distances.append((dist, i, j))

    distances.sort()

    assigned_bikes = set()
    assigned_students = set()

    for dist, student_idx, bike_idx in distances:
        if student_idx not in assigned_students and bike_idx not in assigned_bikes:
            assignments[student_idx] = bike_idx
            assigned_students.add(student_idx)
            assigned_bikes.add(bike_idx)

    return assignments

students = [(0, 0), (1, 1)]
bikes = [(0, 1), (4, 3), (2, 1)]
print(assign_bikes(students, bikes))  # Output: [0, 2]
