from fastapi import APIRouter
from schema.skill_input import SkillInput
from service.skill_cluster_service import predict_cluster

router = APIRouter()

@router.post("/predict-skill-cluster/")
async def get_cluster(data: SkillInput):
    cluster_id, label = predict_cluster(data.qualifications)

    if cluster_id is None:
        return {
            "cluster_id": None,
            "cluster_label": "Unknown",
            "message": label  # the error message from service
        }

    return {
        "cluster_id": cluster_id,
        "cluster_label": label,
        "message": f"This job matches the '{label}' skill set"
    }
