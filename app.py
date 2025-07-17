from fastapi import FastAPI, Request
from retriever import get_prerequisites, get_courses_with_prereq, get_all_courses
import string

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question", "").lower()

    # Simple rule-based routing for demo
    if "prerequisite" in question and "for" in question:
        # e.g., "What are the prerequisites for CS 180?"
        course_code = question.split("for")[-1].strip().upper()
        # Remove punctuation (like '?')
        course_code = course_code.strip(string.punctuation + " ")
        prereqs = get_prerequisites(course_code)
        if prereqs:
            return {"answer": f"Prerequisites for {course_code}: " + ", ".join([f"{c['code']} ({c['name']})" for c in prereqs])}
        else:
            return {"answer": f"{course_code} has no prerequisites."}
    elif "require" in question and "as a prerequisite" in question:
        # e.g., "Which courses require CS 31 as a prerequisite?"
        prereq_code = question.split("require")[1].split("as a prerequisite")[0].strip().upper()
        courses = get_courses_with_prereq(prereq_code)
        if courses:
            return {"answer": f"Courses that require {prereq_code}: " + ", ".join([f"{c['code']} ({c['name']})" for c in courses])}
        else:
            return {"answer": f"No courses require {prereq_code} as a prerequisite."}
    elif "all courses" in question:
        courses = get_all_courses()
        return {"answer": "All courses: " + ", ".join([f"{c['code']} ({c['name']})" for c in courses])}
    else:
        return {"answer": "Sorry, I can't answer that yet. Try asking about prerequisites or course lists."} 