from flask import Blueprint, request

from categorization.controller import comment_categorization

# cria a blueprint para categorization
categorization_bp = Blueprint("categorization", __name__)

@categorization_bp.route("/categorization", methods=["POST"])
def get_comment_categorization():

    body = request.get_json()

    headers = request.headers

    api_key = headers.get("api-key")

    categories = body.get("categories", [])

    comments = body.get("comments", [])
    
    instructions = body.get("instructions", "")
    
    model = headers.get("model", "")

    return comment_categorization(api_key, categories, comments, instructions, model)