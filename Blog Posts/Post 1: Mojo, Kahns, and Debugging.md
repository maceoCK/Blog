# Post 1: Mojo, Kahns, and Debugging

## October 19th 2023

### What I learned today

1. Delayed understanding of kahn's algorithm.
2. What is MOJO, how does it work, and why should be be excited that it is coming to mac.
3. Debugging is important and using a debugger is something I need to watch a video on.
4. Hacker news and lobster are interesting and maybe I can be semi-productive in my procrastination.

#### Delayed understanding of kahn's algorithm

> RECAP: I had an interview question in the final round of an interview which I was not prepared for last week.
> This question from an undisclosed country was presented to me in the final round of interviewing but due to my unfamiliarity with the question I stumbled through it awkwardly in a way which I feel led to me ultimately getting rejected.

**What was this question you ask?**

It was a question that basically asked me to topologically sort a dependency graph.

For people who dont know what that means:

* Dependency graphs
  * Think of dependency graphs as each node being a course and each edge showing the prerequisite relation of the courses
  * A dependency graph can help illustrate the relationships between courses and the courses that must be completed before taking a particular course.
  * Here's how a dependency graph can be used with courses and prerequisites as an example:
    * Imagine you're planning a college curriculum, and you have a list of courses, each with its own set of prerequisites. You want to visualize which courses depend on completing other courses before they can be taken. You can represent this information in a dependency graph.

* **Example courses which could be shown in a dependency graph**

  * Calculus I
    * Prerequisites: None
  * Calculus II
    * Prerequisites: Calculus I
  * Physics I
    * Prerequisites: Calculus I
  * Physics II
    * Prerequisites: Physics I
  * Computer Science 101
    * Prerequisites: None
  * Data Structures
    * Prerequisites: Computer Science 101
  * Algorithms
    * Prerequisites: Data Structures

* Topological sort
  * Using this same analogy a topological sort is a linear ordering of the nodes (courses) in a directed acyclic graph (DAG) that respects the partial order imposed by the edges (prerequisites). In the context of courses with prerequisites, a topological sort arranges the courses in a sequence such that no course is taken before its prerequisites
  * The topologically sorted version of that previous example would be:
    1. Calculus I
    2. Computer Science 101
    3. Physics I
    4. Calculus II
    5. Data Structures
    6. Physics II
    7. Algorithms
*Sorry for explaining that all, but it was useful for me*
**The way I learned you were supposed to do it was using kahn's agorithm you can find kahn's algo in this repo in the aditional resources directory (ADD THAT THEN REMOVE THESE PARENTHESES)**

#### MOJO

I saw this on hackernews after being told to read that so I can blend in like a chameleleon and learn all the jargon.

The top post when I looked at the page was the mojo was avaliable for mac and having no idea what mojo was I looked it up and did a little research. From what I found:
Mojo isn't your typical programming language; it's designed to complement the Project Jupyter ecosystem. While not a Python clone, it introduces unique features like "fn" for compiled functions and "struct" for memory-efficient data structures.
What's intriguing is Mojo's compatibility with existing Python code through the CPython runtime. Plus, it incorporates a borrow checker inspired by Rust, setting it apart from Python for memory safety and low-level programming.
ITS ALSO WAY FASTER!!! (68000 times according to their website but I am not sure how accurate that number is though)

#### Debugging is important

This is exactly what the title says, expect next post to be about my debugging lab and me struggling to figure out what is wrong with my Eclipse editor. I need to debug some code but I am actually struggling to use eclipses debugger and I am refusing to resort to colsole logs.

#### Hacker news and lobster are interesting

Same as the header, theyre interesting. I feel like I can actually intergrate myself into the subculture of development which I have always admired from afar.
