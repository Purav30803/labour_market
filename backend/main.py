from fastapi import FastAPI
from controller import skill_cluster_controller

app = FastAPI(
    title="Skill Cluster API",
    description="API for predicting job skill clusters using KMeans + TF-IDF",
    version="1.0.0"
)

app.include_router(skill_cluster_controller.router)
