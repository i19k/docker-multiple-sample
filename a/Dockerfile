# create environment
FROM continuumio/miniconda3

WORKDIR /app

# create the environment
COPY environment.yml .
RUN conda env create -f environment.yml

# activate the environment
ENV PATH /opt/conda/envs/occ_env/bin:$PATH
RUN /bin/bash -c "source activate occ_env"