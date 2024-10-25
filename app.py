from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
courses = [
    {"id": 1, "name": "Introduction to Computer Science"},
    {"id": 2, "name": "Data Science Basics"},
    {"id": 3, "name": "Web Development Bootcamp"},
    {"id": 4, "name": "Health and Wellness"},
    {"id": 5, "name": "Art History"},
]

@app.route('/api/search', methods=['GET'])
def search_courses():
    keyword = request.args.get('keyword', '').lower()
    results = [course for course in courses if keyword in course['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)