from django.test import TestCase, Client
from challenges_app.models import Challenges


class YourTestClass(TestCase):

    def setUp(self):
        # Create sample challenges for testing
        Challenges.objects.create(
            title="Python_Basics",
            full_title="Introduction to Python Programming",
            description="""---
title: Python Basics
author: Alice-c123
course: CS101
week: 1
topics: "['Variables', 'Control Flow', 'Functions']"
This challenge introduces the fundamentals of Python programming.
Participants will explore variables, control flow, and functions.
---
https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/""",
            course="CS101",
            week="1",
            author="Alice-c123",
        )

        Challenges.objects.create(
            title="Data_Analysis",
            full_title="Analyzing Data with Python",
            description="""---
title: Data Analysis
author: CharlieData
course: DATA300
week: 5
topics: "['Pandas', 'Matplotlib', 'Data Visualization']"
---
Explore the world of data analysis using Python. This challenge covers
Pandas, Matplotlib, and data visualization techniques.""",
            course="DATA300",
            week="5",
            author="CharlieData",
        )

        Challenges.objects.create(
            title="Machine_Learning",
            full_title="Introduction to Machine Learning",
            description="""---
title: Machine Learning
author: DaveML
course: ML400
week: 7
topics: "['Supervised Learning', 'Unsupervised Learning', 'Model Evaluation']"
Dive into the fascinating field of machine learning. Participants will
learn about supervised learning, unsupervised learning, and model evaluation.
---
## Blocks
<details open>
    <summary>Did you know?</summary>
    You can create a note with Blocks!
</details>
<details>
    <summary>Hidden note</summary>
    Secret inside!
</details>""",
            course="ML400",
            week="7",
            author="DaveML",
        )

    def test_index(self):
        # Test the index page
        client = Client()
        response = client.get("/")
        print(f"{response.context}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["challenges"]), 3)

    def test_problem_view1(self):
        # Test the Machine Learning challenge page
        client = Client()
        response = client.get("/problems/Machine_Learning")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Did you know?")
        self.assertContains(response, "Hidden note")

    def test_problem_view2(self):
        # Test the Data Analysis challenge page
        client = Client()
        response = client.get("/problems/Data_Analysis")
        self.assertEqual(response.status_code, 200)
        expected_text = "Explore the world of data analysis using Python. This challenge covers\nPandas, Matplotlib, and data visualization techniques."
        response_content = response.content.decode("utf-8")
        self.assertIn(expected_text, response_content)

    def test_problem_view3(self):
        # Test a page that does not exist
        client = Client()
        response = client.get("/problems/NotExists")
        self.assertEqual(response.status_code, 404)

    def test_problem_view4(self):
        # Test the Python Basics challenge page with LaTeX link
        client = Client()
        response = client.get("/problems/Python_Basics")
        self.assertEqual(response.status_code, 200)
        expected_latex_link = '<p><a href="https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/">https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/</a></p>'
        self.assertContains(response, expected_latex_link)
