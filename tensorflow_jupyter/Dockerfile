FROM tensorflow/tensorflow:2.9.1-gpu-jupyter

COPY requirements.txt .

# RUN rm /etc/apt/sources.list.d/cuda.list

# RUN rm /etc/apt/sources.list.d/nvidia-ml.list

# RUN apt-key del 7fa2af80

# RUN apt update && apt install -y --no-install-recommends wget

# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb

# RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt update -y

# RUN DEBIAN_FRONTEND=noninteractive apt install cuda libopenexr-dev -y
RUN DEBIAN_FRONTEND=noninteractive apt install libopenexr-dev -y


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


