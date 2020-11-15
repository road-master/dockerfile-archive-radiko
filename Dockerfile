FROM mstmelody/python-ffmpeg:20201114221500 as production
COPY ./Pipfile ./Pipfile.lock /workspace/
RUN pip --no-cache-dir install pipenv \
 && pipenv install --deploy --system \
 && pip uninstall -y pipenv virtualenv-clone virtualenv
COPY . /workspace
VOLUME ["/workspace/output"]
ENTRYPOINT [ "python3", "archive.py" ]

FROM production as development
# see: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV PIPENV_VENV_IN_PROJECT=1
RUN pip --no-cache-dir install pipenv \
 && pipenv install --deploy --dev
ENTRYPOINT [ "pipenv", "run" ]
CMD ["pytest"]
