import os
import tomllib as toml
from datetime import datetime


def read_project_info(project_dir):
    info_file = os.path.join(project_dir, "info.toml")
    with open(info_file, "rb") as f:
        project_info = toml.load(f)
    return project_info


def populate_project(portfolio_dir):
    projects = []
    # sort project by the date in it's name
    for project_name in sorted(
        os.listdir(portfolio_dir),
        key=lambda x: datetime.strptime(x.split("-")[0], "%Y%m%d"),
        reverse=True,
    ):
        project_dir = os.path.join(portfolio_dir, project_name)
        if os.path.isdir(project_dir):
            project_info = read_project_info(project_dir)
            projects.append(
                {
                    "name": project_info.get("name", ""),
                    "client": project_info.get("client", ""),
                    "date": project_info.get("date", datetime.strptime(project_name.split("-")[0], "%Y%m%d").date()),
                    "tags": project_info.get("tags", []),
                    "description": project_info.get("description", ""),
                    "icon": project_info.get("icon", ""),
                    "cover_picture": "",
                    "pictures": [],
                }
            )
            gallery_dir = os.path.join(project_dir, "gallery")
            if os.path.isdir(gallery_dir):
                projects[-1]["pictures"] = [
                    os.path.join(gallery_dir, file) for file in os.listdir(gallery_dir)
                ]
                projects[-1]["cover_picture"] = projects[-1]["pictures"][0]
    return projects


projects = populate_project("portfolio")
