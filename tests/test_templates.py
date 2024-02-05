from django.test import TestCase, Client
from challenges_app.models import Challenges


class YourTestClass(TestCase):

    def setUp(self):
        Challenges.objects.create(
            title="Python Basics",
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
            title="Data Analysis",
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
            title="Machine Learning",
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
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["problems"]), 3)

    def test_problem_view(self):
        client = Client()

        response1 = client.get("/problems/Machine Learning")
        self.assertEqual(response1.status_code, 200)
        self.assertContains(response1, "Did you know?")
        self.assertContains(response1, "Hidden note")

        response2 = client.get("/problems/Data Analysis")
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, "Analyzing Data with Python")

        expected_text = "Explore the world of data analysis using Python. This challenge covers\nPandas, Matplotlib, and data visualization techniques."
        response_content = response2.content.decode("utf-8")
        self.assertIn(expected_text, response_content)

        response3 = client.get("/problems/NotExists")
        self.assertEqual(response3.status_code, 404)

        response4 = client.get("/problems/Python Basics")
        self.assertEqual(response4.status_code, 200)
        print(response4.content.decode("utf-8"))
        expected_latex_link = '<p><a href="https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/">https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/</a></p>'

        # Check for the presence of the LaTeX link
        self.assertContains(response4, expected_latex_link)
