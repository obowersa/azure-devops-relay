FROM relaysh/core:latest-python
RUN pip --no-cache-dir install quart
COPY "./handler.py" "/handler.py"
ENTRYPOINT []
CMD ["python3", "/handler.py"]

LABEL "org.opencontainers.image.title"="Azure Devops agent pool resized"
LABEL "org.opencontainers.image.description"="Blah blah blah TODO: Remove Blah blah blah"
LABEL "sh.relay.sdk.version"="v1"