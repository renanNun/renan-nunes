import os
from jinja2 import Environment, FileSystemLoader


def main():

    # Setup Enviroment
    env = Environment(loader=FileSystemLoader("template"))
    template = env.get_template("README_TEMPLATE.md")

    # Render Template
    rendered_readme = template.render()

    # Save to README.md
    with open("README.md", "w") as f:
        f.write(rendered_readme)


if __name__ == "__main__":
   main()