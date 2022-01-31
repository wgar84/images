FROM r-base:latest

RUN apt update
RUN apt install -y gdal-bin libgdal-dev pandoc texlive-xetex graphviz-dev python3 python3-pip \
    r-cran-devtools r-cran-ggplot2 r-cran-scales r-cran-irkernel r-cran-plumber

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# RUN mkdir ggfolha
# COPY ggfolha/* ./ggfolha/

COPY requirements.R .
COPY token .
RUN Rscript requirements.R

USER docker
WORKDIR /home/docker/app

RUN jupyter notebook --generate-config

RUN echo \
    "c.NotebookApp.token = '4fcbc72db3dadfc4585c374a5c83b566b9a86944b1489e79'" \
    >> /home/docker/.jupyter/jupyter_notebook_config.py

RUN echo \
    "c.NotebookApp.password = u'sha1:0bff055a03ce:c09cde8bab532481515d631285948252f72e8cc5'" \
    >> /home/docker/.jupyter/jupyter_notebook_config.py

# ENTRYPOINT [ "wait-for-it.sh", "driver:4444", "--", "/bin/sh",  "-c" ]
# CMD jupyter notebook --no-browser --ip=0.0.0.0
