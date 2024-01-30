# AlumChallenges
A web application for and by alumns of Harvard University's CS50 Introduction to Computer Science.

The title is not yet official. We don't need to worry about aesthetics until the MVP is done.

## Our aims
- Create a community-run platform for CS50 students to create their own problem sets for extra practice
- Gamify extra practice in programming exercise's.
- Expand the portfolio of CS50 alumni.

## TODO:
These are the steps needed to create a minimum viable product (MVP)
- Log in via OAuth
- View problems
- Use check50 to validate
- Submit50 to push solution
- See what you solved

Note: This project is an initiative of enthusiastic CS50 alums. This project is not part of or endorsed by CS50, HarvardX or Harvard University. The entire project is unofficial.

## Usage:

``` shell
pipenv sync
pipenv run server

# migrating
pipenv run makemigrations
pipenv run migrate
```

## Usage of check50:

```shell
# execute this command to check your problem where <problem> stands for its name
check50 typicallythomas/AlumChallenges/main/problem_tests/<problem>
```
