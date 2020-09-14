# Used by appspecfile

# Install / Check that Conda is installed
if ! command -v conda &> /dev/null
then
    echo "Conda could not be found, so installing..."
    echo "Installing Miniconda on the EC2 Instances"
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh;
    echo 'Install miniconda';
    /miniconda.sh -b -p -u $HOME/miniconda;
    eval "$(/miniconda/bin/conda shell.bash hook)";
else
    echo "Conda is already installed"
fi

# Lets activate the conda environment
echo "Activating conda environment"
conda env create --file /python/outbound/environmental_droplet.yml
echo "Finished"



