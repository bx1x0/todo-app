from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do App</title>
</head>
<body>
    <h1>My To-Do List</h1>

    <form method="POST">
        <input type="text" name="task" placeholder="Enter task" required>
        <button type="submit">Add</button>
    </form>

    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template_string(HTML, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
