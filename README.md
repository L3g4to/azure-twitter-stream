# Azure Twitter Stream Data to EventHub

The project is aimed at creating an easy deployment of an Azure Databricks Notebook that can stream filtered Tweets to an Azure EventHub.

Follow instructions below on how to deploy your infrastructure to Azure. You will need to also create a KeyVault for the secrets used in the Databricks Notebook.


# Azure DevOps Library Variables:

The settings below apply in case you would be using Azure Devops to deploy the infrastructure (infra folder).

## Step 1: Create a new repository and clone this Git

## Step 2: Create a Service Connection

## Step 3: Create a new Library within the Pipeline settings

Add the following items:
* **CONNECTION** - Azure DevOps Service Connection
* **DATABRICKS_WORKSPACE_NAME** - Databricks workspace name
* **EVENTHUB_NAMESPACE** - Name of the EventHub namespace
* **EVENTHUB_NAME** - Name of the EventHub (within the EventHub namespace)
* **LOCATION** - Deployment location (e.g. westeurope)
* **RESOURCE_GROUP** - Name for the Azure ResoureGroup
* **SUBSCRIPTION_ID** - Id of your Azure Subscription

## Step 4: Create a new Pipeline basis the YAML in the infra folder.
