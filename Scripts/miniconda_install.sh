echo "Installing Miniconda on the EC2 Instances"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh;
echo 'Install miniconda';
sh ~/miniconda.sh -b -p $HOME/miniconda;
eval "$(~/miniconda/bin/conda shell.bash hook)";