# Example webhook payloads from ADO serivce hooks

Each file maps to an ADO Service Hook event type ( specifically pipeline/repo related)
List of events: [Azure Devops Events](https://docs.microsoft.com/en-us/azure/devops/service-hooks/events?view=azure-devops)


Fields where I'm not sure on the usefulness are marked with a ? at the begining of the name
## Globaly useful fields
```
body:
    eventType: ""
```
## build.complete.json
Useful fields:
```
resource:
    url: ""
    buildNumber: ""
    startTime: ""
    finishTime: ""
    reason: ""
    status: ""
    sourceGetVersion: ""
``` 

## elasticagentpool.resized.json
Useful fields:
```
resource:
    poolId: 0
    poolName: ""
    resourceId: ""
    previousSize: 0
    newSize: 0    
```

## git.pullrequest.created.json
Useful fields:
```
resource:
    repository:
        remoteUrl: ""
    pullRequestId: 0
    status: ""
    creationDate: ""
    mergeStatus: ""
    ?mergeId: ""
    ?sourceRefName: ""
    ?targetRefName: ""
    
```

## git.pullrequest.merged.json/git.pullrequest.updated.json
Useful fields:
```
resource:
    repository:
        remoteUrl: ""
    pullRequestId: 0
    status: ""
    closedDate: ""
    creationDate: ""
    mergeStatus: ""
    ?mergeId: ""
    ?sourceRefName: ""
    ?targetRefName: ""
```

## git.push.json
```
resource:
    repository:
        id: ""
        remoteUrl: ""
    pushId: 0
    date: ""

```

## ms.vss-code.git-pullrequest-comment-event.json
TODO
## ms.vss-release.release-abandoned-event.json