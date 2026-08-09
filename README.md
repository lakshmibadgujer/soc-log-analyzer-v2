# 🛡️ SOC Log Analyzer V2

A Python-based SOC (Security Operations Center) log analysis tool that reads security logs and identifies important security events.

## 🎯 Project Objective

The purpose of this project is to practice how a SOC analyst can analyze security logs using Python and identify suspicious security-related events.

## 🔍 Features

* Reads security log files
* Detects failed login attempts
* Counts failed login attempts
* Generates a security report
* Separates error logs
* Displays log statistics and percentages
* Allows the user to enter a log file name
* Extracts IP addresses from failed login attempts
* Counts failed attempts by IP address

## 🛠️ Technologies Used

* Python 3
* Linux
* Git & GitHub
* Regular Expressions (Regex)
* File Handling
* Date & Time

## 📂 Project Structure

```text
soc-log-analyzer-v2/
│
├── analyzer.py
├── cybersecurity.logs
├── ERROR_LOGS.txt
├── Report.txt
└── README.md
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/lakshmibadgujer/soc-log-analyzer-v2.git
```

Move into the project directory:

```bash
cd soc-log-analyzer-v2
```

Run the analyzer:

```bash
python3 analyzer.py
```

The program reads the selected log file and displays the analyzed security events.

## 📊 Example Log Events

```text
INFO User login successful
WARNING CPU usage high
ERROR Failed login attempt
ERROR Malware detected
```

## 📄 Generated Output

The project can generate:

* `Report.txt` — summary of analyzed logs
* `ERROR_LOGS.txt` — extracted error events

The report includes information such asexpressions. 

```text
Total logs
Info logs
Error logs
Warning logs
Percentages
Date
Time
```

## 🔐 Failed Login & IP Analysis

The project also analyzes failed login attempts and extracts IP addresses using Python regular expressions.as

Example:

```text
Failed password for admin from 192.168.1.10
Failed password for root from 10.0.0.5
Failed password for test from 10.0.0.5
```

The analyzer can count how many failed login attempts came from each IP address.

## 🧠 SOC Skills Practiced

* Security log analysis
* Authentication event analysis
* Failed login detection
* IP address analysis
* Python file handling
* Python Regex
* Log parsing
* Linux command-line usage
* Git & GitHub workflow

## 🚀 Future Improvements

* Real-time log monitoring
* Suspicious IP detection
* Automated alerts
* Brute-force detection
* SIEM integration
* More advanced threat detection

## 👩‍💻 Author

**Lakshmi Badgujer**

Cybersecurity Learner | SOC Analyst Aspirant
