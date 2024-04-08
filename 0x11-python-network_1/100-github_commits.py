#!/usr/bin/python3
"""
This script fetches the last 10 commits from a GitHub repository
specified by the repository name and owner name provided as
command-line arguments. It then displays each commit's SHA and author name.
"""
import requests
import sys

if __name__ == '__main__':
    # Extract repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Set up the URL for the GitHub API to fetch the commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Extract the last 10 commits if the request is successful
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the last 10 commits
        # Print each commit in the desired format
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
