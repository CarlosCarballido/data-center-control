# Data Center Control System - Expert System Using CLIPS

This project implements an expert system using **CLIPS** and **Python** to control and monitor a Data Center. The system monitors environmental factors such as temperature, humidity, and power supply, while also managing access control, disaster detection, and climate regulation through a rule-based inference engine.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The system is composed of three main components:
1. **Monitoring Subsystem**: Collects data from sensors in the Data Center such as temperature, humidity, and access requests.
2. **Control Module**: A rule-based expert system developed in **CLIPS** that processes the input data and makes decisions based on predefined rules.
3. **Actuation Subsystem**: Executes the control actions (like adjusting the air conditioning or restricting access) based on the decisions from the control module.

The system's goal is to ensure that the Data Center operates within optimal environmental conditions and provides secure access control, while being able to detect and react to disaster scenarios like fires or floods.

## Features

- **Access Control**: Manages entry to different zones in the Data Center based on user access levels.
- **Climate Control**: Maintains optimal temperature and humidity levels in various zones.
- **Disaster Detection**: Detects and reacts to fire and flood conditions, triggering the appropriate disaster recovery protocols.
- **Power Monitoring**: Monitors power supply to racks and triggers alerts if voltage levels are outside the safe range.

## Technologies

- **CLIPS**: Used for implementing the expert system's rules and inference engine.
- **Python**: Used to manage the integration with CLIPS and simulate the monitoring and actuation subsystems.
- **clipspy**: Python library that provides integration with the CLIPS engine.

## Setup

### Prerequisites
To run this project, you'll need:
- Python 3.x
- CLIPS
- clipspy library for Python
