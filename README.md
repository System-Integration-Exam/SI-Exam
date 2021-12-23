# System Integration 2021 Exam

## Contributors
- [Emil Jógvan Svensmark - cph-eb122](https://github.com/Svensmark)
- [Emil Skovbo - cph-es149](https://github.com/Emil-Skovbo)
- [Henning Wiberg - cph-hw98](https://github.com/Mutestock)
- [Sofus Hilfling Nielsen - cph-sn331](https://github.com/sofushn)

[Exam Assignment Document]()

The repository is hosted online on GitHub at https://github.com/System-Integration-Exam/SI-Exam

## Video
[![Presentation Video](https://img.youtube.com/vi/unbdrz68lLU/0.jpg)](https://www.youtube.com/watch?v=unbdrz68lLU "SI Exam Demo")

_The video is also zipped with the project as a .mp4 file_
# Table of Contents

- [Business case](#business-case)
  * [Domain](#domain)
  * [Requirements](#requirements)
- [Architecture](#architecture)
  * [Legacy System](#legacy-system)
  * [Modern Solution](#modern-solution)
  * [Technologies](#technologies)
    + [gRPC](#grpc)
    + [Camunda](#camunda)
    + [Kafka](#kafka)
    + [Docker & Kubernetes](#docker-and-kubernetes)
- [Development Process](#development-process)
- [Run](#run)
  * [Prerequisites](#prerequisites)
  * [Kubernetes with Minikube](#kubernetes-with-minikube)
    + [1. Start minikube cluster](#1-start-minikube-cluster)
    + [2. Tunnel to cluster](#2-tunnel-to-cluster)
    + [3. Apply kubernetes deployments](#3-apply-kubernetes-deployments)
  * [Access to services](#access-to-services)
- [Gateway Endpoints](#gateway-endpoints)
  * [Metadata](#metadata)
    + [Book](#book)
    + [Song](#song)
    + [Vinyl](#vinyl)
  * [Reservation](#reservation)
  * [Restock](#restock)
  * [Subscription](#subscription)
    + [Customer](#customer)
    + [Subscription](#subscription-1)
  * [Warehouse](#warehouse)


# Business case

A book & vinyl subscription renting chain called Vintage Champions. The concept is derived from an older version of blockbuster where you physically had to pick up the item from the store. Each store have their own inventory of books & vinyl’s that can be rented if you have a subscription service with the chain. 

## Domain

We designed our system with a domain-driven-design approach which meant that we needed a domain diagram that contained all our vocabulary from our business domain:
![Domain Model](/assets/domain_model.png "Domain Model")

## Requirements

- Integration with external REST API for retrieving item metadata
- 
- Transform old customer data from legacy system into modern system
- Use of BPMN to handle restocking of new or existing items
- Microservice orchestration with Kubernetes
- Basic console logging and monitoring


# Architecture

## Legacy System

Vintage Champions is currently using an old legacy system that is deployed to each of their stores. This system has a basic frontend GUI for the employees and the system stores all the data in individual csv files.

![Old architecture](/assets/legacy_system_architecture.png "Old architecture")

## Modern Solution

The new system is a microservice solution hosted in the cloud with Kubernetes, this has some important improvements over the original legacy system. By hosting the system in the cloud it’s possible to create customer centric services like the online reservation system. It also makes it possible to for each store to have a shared customer base because all their customers are stored in a central place. Kubernetes also allows for much easier scalability compared than the old system.
Our final architecture can be seen on the picture below:

![New architecture](/assets/system_architecture.png "New architecture")

## Technologies
| Technology | Type | Usage |
| - | - | - |
| Python 3.9 | Language | Used in our Gateway, Subscription, &  Metadata service. Its also used for our migration services |
| C# 10 | Language | Used for developing the Reservation & Restock service |
| Java 17 | Language | Used in our CamelPro service together with Apache Camel |
| Rust 1.57 | Language | Used in Warehouse service |
| Protobuf 3 | Language | A IDL language used for specifying our gRPC contracts between services |
| gRPC | Framework | Used for serialization and communication between services |
| Apache Camel | Framework | Used for translating our legacy csv files to Kafka messages |
| Docker | Container Platform | Used for containerization |
| Kubernetes | Container Orchestration | Used to orchestrate docker containers |
| Camunda | Workflow and Decision Automation | Decision automation system for managing business workflows, used to manage user request about restock and adding new items |
| Apache Kafka | Message Broker | Event streaming platform for sending communication between our services |
| SQLite | Database | In-memory database for persisting our data |
| Kafdrop | Tool | Web UI for viewing Kafka topics and browsing consumer groups |
| Insomnia | Tool | API Client for GraphQL, REST, and gRPC |
| BloomRPC | Tool | gRPC consumer |

### gRPC

We use gRPC as a way for each service to serialize their entity classes and communicate with the other services through the gateway. We use protocol buffers to define the end points of each service.

### Camunda

We use Camunda for handling restock requests or requests for a new item to be added to the database. Camunda is a perfect match for this use case because it allows us to easily visualize the whole restock process and handle user task throughout the process. Our restock process is shown on the BPMN diagram below, we also use a decision table to validate the request before we continue with the process. This allows us to easily manage the rules which determines whether a request is valid or invalid.  

![Camunda BPMN model for Restock process](/assets/restock_model.png "Restock Process")



![Decision Table for Restock process](/assets/restock_decision_table.png "Restock decision table")

### Kafka

We use Kafka as our message broker for sending event-based messages between our applications. It allows the services to communicate asynchronously with each other and without knowledge of their consumers.

### Docker and Kubernetes

We use Docker to containerize all our services and thereby make it possible to run the services without requiring us to install all the different runtimes for each service before we can test them. Containerizing all our services also makes it possible to use Kubernetes as a deployment strategy, this makes it possible to run multiple instances of the same service, monitor for errors, and automatically recover from service crashes.

# Development Process

We started this process by discussing the business case. It was important to have a good and realistic scenario from the get-go.
The business case was agreed upon, and the development process could start.

Process began with the development team agreeing upon a work schedule as well as work rituals. We agreed on having a scrum-like
daily meeting each day to follow up on each other on how the project was coming along. We divided the project into smaller tasks,
again, similar to scrum and their user stories, and shared and distributed them on a project board, on GitHub. The board can be
seen on the following link: https://github.com/System-Integration-Exam/SI-Exam/projects/1.

# Run
## Prerequisites
The Project requires Docker and Kubernetes (with minikube) to run locally.
The system also requires a REST API testing tool like Postman, CURL,  or Insomnia for making calls to the Gateway Service.

## Kubernetes with Minikube
_Tested on Windows 10, Manjaro & Fedora Linux_

### 1. Start minikube cluster
```
$ minikube start
```
### 2. Tunnel to cluster
_This blocks the terminal so it's a good idea to run it in a seperate terminal window._
```
$ minikube tunnel
```
### 3. Apply kubernetes deployments
_This assummes that you are stading in the root folder for the repository._
```
$ kubectl apply -f .kubernetes
```

## Access to services

Only some of the services can be access externaly from outside the cluseter:
- Gateway: `20090`
- Camunda: `10000`
- Kafdrop: `9000`
- Kafka broker: `9094`

If access is required to any other service, for e.g testing purposes, its possible to port forward the internal cluter port in k8s by changing and running the following command:
```
$ kubectl port-forward service/{serviceName} {servicePort}
```

# Gateway Endpoints


| Endpoint      | HTTP Method   | Description |
| -             | :-:           | -
| /             | `GET`         |
| /health       | `GET`         |

## Metadata
### Book

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /book         | `GET`         | Get a list of all books
| /book/\<id>   | `GET`         | Get a specific book by its id
| /book/\<id>   | `DELETE`      | Remove an book from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /book         | `POST`        | <pre>{<br>  "title": "string",<br>  "author": "string",<br>  "rating": int<br>}</pre> | Create a new book
| /book/\<id>   | `PUT`         |<pre>{<br>  "title": "string",<br>  "author": "string",<br>  "rating": int<br>}</pre> | Update an existing book

### Song

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /song         | `GET`         | Get a list of all songs
| /song/\<id>   | `GET`         | Get a specific song by its id
| /song/\<id>   | `DELETE`      | Remove an song from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /song         | `POST`        | <pre>{<br>  "title": "string",<br>  "duration_sec": int,<br>  "vinyl_id": "string"<br>}</pre> | Create a new song
| /song/\<id>   | `PUT`         | <pre>{<br>  "title": "string",<br>  "duration_sec": "string",<br>  "vinyl_id": "string"<br>}</pre> | Update an existing song

### Vinyl

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /vinyl         | `GET`         | Get a list of all vinyls
| /vinyl/\<id>   | `GET`         | Get a specific vinyl by its id
| /vinyl/\<id>   | `DELETE`      | Remove an vinyl from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /vinyl         | `POST`        | <pre>{<br>  "artist": "string",<br>  "genre": "string"<br>}</pre> | Create a new vinyl
| /vinyl/\<id>   | `PUT`         | <pre>{<br>  "artist": "string",<br>  "genre": "string"<br>}</pre> | Update an existing vinyl

## Reservation

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /reservation         | `GET`         | Get a list of all reservations

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /reservation         | `POST`        | <pre>{<br>  "id":"string",<br>  "item_id":"string",<br>  "user_id":"string",<br>  "status":"string", <br>  "store_id":int <br>}</pre> | Create a new reservation
| /reservation/complete         | `POST`        | <pre>{<br>  "id": "string"<br>}</pre> | Mark a reservation as completed
| /reservation/cancel         | `POST`        | <pre>{<br>  "id": "string"<br>}</pre> | Mark a reservation as canceled


## Restock


| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /restock         | `POST`        | <pre>{<br>  "requestText": "string",<br>  "item_type": "string",<br>  "existingItemCount": int, <br>  "storeId":int,<br>  "itemId": "string"<br>}</pre> | Restock item


## Subscription

### Customer

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /customer         | `GET`         | Get a list of all customers
| /customer/\<id>   | `GET`         | Get a specific customer by its id
| /customer/\<id>   | `DELETE`      | Remove an customer from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /customer         | `POST`        | <pre>{<br>  "subscription_id": "string", <br>  "first_name": "string", <br>  "last_name": "string",<br>  "email": "string",<br>  "phone_number": "string"<br>}</pre> | Create a new customer
| /customer/\<id>   | `PUT`         | <pre>{<br>  "first_name": "string",<br>  "last_name": "string",<br>  "email": "string", <br>  "phone_number": "string"<br>}</pre> | Update an existing customer


### Subscription

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /subscription         | `GET`         | Get a list of all subscriptions
| /subscription/\<id>   | `GET`         | Get a specific subscription by its id
| /subscription/\<id>   | `DELETE`      | Remove an subscription from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /subscription         | `POST`        | <pre>{<br>  "is_active": bool<br>  "expiration_date": "string"<br>}</pre> | Create a new subscription
| /subscription/\<id>   | `PUT`         | <pre>{<br>  "is_active": bool<br>  "expiration_date": "string"<br>}</pre> | Update an existing subscription



## Warehouse


| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /store         | `GET`         | Get a list of all stores
| /store/\<id>   | `GET`         | Get a specific store by its id
| /store/\<id>   | `DELETE`      | Remove a store from the system
| /store/remove-book=<store_id>&<book_id>   | `DELETE`      | Remove a book from a store
| /store/add-book=<store_id>&<book_id>         | `POST`        | Add book to store
| /store/total-book=<store_id>&<book_id>   | `GET`         | Get the total amount of a specific book from a specific store
| /store/remove-vinyl=<store_id>&<vinyl_id>   | `DELETE`      | Remove a vinyl from a store
| /store/add-vinyl=<store_id>&<vinyl_id>         | `POST`        | Add vinyl to store
| /store/total-vinyl=<store_id>&<vinyl_id>   | `GET`         | Get the total amount of a specific vinyl from a specific store


| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /store         | `POST`        | <pre>{<br>  "address": "string",<br>  "phone_number": "string",<br>  "email": "string"<br>}</pre> | Create a new store
| /store/\<id>   | `PUT`         | <pre>{<br>  "address": "string",<br>  "phone_number": "string",<br>  "email": "string"<br>}</pre> | Update an existing store

