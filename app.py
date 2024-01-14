from flask import Flask, jsonify, request, send_from_directory
import os
import json



app = Flask(__name__)

UPLOAD_FOLDER = ""
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return "Welcome to the Codeedex Store "

# Ignore favicon requests
@app.route("/favicon.ico")
def favicon():
    return ""



# Load product data from JSON file
with open("products.json", "r") as file:
    products = json.load(file)

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({"products": products})

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products["products"] if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], Brown_Jacket.jpg)

if __name__ == "__main__":
    app.run(debug=True)
