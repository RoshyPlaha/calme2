# Used by appspecfile

# Install / Check that Conda is installed
if ! command -v conda &> /dev/null
then
    echo "Conda could not be found, so installing..."
    echo "Installing Miniconda on the EC2 Instance"
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh;
    echo 'Install miniconda';
    sudo chmod 777 ~/miniconda.sh
    sudo /miniconda.sh -b -p $HOME/miniconda -u;
    eval "$(~/miniconda/bin/conda shell.bash hook)";
else
    echo "Conda is already installed"
fi
