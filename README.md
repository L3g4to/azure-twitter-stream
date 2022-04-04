# Azure Twitter Stream Data to EventHub

The project is aimed at creating an easy deployment of an Azure Databricks Notebook that can stream filtered Tweets to an Azure EventHub. The benefit of this approach is the ability to quickly setup and then delete all infrastructure. 

Follow instructions below on how to deploy your infrastructure to Azure. You will need to also create a KeyVault for the secrets used in the Databricks Notebook.

You will also need to acquire a token for the [Twitter API](https://developer.twitter.com/en/docs/twitter-api/tutorials).

# Producer and Consumer

The code is broken down into 2 Python Notebooks - a Producer and Consumer model. The Producer captures Tweets through the Twitter REST API and pushes them into the Azure EventHub. The Consumer (can work on the same Cluster) listens for EventHub events and extracts the Tweet data. 

# Azure DevOps deployment:

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

# Azure KeyVault

It is recommended to reference your secrets using an Azure KeyVault which you will access through an Azure Databricks secret scope.

The following secrets are being kept in an Azure KeyVault:
* **EventHubNamespace** - EventHub namespace.
* **EventHubName** - EventHub name.
* **EventHubPolicy** - the EventHub policy name.
* **EventHubSAS** - the SAS token for the Policy.
* **EventHubServicebus** - the EventHub namespace service bus.
* **BearerToken** - your Twitter bearer token.
