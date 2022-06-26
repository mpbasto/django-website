# For pyenv tags in the terminal, add the following to the ~/.zshrc file
# NOTE: If using ohmyzsh, it might delete the contents of the file so it is necessary
# to add this script after installing ohmyzsh

if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
fi
export PATH=/usr/local/bin:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"