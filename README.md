# docker-multiple-sample
Sample docker files to create multiple docker images, inheriting, networking...

Main image is from *miniconda* and sample application contains a flask server.

# Build
    docker-compose build

# Run
    docker-compose run
    
Go to http://localhost:3892 and http://localhost:3893


# services
## build
Build folder that contains the Dockerfile. There may be multiple services, so they should be in subfolders.

## image
Docker will be build the docker image in this name. If there is no build option here, docker try to use local/remote(Docker Hub) images with this name.

## depends_on
Build operation will wait for this image until the dependent image build operation is completed.

## ports
Same as the port option:
    docker run -p "out_docker_port:in_docker_port"
Docker will map these ports while running the service. If you want to use your service outside of your Docker, you have to specify this option.
