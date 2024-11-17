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

Konstantinos Mitalloulis


