# End-To-End-Data-Engineering-Project
1. Microsoft SQL Server (On-premise was installed on local computer).
   Data source: https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms (AdventureWorksLT2022.bak)
2. Azure Data Factory (Ingestion). Copy of all schemas and tables into bronze container (Azure Storage Account).
3. Medalion transformation by using Azure Databricks (bronze to silver & silver to gold)
