PROJEKT NOCH IN BEARBEITUNG

Hallo!

Ziel dieses Projekts ist der Aufbau eines Data Warehouses, das Fußballdaten aus drei verschiedenen Quellen (Webseiten) sammelt.
Alle verwendeten Services (Postgres, Airflow, Metabase, pgAdmin) sind über Docker Compose integriert, d. h., sie laufen in separaten Docker-Containern.

Die Tasks werden mithilfe von Airflow orchestriert. Es gibt zwei DAGs:

Initialisierung: Dient zur Erstbefüllung des Data Warehouses.
Aktualisierung: Ermöglicht das regelmäßige Aktualisieren der Daten.
Beide DAGs müssen manuell gestartet werden.

Verwendete Technologien:

Programmiersprache: Python
Datenbank: PostgreSQL
Orchestrierung: Apache Airflow
Containerisierung: Docker
Visualisierung: Metabase

PROJECT STILL IN PROGRESS

Hello!

The goal of this project is to build a Data Warehouse that collects football data from three different sources (websites).
All services used (Postgres, Airflow, Metabase, pgAdmin) are integrated via Docker Compose, meaning they run in separate Docker containers.

Tasks are orchestrated using Airflow. There are two DAGs:

Initialization: Responsible for the initial population of the Data Warehouse.
Update: Enables the regular updating of data.
Both DAGs must be started manually.

Technologies used:

Programming language: Python
Database: PostgreSQL
Orchestration: Apache Airflow
Containerization: Docker
Visualization: Metabase

Konstantinos Mitalloulis
