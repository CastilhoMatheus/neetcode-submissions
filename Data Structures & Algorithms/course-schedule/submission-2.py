class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:    
        pr = defaultdict(list)
        completed = set()

        for courses in prerequisites:
            if courses[0] == courses[1]:
                return False

            pr[courses[0]].append(courses[1])

        def canCompleteCourse(course, visited):
            if course in completed:
                return True

            if course in visited:
                return False

            if len(pr[course]) == 0:
                completed.add(course)
                return True

            preReqs = pr[course]
            visited.add(course)
            for p in preReqs:
                if not canCompleteCourse(p, visited):
                    return False

            completed.add(course)
            return True

        for i in range(numCourses - 1):
            visited = set()
            if not canCompleteCourse(i, visited):
                return False
        
        return True
