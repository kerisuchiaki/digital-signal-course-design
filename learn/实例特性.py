class Student(object):
    """represents a student"""
    count = 0  # 可以记数创建的对象的个数

    def __init__(self, name, number):
        """Constructor creates a Student
        with the given name and number of scores and sets all scores to 0."""
        Student.count += 1
        self.name = name
        self.scores = []
