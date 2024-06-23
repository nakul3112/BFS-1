# Time Complexity (DFS Approach) :
# O(V+E)

# Space Complexity (DFS Approach):  
# O(V+E) 


# Approach:
# ==> This is a Graph problem. Can also be considered as a Dependency Graph, which falls under "Topological Sort"


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses or not prerequisites:
            return True

        adjListMap = {}   # map of "the course"(key), and the "list of courses"(value) that can be completed after completing this course
        inCourses = []    # All courses and their dependencies count(no of subjects they depend on) at respective index
        queue = []     # to hold the courses that have been completed and navigate to the courses that depend on this course
        count = 0   # keeps track of courses that are completed

        # Build inCourses with all 0's
        inCourses = [0]*numCourses

        # build the adjListMap and update inCourses
        for prereq in prerequisites:
            fromSub = prereq[1]
            toSub = prereq[0]

            inCourses[toSub] += 1

            if fromSub not in adjListMap.keys():
                adjListMap[fromSub] = []
            adjListMap[fromSub].append(toSub)

        # Find the course with 0 depeendency to start with the exploration of dependency graph
        for i in range(0, len(inCourses)):
            if inCourses[i] == 0:
                queue.append(i)
                count += 1
        
        print("Queue: ", queue)

        while(queue):
            currSub = queue.pop(0)

            # Get the dep list from adjListMap for this currSub
            if currSub not in adjListMap.keys():
                continue

            depList = adjListMap[currSub]

            for depSub in depList:
                # decrement the count in inCourses array for current depSub
                inCourses[depSub] -= 1

                # add it to queue if it is 0, (means we have completed the course)
                if inCourses[depSub] == 0:
                    queue.append(depSub)
                    # increment the count to mark this subject as completed
                    count += 1


        return count == numCourses