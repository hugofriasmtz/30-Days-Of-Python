import os
from datetime import datetime, timezone
from pathlib import Path

from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE")
COLLECTION_NAME = "students"

if not MONGODB_URI or not DATABASE_NAME:
	raise RuntimeError("Missing MONGODB_URI or MONGODB_DATABASE in .env")

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
students = db[COLLECTION_NAME]


def now_iso():
	return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def ok_response(data, status=200):
	return jsonify(data), status


def error_response(message, status=400, extra=None):
	body = {"error": message}
	if extra:
		body.update(extra)
	return jsonify(body), status


def serialize_student(student):
	return {
		"id": str(student["_id"]),
		"name": student.get("name"),
		"country": student.get("country"),
		"city": student.get("city"),
		"age": student.get("age"),
		"created_at": student.get("created_at"),
		"updated_at": student.get("updated_at"),
	}


def parse_json_body():
	if not request.is_json:
		return None, error_response("Content-Type must be application/json", 415)

	data = request.get_json(silent=True)
	if data is None:
		return None, error_response("Invalid JSON body", 400)

	if not isinstance(data, dict):
		return None, error_response("JSON body must be an object", 400)

	return data, None


def validate_payload(data, partial=False):
	required_fields = ["name", "country", "city", "age"]

	if not partial:
		missing_fields = [field for field in required_fields if field not in data]
		if missing_fields:
			return None, error_response("Missing fields", 400, {"fields": missing_fields})

	payload = {}
	for field in required_fields:
		if field in data:
			payload[field] = data[field]

	if "age" in payload:
		try:
			payload["age"] = int(payload["age"])
		except (TypeError, ValueError):
			return None, error_response("Age must be an integer", 400)

	for field in ["name", "country", "city"]:
		if field in payload and not str(payload[field]).strip():
			return None, error_response(f"{field.capitalize()} cannot be empty", 400)

	return payload, None


def find_student(student_id):
	if not ObjectId.is_valid(student_id):
		return None, error_response("Invalid student id", 400)

	student = students.find_one({"_id": ObjectId(student_id)})
	if student is None:
		return None, error_response("Student not found", 404)

	return student, None


@app.get("/")
def home():
	return ok_response(
		{
			"message": "Flask + MongoDB CRUD API",
			"collection": COLLECTION_NAME,
			"routes": {
				"GET /health": "Check database connection",
				"GET /api/students": "List students",
				"GET /api/students/<id>": "Get one student",
				"POST /api/students": "Create student",
				"PUT /api/students/<id>": "Replace student",
				"PATCH /api/students/<id>": "Update student",
				"DELETE /api/students/<id>": "Delete student",
			},
		}
	)


@app.get("/health")
def health():
    try:
        client.admin.command("ping")
        return ok_response({"status": "ok", "database": DATABASE_NAME})
    except PyMongoError as exc:
        return error_response("Database connection failed", 500, {"detail": str(exc)})


@app.get("/api/students")
def list_students():
	try:
		items = [serialize_student(student) for student in students.find().sort("name", 1)]
		return ok_response(items)
	except PyMongoError as exc:
		return error_response("Failed to list students", 500, {"detail": str(exc)})


@app.get("/api/students/<student_id>")
def get_student(student_id):
    student, response_error = find_student(student_id)
    if response_error:
        return response_error

    return ok_response(serialize_student(student))


@app.post("/api/students")
def create_student():
	data, response_error = parse_json_body()
	if response_error:
		return response_error

	payload, response_error = validate_payload(data)
	if response_error:
		return response_error

	timestamp = now_iso()
	document = {
		**payload,
		"created_at": timestamp,
		"updated_at": timestamp,
	}

	try:
		result = students.insert_one(document)
		created_student = students.find_one({"_id": result.inserted_id})
	except PyMongoError as exc:
		return error_response("Failed to create student", 500, {"detail": str(exc)})

	return ok_response(serialize_student(created_student), 201)


@app.put("/api/students/<student_id>")
def replace_student(student_id):
	student, response_error = find_student(student_id)
	if response_error:
		return response_error

	data, response_error = parse_json_body()
	if response_error:
		return response_error

	payload, response_error = validate_payload(data)
	if response_error:
		return response_error

	timestamp = now_iso()
	document = {
		**payload,
		"created_at": student.get("created_at", timestamp),
		"updated_at": timestamp,
	}

	try:
		students.replace_one({"_id": student["_id"]}, document)
		updated_student = students.find_one({"_id": student["_id"]})
	except PyMongoError as exc:
		return error_response("Failed to replace student", 500, {"detail": str(exc)})

	return ok_response(serialize_student(updated_student))


@app.patch("/api/students/<student_id>")
def update_student(student_id):
	student, response_error = find_student(student_id)
	if response_error:
		return response_error

	data, response_error = parse_json_body()
	if response_error:
		return response_error

	payload, response_error = validate_payload(data, partial=True)
	if response_error:
		return response_error

	if not payload:
		return error_response("No fields provided to update", 400)

	payload["updated_at"] = now_iso()

	try:
		students.update_one({"_id": student["_id"]}, {"$set": payload})
		updated_student = students.find_one({"_id": student["_id"]})
	except PyMongoError as exc:
		return error_response("Failed to update student", 500, {"detail": str(exc)})

	return ok_response(serialize_student(updated_student))


@app.delete("/api/students/<student_id>")
def delete_student(student_id):
	student, response_error = find_student(student_id)
	if response_error:
		return response_error

	try:
		students.delete_one({"_id": student["_id"]})
	except PyMongoError as exc:
		return error_response("Failed to delete student", 500, {"detail": str(exc)})

	return ok_response({"message": "Student deleted successfully", "id": student_id})


@app.errorhandler(404)
def not_found(_error):
    return error_response("Route not found", 404)


@app.errorhandler(405)
def method_not_allowed(_error):
    return error_response("Method not allowed", 405)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
