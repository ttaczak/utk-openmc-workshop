# This Dockerfile adds the workshop files to the base dockerfile to make a
# complete neutronics-workshop docker image

# This Dockerfile can be build locally or a prebuild image can be downloaded

# To download the prebuild image
# docker pull ghcr.io/fusion-energy/neutronics-workshop

# To build this Dockerfile into a docker image:
# docker build -t neutronics-workshop -f .devcontainer/Dockerfile .

# then run with this command
# docker run -p 8888:8888 neutronics-workshop

# remote image
FROM ghcr.io/fusion-energy/neutronics-workshop:base as base
# local image
# FROM neutronics-workshop:base as base

# Copy over the local repository files
COPY tasks tasks/
COPY file_unzipper .
WORKDIR /tasks

# this sets the port, gcr looks for this varible
FROM base as jupyter_cmd

ENV PORT 8888

# could switch to --ip='*'
CMD ["jupyter", "lab", "--notebook-dir=/tasks", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
