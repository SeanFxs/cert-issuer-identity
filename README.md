
# cert-issuer-identity

Blockchain certificate identity service


## Quick Start with Docker

1. First ensure you have Docker installed. [See our Docker installation help](https://github.com/blockchain-certificates/developer-common-docs/blob/master/docker_install.md).
    
2. Git clone the repository

    ```
    git clone https://github.com/blockchain-certificates/cert-issuer-identity.git
    ```

3. From a command line in the cert-issuer-identity dir, run docker-compose

    ```
    cd cert-issuer-identity
    docker-compose build
    ```

4. Start the container

    ```
    docker-compose up
    ```

5. Access cert-issuer-identity at `http://localhost:5002`.


## Running the CLI locally

1. Ensure you have an python environment. [Recommendations](https://github.com/blockchain-certificates/developer-common-docs/blob/master/virtualenv.md)

2. Install [mongodb](https://docs.mongodb.com/v3.0/installation/)

3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Setup your config.py file
    
5. To run the server, please execute the following:
    ```bash
    python cert-issuer-identity/app.py
    ```

You can see the Swagger API specification at this URL:

```
http://localhost:5002/ui/
```

## API Documentation

The API documentation is currently hosted here:

[http://cert-issuer-identity.herokuapp.com/ui/](http://cert-issuer-identity.herokuapp.com/ui/)

Updates coming soon!

## Unit tests

This project uses tox to validate against several python environments.

1. Ensure you have an python environment. [Recommendations](https://github.com/blockchain-certificates/developer-common-docs/blob/master/virtualenv.md)

2. Run tests
    ```
    ./run_tests.sh
    ```

## Release Docker image

```
docker build -t blockcerts/certissueridentity_web:<version> .
docker login
docker push blockcerts/certissueridentity_web:<version>
```


## Contact

Contact [certs@mit.edu](mailto:certs@mit.edu) with questions
