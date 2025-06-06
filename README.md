# CodeGPT

![til](./static/gif/home.gif)

## What it does ⚙️

When you submit a GitHub repository link or a code snippet to CodeGPT, it can to generate a line-by-line summary of the repo in plain text. This allows developers to quickly understand the project and start contributing.

When a GitHub repository link is submitted, our app uses the GitHub API to walk through all files within the repository and retrieve the code in each file. Using a fine-tuned CodeT5 code-to-text model from Hugging Face, all code within the repository can be summarized. The original code and its corresponding summarization are displayed side-by-side, allowing developers to understand the code segments easily. If the user creates an account on our application, it also stores all past searches to allow easy future access.

## How we built it 👷‍♀️🔧

We built our web application using Python with Flask framework, HTML, Tailwind CSS, MongoDB Atlas for the database and downloaded a CodeT5-base model for code summarization.

## Screenshots

![Example code snippet result.](./static/images/example_code_snippet_result.png)

![Example GitHub Repository Result.](./static/images/example_github_repo_result.png)

![Create account page.](./static/images/create_account.png)

![Sign in page.](./static/images/sign_in.png)
