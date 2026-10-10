from fastapi import FastAPI
from models import Project, Developer

app=FastAPI()

@app.post('/developer')
def create_developer(developer:Developer):
    return {"message":"Developer created successfully","developer":developer}
    #mas returnit cdo kopd eshte i paarritshem aty perfundon

@app.post("/project")
def create_project(project:Project):
    return{"message":"Project created successfully!","project":project}

@app.get('/project')
def get_projects():
    developer:Developer=Developer(name="Artiol",experience=2)
    sample_project:Project=Project(title="Hr Management System",description="This a sample project",
                                   languages=["Python","Javascript","SQL"],lead_developer=developer)
    return {"projects":[sample_project]}
