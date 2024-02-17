variable "credentials" {
    description = "My credentials"
    default = "/home/codespace/.config/gcloud/application_default_credentials.json"
}

variable "project" {
    description = "Project"
    default = "de-zoomcamp-414604"
}

variable "region" {
    description = "Region"
    default = "us-cental1"
}

variable "location" {
    description = "Project location"
    default = "US"
}

variable "bq_dataset_name" {
    description = "My Bigquery Dataset Name"
    default = "yellow_taxi"
}

variable "gcs_bucket_name" {
    description = "My Storage Bucket Name"
    default = "terraform-yellow-bucket"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}
