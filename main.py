import config
import core

for remote, local in config.STORAGE.items():
    repo = config.github.get_repo('panhaoyu/' + remote)
    storage = core.Storage(local, repo)
    storage.upload()

input('Press Enter to Exit.')
