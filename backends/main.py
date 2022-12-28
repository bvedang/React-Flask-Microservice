def getRepoStars(repositories:list,github)->list:
    repoStarscount = []
    for repos in repositories:
        reponame = repos.split(':')
        repo = github.repository(reponame[0], reponame[-1])
        starobj = {}
        starobj['name'] = reponame[-1]
        starobj['value'] = repo.stargazers_count
        repoStarscount.append(starobj)
    return repoStarscount

def getRepoForks(repositories: list,github)->list:
    repoforkCount = []
    for repos in repositories:
        reponame = repos.split(':')
        repo = github.repository(reponame[0], reponame[-1])
        forkobj = {}
        forkobj['name'] = reponame[-1]
        forkobj['value'] = repo.forks_count
        repoforkCount.append(forkobj)
    return repoforkCount


