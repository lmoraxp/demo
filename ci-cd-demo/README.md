# CI/CD Demonstration Project

This project is a simple demonstration of a CI/CD pipeline using GitHub Actions. It includes a Python application that prints a message to the console and is set up to automatically run tests and deploy using GitHub workflows.

## Project Structure

```
ci-cd-demo
├── src
│   └── main.py
├── .github
│   └── workflows
│       └── ci-cd.yml
├── requirements.txt
└── README.md
```

## Getting Started

To set up and run this project locally, follow these steps:

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ci-cd-demo
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, install the required packages using:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the application by executing:
   ```
   python src/main.py
   ```

   This should output:
   ```
   Hello, CI/CD!
   ```

## CI/CD Process

This project uses GitHub Actions for continuous integration and deployment. The workflow is defined in the `.github/workflows/ci-cd.yml` file. 

### Workflow Triggers

The CI/CD pipeline is triggered on:
- Push events to the main branch
- Pull requests targeting the main branch

### Jobs

The workflow includes jobs for:
- Running tests
- Deploying the application (if applicable)

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.