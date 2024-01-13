import asyncio
import os
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

import aiohttp
from github_stats import Stats


async def main():

    load_dotenv()

    access_token = os.getenv("ACCESS_TOKEN")
    user = os.getenv("GITHUB_ACTOR")

    if access_token is None or user is None:
        raise RuntimeError(
            "ACCESS_TOKEN and GITHUB_ACTOR environment variables cannot be None!"
        )
        
    async with aiohttp.ClientSession() as session:
        s = Stats(user, access_token, session)
        print(await s.to_str())

    # Setup Enviroment
    env = Environment(loader=FileSystemLoader("template"))
    template = env.get_template("README_TEMPLATE.md")

    # Render Template
    rendered_readme = template.render()

    # Save to README.md
    with open("README.md", "w") as f:
        f.write(rendered_readme)


if __name__ == "__main__":
    asyncio.run(main())