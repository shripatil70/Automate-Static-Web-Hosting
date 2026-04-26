# 🚀 AWS Static Website Hosting Automation (Python + boto3)

## 📌 Overview

This project automates the deployment of a static website on AWS S3 using Python (boto3). It eliminates manual configuration by programmatically creating and configuring S3 buckets for public web hosting.

---

## 🎯 Objectives

* Automate static website deployment on AWS
* Enable public access securely
* Apply Infrastructure-as-Code (IaC) principles

---

## 🧰 AWS Services Used

* **Amazon S3** – Static website hosting

---

## ⚙️ Features

* ✅ S3 bucket creation
* ✅ Static website hosting enablement
* ✅ Disable Block Public Access
* ✅ Public bucket policy configuration
* ✅ HTML file upload
* ✅ Fully automated deployment

---

## 🏗️ Architecture

| Component      | Description          |
| -------------- | -------------------- |
| User (Browser) | Sends HTTP request   |
| S3 Bucket      | Hosts static website |
| index.html     | Website content      |
| Public Policy  | Allows global access |

---

## 📂 Project Structure

```
static-site-automation/
│── main.py
│── config.py
│── s3_setup.py
│── upload_files.py
│── website/
│     └── index.html
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```
git clone https://github.com/<your-username>/aws-static-site-automation.git
cd static-site-automation
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure AWS Credentials

```
aws configure
```

### 4️⃣ Run Script

```
python main.py
```

---

## 📸 Screenshots

###  Website Output
![Alt Text](https://github.com/shripatil70/Automate-Static-Web-Hosting/blob/3c7c127057badf4623b34dbbbfd5828886be6921/screenshots/output.png)

###  Terminal Output
![Terminal](https://github.com/shripatil70/Automate-Static-Web-Hosting/blob/3c7c127057badf4623b34dbbbfd5828886be6921/screenshots/terminal.png)

---

## ⚠️ Important Notes

* Bucket name must be globally unique
* Disable Block Public Access before applying policy
* Ensure `index.html` exists
* Website URL works only after propagation (~1–2 minutes)

---

## 🧠 Key Learnings

* AWS S3 automation using boto3
* Static website hosting configuration
* Handling AWS security settings (Block Public Access)
* Debugging deployment issues

---

## 🚀 Future Enhancements

* Add **CloudFront (CDN + HTTPS)**
* Configure **custom domain (Route 53)**
* Upload multiple assets (CSS, JS, images)
* CI/CD pipeline integration

---

## 👩‍💻 Author

Dhanashri Patil
