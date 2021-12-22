# System Integration 2021 Exam

## Contributors
- [Emil Jógvan Svensmark - cph-eb122](https://github.com/Svensmark)
- [Emil Skovbo - cph-es149](https://github.com/Emil-Skovbo)
- [Henning Wiberg - cph-hw98](https://github.com/Mutestock)
- [Sofus Hilfling Nielsen - cph-sn331](https://github.com/sofushn)

[Exam Assignment Document]()

The repository is hosted online on GitHub at https://github.com/System-Integration-Exam/SI-Exam

## Video

# Table of Contents

- [System Integration 2021 Exam](#system-integration-2021-exam)
  * [Contributors](#contributors)
  * [Video](#video)
  * [Business case - Book & Vinyl reservation system](#business-case---book---vinyl-reservation-system)
  * [Requirements](#requirements)
- [Architecture](#architecture)
  * [Technologies](#technologies)
- [Development Process](#development-process)
- [Run](#run)
  * [Prerequisites](#prerequisites)
  * [Minikube](#minikube)
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

A book & vinyl subscription renting chain called Vintage Champions. The concept is derrived from an older version of blokbuster where you physically had to pick up the item in the store. Each store have their own inventory of books & vinyls that can be rented if you have a subscription service with the chain. 

## Domain

We designed our system with a domain-driven-design approrach which ment that we needed a domain diagram that contained all our vocabularur from our business domain:
![Domain Model](/assets/domain_model.png "Domain Model")

## Requirements

- Integration with external REST API for retriving item metadata
- 
- Transform old customer data from legacy system into moden system
- Use of BPMN to handle restocking of new or existing items
- Microservice orchestration with Kubernetes
- Basic console logging and monitoring

# Architecture

## Legacy System

Vintage Champions is currently using an old legacy system that is deployed to each of their stores. This system has a basic frontend for the employees and stores all their data in indiviual csv files.

![Old architecture](/assets/legacy_system_architecture.png "Old architecture")

## Moden Solution

The new system should make it possible for the scenario's shops to communicate with each other. It should also be scalable where the old system was not. We came to the conclusion, that a microservice-like architecture would be more optimal. After discussing some different setups, we came to a conclusion and made the final diagram:

![New architecture](/assets/system_architecture.png "New architecture")

## Technologies
| Technology | Type | Usage |
| - | - | - |
| Python 3.9 | Language | Used in our Gateway, Subscription, &  |
| C# 10 | Language | |
| Java 17 | Language | |
| Rust 1.57 | Language | |
| Protobuf 3 | Language | |
| gRPC | Framework |  |
| Appache Camel | Framework | |
| Docker | Container Platform | |
| Kubernetes | Container Orchestration | |
| Camunda | Workflow and Decision Automation | |
| Apache Kafka | Message Broker | Event streaming platform for sending comunicating between our services |
| SQLite | Database | In-memory database for persisting our data |
| Kafdrop | Tool | Web UI for viewing Kafka topics and browsing consumer groups |
| Insomnia | Tool | API Client for GraphQL, REST, and gRPC |
| BloomRPC | Tool | gRPC consumer |

### gRPC



### Camunda

We use camunda for handling restock requests or reqeust for a new item to be added to 

![Camunda BPMN model for Restock process](/assets/restock_model.png "Restock Process")

![Decision Table for Restock process]( "")

### Kafka

We use Kafka as our message broker for sending event based messages between our applications. It allows the services to commynicate asyncrosly with each other and without knowledge of their consuemrs. 

### Docker & Kubernetes



# Development Process

After this we discussed what a suboptimal existing product would look like. Since the frontend isn't a requirement, we decided that the frontend would in this scenario require the usage of some features, that the old backend provided. Our system should be an optimized stand-in for the legacy backend system. This is what the scenario's old system looks like:

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
_This blocks the terminal so run in seperate terminal window_
```
$ minikube tunnel
```
### 3. Apply kubernetes deployments
_This assummes that you are stading in the root folder for the repository_
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

