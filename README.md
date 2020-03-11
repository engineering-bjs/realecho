# realecho

A server that actually echos your stuff back through docker (stdout).

Listens internally on port 5000.

`docker run -p 5000:5000 -e PPRINT_JSON='1' bjshomedelivery/realecho`

[Dockerhub](https://hub.docker.com/repository/docker/bjshomedelivery/realecho)

## Envs

 - `PPRINT_JSON` if present will pretty print + sort the body back out to you, must be json
