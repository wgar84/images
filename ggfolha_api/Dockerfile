FROM r-base:latest

RUN apt update
RUN apt install -y gdal-bin libgdal-dev pandoc texlive-xetex graphviz-dev python3 python3-pip

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash -u 1000 -g 1000 jovyan

COPY requirements.R .

RUN mkdir ggfolha
COPY ggfolha/* ./ggfolha/

RUN R CMD requirements.R

USER jovyan

#COPY utils/ /home/jovyan/utils
#ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/utils"

WORKDIR /home/jovyan/app
# ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/app"
# COPY bin/* ./


# COPY bin/* /usr/local/bin/

RUN jupyter notebook --generate-config

RUN echo \
    "c.NotebookApp.token = '4fcbc72db3dadfc4585c374a5c83b566b9a86944b1489e79'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py

RUN echo \
    "c.NotebookApp.password = u'sha1:0bff055a03ce:c09cde8bab532481515d631285948252f72e8cc5'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# ENTRYPOINT [ "wait-for-it.sh", "driver:4444", "--", "/bin/sh",  "-c" ]
# CMD jupyter notebook --no-browser --ip=0.0.0.0
