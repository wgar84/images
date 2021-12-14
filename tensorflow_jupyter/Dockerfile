FROM tensorflow/tensorflow:nightly-gpu-py3-jupyter

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash -u 1000 jovyan

USER jovyan

WORKDIR /home/jovyan/app

RUN jupyter notebook --generate-config

RUN echo \
    "c.NotebookApp.token = '4fcbc72db3dadfc4585c374a5c83b566b9a86944b1489e79'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py

RUN echo \
    "c.NotebookApp.password = u'sha1:0bff055a03ce:c09cde8bab532481515d631285948252f72e8cc5'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py


