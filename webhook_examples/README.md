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


todo: group pull request types ? 

## pullrequest-common
resource:
    repository:
        remoteUrl: ""
    pullRequestId: 0
    status: ""
    creationDate: ""
    mergeStatus: ""
    mergeId: ""
    sourceRefName: ""
    targetRefName: """


## git.pullrequest.created.json
Useful fields:
```
- pullrequest-common
    
```
## git.pullrequest.merged.json/git.pullrequest.updated.json
Useful fields:
todo: double check if there's a double event trigger of updated+merged on pr merge
```
- pullrequest-common
resource:
    closedDate: """"
```
## git.pullrequest.updated.json
todo: double check if there's a double event trigger of updated+merged on pr merge

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