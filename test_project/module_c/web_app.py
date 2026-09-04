from flask import Flask, jsonify
import click
from rich.console import Console
from rich.table import Table
import requests

app = Flask(__name__)
console = Console()


@app.route("/status")
def status():
    return jsonify({"status": "ok"})


@click.command()
@click.option("--port", default=5000)
def run(port):
    console.print(f"Starting server on port {port}")
    app.run(port=port)
