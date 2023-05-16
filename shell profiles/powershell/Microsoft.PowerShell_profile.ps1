oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\night-owl.omp.json" | Invoke-Expression

# Git
New-Alias -Name "git temp" -Value "git checkout"

function git-cleanup-local {
	# update local list of pruned branches on the remote to local:
	git fetch --prune 
	# delete local branches that have been merged to develop
	git branch --merged remotes/origin/develop | %{$_.trim()} | ?{$_ -notmatch 'develop'} | %{git branch -d $_}
	# remove stale refs (local refs to branches that are gone on the remote)
	git remote prune origin
}

function git-cleanup-remote {
	# update local list of pruned branches on the remote to local:
	git fetch --prune 
	# delete branches on remote origin that have been merge to develop
	git branch --merged remotes/origin/develop -r | %{$_.trim().replace('origin/', '')} | ?{$_ -notmatch 'develop'} | %{git push --delete origin $_}
	# remove stale refs (local refs to branches that are gone on the remote)
	git remote prune origin
}

# Flutter + Dart FVM environment manager
function global:flutter {
	fvm flutter $args
}
function global:dart {
	fvm dart $args
}

# Python
New-Alias -Name "pip upgrade all" -Value "pip-review --local --interactive"
