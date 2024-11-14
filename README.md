# Flask File Converter

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [File: app.py Context](#file-apppy-context)
8. [Troubleshooting](#troubleshooting)
9. [License](#license)

---

## Overview
Flask File Converter is a web-based application that allows users to upload files, convert them to a desired format, and download the converted versions. The application is built using Flask and features error handling, logging, and a user-friendly interface.

---

## Prerequisites
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Virtual Environment**: Recommended for dependency management

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Chandan062311/doc-pdf-converter
    cd repository
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
    - **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

1. **Environment Variables**

    Create a `.env` file in the project root and add the following:
    ```env
    SECRET_KEY=your-secret-key
    UPLOAD_FOLDER=uploads
    ```

2. **Create Uploads Directory**
    ```bash
    mkdir uploads
    ```

---

## Usage

1. **Run the Application**
    ```bash
    python app.py
    ```

2. **Access the Application**
    Open your browser and navigate to `http://localhost:5000`.

---

## Project Structure
repository/ │ ├── app.py ├── requirements.txt ├── .env ├── uploads/ ├── templates/ │ └── index.html └── README.md


---

