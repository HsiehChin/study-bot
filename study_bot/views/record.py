from flask import Blueprint, request, jsonify
from study_bot import model
from study_bot.lib import custom_except, record

record_api = Blueprint("record_api", __name__)


@record_api.route("/", methods=["POST"])
def register():
    data = request.get_json()
    try:
        model.record.add(data)
        return "", 200
    except custom_except.duplicateError:
        return "", 409


@record_api.route("/recent/<user_id>", methods=["GET"])
def get_recent(user_id):
    records = model.record.get_recent(user_id)
    return jsonify(record.gen_seq(records))
