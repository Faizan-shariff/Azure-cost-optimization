# Azure-cost-optimization
Complete cost optimization solution for your Azure serverless billing system, designed to reduce Cosmos DB storage costs while maintaining data availability, simplicity, and zero downtime.

___________________________________________________________________________________________________________________________

This solution implements a cost-optimized serverless architecture for managing billing records using Azure services. It separates hot and cold data by retaining recent billing records (less than 3 months old) in Azure Cosmos DB and archiving older, infrequently accessed records to Azure Blob Storage. A timer-triggered Azure Function automatically handles the archival process daily, ensuring no data loss or downtime while maintaining API compatibility. The infrastructure is provisioned using Terraform, and the entire deployment process—including infrastructure setup and function publishing—is fully automated through an Azure DevOps YAML pipeline. This approach significantly reduces storage and query costs while preserving long-term data availability and simplicity of maintenance.

![flow_diag](https://github.com/user-attachments/assets/600dc586-370f-4bf5-bcb9-2562e5548a72)
![config_diag](https://github.com/user-attachments/assets/a0c7e62e-60f7-4b87-ad53-95ebee119eda)
