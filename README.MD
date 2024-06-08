# Chess Backend

This project is a simple backend for a chess application built using FastAPI, MongoDB, Kafka, and Domain-Driven Design (DDD). The chess logic is implemented using the Python Chess library.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Docker
- Docker Compose

## Makefile Commands

The Makefile provides several commands to manage the application and its dependencies. Below is a list of the available commands:

### Start the Application

```sh
make app
make storages
```

    This command builds and starts the application using Docker Compose.

    or

```bash
make all
```

Access the application at `http://localhost:8000`.

### Stop the Application

```bash
make app-down
make storages-down
```

This command stops the application and removes the containers.


## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
