# Dockerfile Tensorflow
Wanting to explore ML/AI implementations in python with tensorflow while avoiding most of the installation and maintenance?  OK with Docker?  This is it.

After installing tensorflow directly in wsl2 and thinking about [pets versus cattle](http://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/) this seemed like a better alternative, a means to have a consistent, performant environment without spending time with install, update or versioning.  It also seemed like an easier way to share with others.  Potentially, it may make it easier to deliver tensorflow-based products. 

## Background Material
The [Tensorflow Docker](https://www.tensorflow.org/install/docker) documentation was a good start, useful for making sure things worked.  (Also worth a look if one wants other base images, for example gpu enabled.)  The documenation for a composable from [Valohai](https://docs.valohai.com/howto/docker/docker-build-image/) helped while drafting the first Dockerfile for this.  There are some [interesting ideas](https://towardsdatascience.com/how-to-deploy-machine-learning-models-with-tensorflow-part-2-containerize-it-db0ad7ca35a7) for how to deploy model in docker to support inference which might be useful later.

At the moment this is being done with vscode in win10 with Remote-WSL, Docker, Pylance and Python extensions.  And Tabnine.  Docker is Docker Desktop 4.3.2 with v2 enabled.  In wsl2, the distro is Ubuntu 20.04.3.  This assumes implementation in python.  

## How to Make This Go
Instructions for making this work

### do these things once
Add this to ~/.bashrc
```
export DOCKER_USER="$(id -u):$(id -g)"
```
This won't take effect until the bashrc is run again, which requires sourcing the bashrc or logging out and logging back into wsl2 distribution.  To avoid having to that, run this on the command line:
```
export 'DOCKER_USER="$(id -u):$(id -g)"'
```

Add any needed python modules to `requirements.txt`.  Update as needed.

Not completely sure, but one may want to run this:
```
$ docker pull tensorflow/tensorflow
```
and this seems common advice, but doesn't seem to be necessary
```
$ sudo usermod -aG docker $USER
```

### do this to build and run
To build and run (do this in the vscode terminal)
```
$ docker compose build tf
$ docker compose run tf
```
This puts one into a shell inside the docker environment.  Note that if one is not using v2 compose, e.g. with the linux docker engine, this will work with `docker-compose` as well.

An alternative is to use the Docker extension in vscode to start and attach to the container.  

### in the container 
Once the container is running, `/working` provides access to the local directory.

To see if things are working, try this:
```
tf-docker / > cd /working
tf-docker /working > python example_tf.py 
```
The results should look like:
```
2022-01-15 23:09:38.586021: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
tf.Tensor(-851.3829, shape=(), dtype=float32)
```
