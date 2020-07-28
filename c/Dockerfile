FROM first

WORKDIR /app

# activate the environment
ENV PATH /opt/conda/envs/occ_env/bin:$PATH
RUN /bin/bash -c "source activate occ_env"

EXPOSE 3893

# start server
COPY run.py .
CMD [ "python", "run.py" ]
