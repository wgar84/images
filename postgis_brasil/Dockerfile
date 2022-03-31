FROM python:latest

# RUN apt update
# RUN apt install -y git

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN rm requirements.txt

RUN groupadd -g 1000 jovyan
RUN useradd -ms /bin/bash -u 1000 -g 1000 jovyan

#COPY bin/* /usr/local/bin/

USER jovyan

# ENV PATH "${PATH}:/home/jovyan/.local/bin"

#COPY utils/ /home/jovyan/utils
#ENV PYTHONPATH "${PYTHONPATH}:/usr/local/bin"

WORKDIR /home/jovyan/app
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/app"
# COPY bin/* ./

RUN jupyter notebook --generate-config

RUN echo \
    "c.NotebookApp.token = '4fcbc72db3dadfc4585c374a5c83b566b9a86944b1489e79'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py

RUN echo \
    "c.NotebookApp.password = u'sha1:0bff055a03ce:c09cde8bab532481515d631285948252f72e8cc5'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py
