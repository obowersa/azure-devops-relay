FROM relaysh/core:latest-python
RUN pip --no-cache-dir install quart
COPY "./handler.py" "/handler.py"
ENTRYPOINT []
CMD ["python3", "/handler.py"]

LABEL "org.opencontainers.image.title"="Azure Devops pull request merged"
LABEL "org.opencontainers.image.description"="This trigger fires when an Azure Devops pull request is merged."
LABEL "sh.relay.sdk.version"="v1"