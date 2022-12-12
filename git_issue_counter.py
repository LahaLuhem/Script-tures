from git import Repo, RemoteReference
import re
import datetime

repo: Repo = Repo("/Users/mehulahal/StudioProjects/medappv2")

# Getting release branches
release_regex = re.compile(r'/release*')
release_number_regex = re.compile(r'\d+(\.|-)\d+(\.|-)(\d+|X+)\w*')
release_branches: list[RemoteReference] = [useful_branch for useful_branch in repo.remotes[0].refs if
                                           release_regex.search(
                                               useful_branch.name) is not None
                                           and release_number_regex.search(useful_branch.name) is not None]

# Filtering release branches by year of creation
date_regex = re.compile(r'\w+ \w+ \d+ \d+:\d+:\d+ \d+ \+\d+')
data_range_validation_indices: [bool] = []
for release_branch in release_branches:
    summary = repo.git.show("--summary", repo.git.merge_base(release_branch.name, "origin/develop"))
    timestamp = datetime.datetime.strptime(date_regex.search(summary).group(), '%a %b %d %H:%M:%S %Y +%f')
    data_range_validation_indices.append(2020 <= timestamp.year < 2021)

skipped_releases: list[RemoteReference] = [weird_branch for weird_branch in release_branches if
                                           release_number_regex.search(weird_branch.name) is None]
release_branches_in_range = [d for (d, remove) in zip(release_branches, data_range_validation_indices) if remove]
del release_branches

# Ordering by ascending order of releases
release_branches_in_range.sort(
    key=lambda branch: int(re.split(r'\D+', release_number_regex.search(branch.name).group())[1]))

# Get commit messages for successive releases
issues_set: set = set()
ticket_regex = re.compile(r'[Mm][Aa][AFaf][-_]\d+')
for n_elem, n1_elem in zip(release_branches_in_range, release_branches_in_range[1:]):
    commits_dump: str = repo.git.cherry("-v", n_elem.name, n1_elem.name)
    tickets = ticket_regex.findall(commits_dump)
    [issues_set.add(issue) for issue in tickets]

print("\n".join(issues_set))
