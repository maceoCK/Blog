from collections import defaultdict

sampleGraph = {"Calc3": ["Calc1", "Calc2", "PreCalc"],
               "English": [],
               "Computer Science": ["Calc2"],
               "Machine Learning": ["Computer Science"],
               "Technical Writing": ["English"]}

def countPreReqs(sampleGraph):
    preReqCount = defaultdict(int)

    for course, prerequisites in sampleGraph.items():
        preReqCount[course]  # Initialize the course with 0 prerequisites
        for prereq in prerequisites:
            preReqCount[prereq] += 1

    return preReqCount

preReqCounts = countPreReqs(sampleGraph)
print(preReqCounts)
