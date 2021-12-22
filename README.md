# SI-Exam

# How to run
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
```
$ kubectl apply -f .kubernetes
```

### 4. Access to services
This can by default only be done through the gateway. If access to the service is needed, its possible to do a port forward in k8s by changing and running the command:
```
$ kubectl port-forward service/reservation-service 5000
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
| /book/\<id>   | `PUT`         |<pre>{<br>  "id": "string",<br>  "title": "string",<br>  "author": "string",<br>  "rating": int<br>}</pre> | Update an existing book

### Song

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /song         | `GET`         | Get a list of all songs
| /song/\<id>   | `GET`         | Get a specific song by its id
| /song/\<id>   | `DELETE`      | Remove an song from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /song         | `POST`        | <pre>{<br>  "title": "string",<br>  "duration_sec": int,<br>  "vinyl_id": "string"<br>}</pre> | Create a new song
| /song/\<id>   | `PUT`         | <pre>{<br>  "id": "string",<br>  "title": "string",<br>  "duration_sec": "string",<br>  "vinyl_id": "string"<br>}</pre> | Update an existing song

### Vinyl

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /vinyl         | `GET`         | Get a list of all vinyls
| /vinyl/\<id>   | `GET`         | Get a specific vinyl by its id
| /vinyl/\<id>   | `DELETE`      | Remove an vinyl from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /vinyl         | `POST`        | <pre>{<br>  "artist": "string",<br>  "genre": "string"<br>}</pre> | Create a new vinyl
| /vinyl/\<id>   | `PUT`         | <pre>{<br>  "id": "string",  <br>  "name": "string"<br>  "vinylination_date": "string"<br>}</pre> | Update an existing song

## Reservation

### Reservation

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /reservation         | `GET`         | Get a list of all reservations

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /reservation         | `POST`        | <pre>{<br>  "id":"string",<br>  "item_id":"string",<br>  "user_id":"string",<br>  "status":"string", <br>  "store_id":int <br>}</pre> | Create a new reservation
| /reservation/complete         | `POST`        | <pre>{<br>  "id": "string"<br>}</pre> | Mark a reservation as completed
| /reservation/cancel         | `POST`        | <pre>{<br>  "id": "string"<br>}</pre> | Mark a reservation as canceled


### Restock

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /song         | `GET`         | Get a list of all songs
| /song/\<id>   | `GET`         | Get a specific song by its id
| /song/\<id>   | `DELETE`      | Remove an song from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /song         | `POST`        | <pre>{<br>  "name": "string"<br>  "songination_date": "string"<br>}</pre> | Create a new song
| /song/\<id>   | `PUT`         | <pre>{<br>  "name": "string"<br>  "songination_date": "string"<br>}</pre> | Update an existing song


## Subscription

### Customer

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /customer         | `GET`         | Get a list of all customers
| /customer/\<id>   | `GET`         | Get a specific customer by its id
| /customer/\<id>   | `DELETE`      | Remove an customer from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /customer         | `POST`        | <pre>{<br>  "name": "string"<br>  "customerination_date": "string"<br>}</pre> | Create a new customer
| /customer/\<id>   | `PUT`         | <pre>{<br>  "name": "string"<br>  "customerination_date": "string"<br>}</pre> | Update an existing song


### Subscription

| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /subscription         | `GET`         | Get a list of all subscriptions
| /subscription/\<id>   | `GET`         | Get a specific subscription by its id
| /subscription/\<id>   | `DELETE`      | Remove an subscription from the system

| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /subscription         | `POST`        | <pre>{<br>  "name": "string"<br>  "subscriptionination_date": "string"<br>}</pre> | Create a new subscription
| /subscription/\<id>   | `PUT`         | <pre>{<br>  "name": "string"<br>  "subscriptionination_date": "string"<br>}</pre> | Update an existing song



## Warehouse


| Endpoint      | HTTP Method   | Description |
| -             | :---------:   | -
| /store         | `GET`         | Get a list of all stores
| /store/\<id>   | `GET`         | Get a specific store by its id
| /store/\<id>   | `DELETE`      | Remove a store from the system
| /store/remove-book=<store_id>&<book_id>   | `DELETE`      | Remove a book from a store
| /store/add-book=<store_id>&<book_id>         | `POST`        | <pre></pre> | Add book to store
| /store/total-book=<store_id>&<book_id>   | `GET`         | Get the total amount of a specific book from a specific store
| /store/remove-vinyl=<store_id>&<vinyl_id>   | `DELETE`      | Remove a vinyl from a store
| /store/add-vinyl=<store_id>&<vinyl_id>         | `POST`        | <pre></pre> | Add vinyl to store
| /store/total-vinyl=<store_id>&<vinyl_id>   | `GET`         | Get the total amount of a specific vinyl from a specific store


| Endpoint      | Http Method   | Request Body  | Description
| -             | :-:           | -             |   -
| /store         | `POST`        | <pre>{<br>  "address": "string",<br>  "phone_number": "string",<br>  "email": "string"<br>}</pre> | Create a new store
| /store/\<id>   | `PUT`         | <pre>{<br>  "id": int,<br>  "address": "string",<br>  "phone_number": "string",<br>  "email": "string"<br>}</pre> | Update an existing store

