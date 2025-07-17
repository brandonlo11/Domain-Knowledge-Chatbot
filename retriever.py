from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "wf3hn39jn9"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def get_prerequisites(course_code):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (c:Course {code: $code})-[:HAS_PREREQUISITE]->(p:Course)
            RETURN p.code AS code, p.name AS name
            """,
            code=course_code
        )
        return [record.data() for record in result]

def get_courses_with_prereq(prereq_code):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (c:Course)-[:HAS_PREREQUISITE]->(p:Course {code: $prereq})
            RETURN c.code AS code, c.name AS name
            """,
            prereq=prereq_code
        )
        return [record.data() for record in result]

def get_all_courses():
    with driver.session() as session:
        result = session.run(
            "MATCH (c:Course) RETURN c.code AS code, c.name AS name"
        )
        return [record.data() for record in result] 